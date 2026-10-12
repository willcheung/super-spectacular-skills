/* MIT; pure calculations shared by the CLI and browser. No external data or network. */
export function validate(p) {
  const fail=(s)=>{throw new Error(s);};
  const num=(v,s,lo=-Infinity,hi=Infinity)=>{if(typeof v!=='number'||!Number.isFinite(v)||v<lo||v>hi)fail(s+' must be a finite number from '+lo+' to '+hi);};
  const integer=(v,s,lo=1900,hi=2300)=>{num(v,s,lo,hi);if(!Number.isInteger(v))fail(s+' must be an integer');};
  const list=(v,s)=>{if(!Array.isArray(v))fail(s+' must be an array');};
  const ids=(items,s)=>{list(items,s);const seen=new Set();for(const a of items){if(typeof a.id!=='string'||!a.id||seen.has(a.id))fail(s+' requires unique nonempty IDs');seen.add(a.id);}return seen;};
  if(p?.schema_version!==1)fail('schema_version must be 1');
  if(p.metadata!=null){if(typeof p.metadata!=='object'||Array.isArray(p.metadata))fail('metadata must be an object');if(p.metadata.unresolved!=null&&(!Array.isArray(p.metadata.unresolved)||p.metadata.unresolved.some(v=>typeof v!=='string')))fail('metadata.unresolved must be an array of strings');}
  integer(p.start_year,'start_year');integer(p.horizon_years,'horizon_years',1,100);num(p.reserve_real,'reserve_real',0);
  integer(p.comparison_stop_year,'comparison_stop_year',p.start_year,p.start_year+p.horizon_years);
  try{new Intl.NumberFormat('en-US',{style:'currency',currency:p.currency});}catch{fail('currency must be a valid currency code');}
  const adults=ids(p.adults,'adults');if(!adults.size)fail('At least one adult is required');for(const a of p.adults)integer(a.age_at_start,'adult age_at_start',0,120);
  const accounts=ids(p.accounts,'accounts');const accountMap=new Map(p.accounts.map(a=>[a.id,a]));
  for(const a of p.accounts){num(a.balance,a.id+' balance',0);num(a.unavailable,a.id+' unavailable',0,a.balance);integer(a.available_year,a.id+' available_year');if(!['cash','brokerage','traditional','roth','education','other'].includes(a.type))fail('Invalid account type for '+a.id);if(a.duplicate_of!=null&&(!accounts.has(a.duplicate_of)||a.duplicate_of===a.id))fail('Invalid duplicate_of for '+a.id);const seen=new Set([a.id]);let cur=a;while(cur.duplicate_of){if(seen.has(cur.duplicate_of))fail('Circular account duplicate');seen.add(cur.duplicate_of);cur=accountMap.get(cur.duplicate_of);}}
  ids(p.incomes,'incomes');for(const a of p.incomes){if(!adults.has(a.adult_id))fail('Unknown income adult_id');num(a.gross_annual,a.id+' gross_annual',0);num(a.growth_rate,a.id+' growth_rate',-.99,2);integer(a.start_year,a.id+' start_year');integer(a.stop_year,a.id+' stop_year',a.start_year);num(a.pretax_annual,a.id+' pretax_annual',0);num(a.benefits_annual,a.id+' benefits_annual',0);if(typeof a.optimize_stop!=='boolean')fail('optimize_stop must be boolean');}
  list(p.other_income,'other_income');for(const a of p.other_income){num(a.annual,'other income annual',0);num(a.growth_rate,'other income growth_rate',-.99,2);integer(a.start_year,'other income start_year');integer(a.end_year,'other income end_year',a.start_year);}
  num(p.spending?.inflation,'spending inflation',-.5,1);list(p.spending.phases,'spending phases');
  if(!p.spending.phases.length||p.spending.phases[0].start_year>p.start_year)fail('First spending phase must cover start_year');
  let last=-Infinity;for(const a of p.spending.phases){integer(a.start_year,'phase start_year');if(a.start_year<=last)fail('Spending phases must have distinct ascending start years');last=a.start_year;num(a.monthly,'phase monthly',0);num(a.healthcare_extra_annual,'healthcare_extra_annual',0);if(typeof a.includes_housing!=='boolean')fail('includes_housing must be boolean');if(a.includes_housing&&a.monthly<p.home.mortgage_monthly)fail('Housing-inclusive spending cannot be less than the mortgage-only payment');}
  for(const k of ['value','debt','mortgage_monthly','nonmortgage_monthly'])num(p.home?.[k],'home '+k,0);integer(p.home.mortgage_end_year,'mortgage_end_year');
  const funds=ids(p.college_funds,'college_funds');const fundAccounts=new Set();for(const f of p.college_funds){num(f.balance,'college fund balance',0);num(f.growth_rate,'college fund growth_rate',-.99,2);if(f.account_id!=null){const a=accountMap.get(f.account_id);if(!a||a.type!=='education'||a.duplicate_of||a.available_year>p.start_year||fundAccounts.has(f.account_id))fail('College fund must link one distinct currently available education account');fundAccounts.add(f.account_id);}}
  integer(p.college?.price_year,'college price_year');num(p.college.inflation,'college inflation',-.5,1);if(typeof p.college.credit_funds!=='boolean')fail('credit_funds must be boolean');if(!p.college.plans||typeof p.college.plans!=='object')fail('College plans required');
  for(const [name,a]of Object.entries(p.college.plans))for(const k of ['tuition','room_board','other'])num(a[k],name+' '+k,0);
  ids(p.children,'children');for(const a of p.children){integer(a.age_at_start,'child age',0,100);integer(a.college_start_year,'college_start_year');integer(a.years,'college years',1,10);if(!Object.hasOwn(p.college.plans,a.plan))fail('Unknown college plan');if(a.fund_id!=null&&!funds.has(a.fund_id))fail('Unknown college fund');}
  num(p.tax?.withdrawal_effective_rate,'withdrawal_effective_rate',0,.95);const wage=p.tax.salary;
  if(wage?.mode==='effective')num(wage.total_effective_rate,'total_effective_rate',0,.95);
  else if(wage?.mode==='progressive'){
    num(wage.index_rate,'tax index_rate',-.5,1);
    for(const jurisdiction of ['national','state']){const a=wage[jurisdiction];num(a?.deduction,jurisdiction+' deduction',0);list(a.brackets,jurisdiction+' brackets');if(!a.brackets.length)fail('Empty brackets');let bound=0;for(let i=0;i<a.brackets.length;i++){const b=a.brackets[i];num(b.rate,'bracket rate',0,1);if(b.up_to===null){if(i!==a.brackets.length-1)fail('Open bracket must be last');}else{num(b.up_to,'bracket threshold',bound+Number.EPSILON);bound=b.up_to;}}if(a.brackets.at(-1).up_to!==null)fail('Last bracket requires up_to:null');for(const b of a.surtaxes??[]){num(b.threshold,'surtax threshold',0);num(b.rate,'surtax rate',0,1);}}
    list(wage.payroll,'payroll');for(const a of wage.payroll){num(a.rate,'payroll rate',0,1);num(a.threshold,'payroll threshold',0);if(a.cap!=null)num(a.cap,'payroll cap',a.threshold);if(!['per_income','household'].includes(a.scope))fail('Invalid payroll scope');if(typeof a.indexed!=='boolean')fail('Payroll indexed must be boolean');}
  }else fail('salary tax mode must be effective or progressive');
  ids(p.scenarios,'scenarios');if(!p.scenarios.length)fail('At least one scenario required');for(const s of p.scenarios){if(typeof s.label!=='string')fail('Scenario label required');num(s.long_run_return,'long_run_return',-.99,2);list(s.returns,'scenario returns');for(const r of s.returns)num(r,'scenario return',-.99,2);if(typeof s.reverse_returns!=='boolean')fail('reverse_returns must be boolean');if(s.inflation!=null)num(s.inflation,'scenario inflation',-.5,1);for(const r of s.inflations??[])num(r,'scenario inflation',-.5,1);}
  list(p.events,'events');for(const e of p.events){integer(e.year,'event year');num(e.amount,'event amount',0);if(!['inflow','outflow'].includes(e.kind))fail('Event kind must be inflow or outflow');}
  return p;
}
export function initialCapital(p){return p.accounts.filter(a=>!a.duplicate_of&&a.type!=='education'&&a.available_year<=p.start_year).reduce((n,a)=>n+a.balance-a.unavailable,0);}
export function returnSeries(p,s){const values=Array.from({length:p.horizon_years},(_,t)=>s.returns[t]??s.long_run_return);return s.reverse_returns?values.reverse():values;}
export function bracketTax(taxable,schedule,scale){let total=0,lower=0;for(const b of schedule.brackets){const upper=b.up_to===null?Infinity:b.up_to*scale;total+=Math.max(0,Math.min(taxable,upper)-lower)*b.rate;lower=upper;}for(const s of schedule.surtaxes??[])total+=Math.max(0,taxable-s.threshold*(s.indexed?scale:1))*s.rate;return total;}
export function salaryNet(p,year,stopOverride=null){
  const t=year-p.start_year;
  const records=p.incomes.map(a=>{const stop=a.optimize_stop&&stopOverride!==null?stopOverride:a.stop_year;const gross=year>=a.start_year&&year<stop?a.gross_annual*(1+a.growth_rate)**t:0;return{gross,pretax:Math.min(gross,a.pretax_annual*(1+a.growth_rate)**t),benefits:gross?a.benefits_annual*(1+a.growth_rate)**t:0};});
  const sum=key=>records.reduce((n,a)=>n+a[key],0),gross=sum('gross'),pretax=sum('pretax'),benefits=sum('benefits'),tax=p.tax.salary;let national=0,state=0,payroll=0,effective=0;
  if(tax.mode==='effective')effective=Math.max(0,gross-pretax)*tax.total_effective_rate;
  else{const scale=(1+tax.index_rate)**t;national=bracketTax(Math.max(0,gross-pretax-tax.national.deduction*scale),tax.national,scale);state=bracketTax(Math.max(0,gross-pretax-tax.state.deduction*scale),tax.state,scale);for(const rule of tax.payroll){const k=rule.indexed?scale:1,threshold=rule.threshold*k,cap=rule.cap==null?Infinity:rule.cap*k;const charge=v=>Math.max(0,Math.min(v,cap)-threshold)*rule.rate;payroll+=rule.scope==='household'?charge(gross):records.reduce((n,a)=>n+charge(a.gross),0);}}
  return{gross,pretax,benefits,national,state,payroll,effective,net:Math.max(0,gross-pretax-benefits-national-state-payroll-effective)};
}
export function project(p,scenario,stopOverride=null,constantReturn=null){
  const s=typeof scenario==='string'?p.scenarios.find(s=>s.id===scenario):scenario;if(!s)throw Error('Unknown scenario');
  const returns=constantReturn===null?returnSeries(p,s):Array(p.horizon_years).fill(constantReturn);
  const fundBalances=Object.fromEntries(p.college_funds.map(f=>{const account=f.account_id?p.accounts.find(a=>a.id===f.account_id):null;return[f.id,account?account.balance-account.unavailable:f.balance];}));
  let balance=initialCapital(p),price=1;const rows=[];
  for(let t=0;t<p.horizon_years;t++){
    const year=p.start_year+t,inf=constantReturn===null?(s.inflations?.[t]??s.inflation??p.spending.inflation):p.spending.inflation;if(t)price*=1+inf;
    const released=p.accounts.filter(a=>!a.duplicate_of&&a.type!=='education'&&a.available_year===year&&year>p.start_year).reduce((n,a)=>n+a.balance-a.unavailable,0);balance+=released;const opening=balance;
    const phase=p.spending.phases.filter(a=>a.start_year<=year).at(-1),mortgage=p.home.mortgage_monthly*12;
    const living=(phase.monthly*12+(phase.includes_housing?-mortgage:p.home.nonmortgage_monthly*12)+phase.healthcare_extra_annual)*price+(year<=p.home.mortgage_end_year?mortgage:0);
    let college=0,enrolled=0;const groupNeeds=new Map();for(const child of p.children){if(year<child.college_start_year||year>=child.college_start_year+child.years)continue;enrolled++;const plan=p.college.plans[child.plan],cost=(plan.tuition+plan.room_board+plan.other)*(1+p.college.inflation)**(year-p.college.price_year);college+=cost;if(child.fund_id)groupNeeds.set(child.fund_id,(groupNeeds.get(child.fund_id)??0)+cost);}
    let fundUsed=0;if(p.college.credit_funds)for(const [id,need]of groupNeeds){const used=Math.min(need,fundBalances[id]);fundBalances[id]-=used;fundUsed+=used;}
    for(const f of p.college_funds)fundBalances[f.id]*=1+f.growth_rate;
    const wages=salaryNet(p,year,stopOverride),other=p.other_income.filter(a=>year>=a.start_year&&year<=a.end_year).reduce((n,a)=>n+a.annual*(1+a.growth_rate)**(year-a.start_year),0);
    const eventTotal=kind=>p.events.filter(a=>a.year===year&&a.kind===kind).reduce((n,a)=>n+a.amount,0),eventIn=eventTotal('inflow'),eventOut=eventTotal('outflow');
    const available=wages.net+other+eventIn,collegeNeed=college-fundUsed,gap=living+collegeNeed+eventOut-available,denom=1-p.tax.withdrawal_effective_rate;
    const livingNeed=Math.max(0,living-available),surplus=Math.max(0,available-living),collegeGap=Math.max(0,collegeNeed-surplus),eventGap=Math.max(0,eventOut-Math.max(0,surplus-collegeNeed));
    const drawNeeded=Math.max(0,gap)/denom,drawFunded=Math.min(balance,drawNeeded),shortfall=(drawNeeded-drawFunded)*denom,contribution=Math.max(0,-gap);
    balance=(balance-drawFunded+contribution)*(1+returns[t]);
    const row={year,ages:Object.fromEntries(p.adults.map(a=>[a.id,a.age_at_start+t])),opening,released,return:returns[t],inflation:inf,price,living,college,enrolled,fund_used:fundUsed,gross_salary:wages.gross,net_salary:wages.net,salary_national_tax:wages.national,salary_state_tax:wages.state,salary_payroll_tax:wages.payroll,salary_effective_tax:wages.effective,excluded_pretax_saving:wages.pretax,other_income:other,event_in:eventIn,event_out:eventOut,living_gross_monthly:livingNeed/denom/12,college_gross_lump:collegeGap/denom,event_gross_draw:eventGap/denom,draw_needed:drawNeeded,draw_funded:drawFunded,withdrawal_tax_needed:drawNeeded*p.tax.withdrawal_effective_rate,withdrawal_tax_paid:drawFunded*p.tax.withdrawal_effective_rate,contribution,shortfall,ending:balance,ending_real:balance/price,education_funds:Object.values(fundBalances).reduce((n,a)=>n+a,0)};
    if(Object.values(row).some(v=>typeof v==='number'&&!Number.isFinite(v)))throw Error('Non-finite forecast in '+year+'; check values and rates');rows.push(row);
  }
  return rows;
}
export function earliestStop(p,s){if(!p.incomes.some(a=>a.optimize_stop))return null;for(let y=p.start_year;y<p.start_year+p.horizon_years;y++){const a=project(p,s,y);if(a.every(r=>r.shortfall<.01)&&a.at(-1).ending_real+.01>=p.reserve_real)return y;}return null;}
export function requiredReturn(p,target,stop=p.comparison_stop_year){
  const ok=rate=>{const a=project(p,p.scenarios[0],stop,rate);return a.every(r=>r.shortfall<.01)&&a.at(-1).ending_real+.01>=target;};
  if(!ok(.30))return null;if(ok(-.20))return-.20;let lo=-.20,hi=.30;for(let i=0;i<44;i++){const mid=(lo+hi)/2;if(ok(mid))hi=mid;else lo=mid;}return hi;
}
export function summarize(p){
  validate(p);const capital=initialCapital(p),lastCollege=p.children.length?Math.max(...p.children.map(c=>c.college_start_year+c.years-1)):null;
  const cases=p.scenarios.map(s=>{const rows=project(p,s,p.comparison_stop_year),first=rows.find(r=>r.shortfall>.01),after=rows.find(r=>r.year===lastCollege),ending=rows.at(-1);return{id:s.id,label:s.label,earliest_stop_year:earliestStop(p,s),after_college_year:lastCollege,after_college_nominal:after?.ending??null,ending_nominal:ending.ending,ending_real:ending.ending_real,first_unfunded_year:first?.year??null,first_unfunded_ages:first?.ages??null,total_unfunded:rows.reduce((n,r)=>n+r.shortfall,0),meets_reserve:!first&&ending.ending_real+.01>=p.reserve_real,rows};});
  return{schema_version:1,currency:p.currency,base_year:p.start_year,end_year:p.start_year+p.horizon_years-1,end_ages:Object.fromEntries(p.adults.map(a=>[a.id,a.age_at_start+p.horizon_years-1])),comparison_stop_year:p.comparison_stop_year,initial_spendable:capital,home_equity_excluded:p.home.value-p.home.debt,reserve_real:p.reserve_real,cases,escape_velocity:{fund_horizon:requiredReturn(p,0),retain_reserve:requiredReturn(p,p.reserve_real),preserve_initial:requiredReturn(p,capital),minimum_tested_return:-.20,maximum_tested_return:.30},limitations:['Deterministic scenarios, not probabilities','Investment withdrawal taxes use a provisional combined effective allowance','Aggregate accessible assets; no tax lots, RMDs or withdrawal-access exceptions','Pretax contributions are excluded retirement savings; not added to accessible capital','Annual beginning-of-year cash-flow convention','Home equity excluded unless explicit net cash event']};
}
