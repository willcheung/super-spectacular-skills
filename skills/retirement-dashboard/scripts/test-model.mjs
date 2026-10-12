import assert from 'node:assert/strict';import fs from 'node:fs';import{validate,project,initialCapital,returnSeries,salaryNet,earliestStop,requiredReturn,summarize}from'./model.mjs';
const fixture=JSON.parse(fs.readFileSync(new URL('../assets/example.json',import.meta.url),'utf8')),copy=()=>structuredClone(fixture),near=(a,b)=>assert.ok(Math.abs(a-b)<.02,`${a} != ${b}`);
validate(fixture);const summary=summarize(fixture);assert.equal(summary.cases.length,6);assert.equal(summary.end_ages.adult_a,85);
// Independent future-value formula, including all prescribed recession sequences.
for(const scenario of fixture.scenarios){const rows=project(fixture,scenario,fixture.comparison_stop_year),returns=returnSeries(fixture,scenario),product=(from,to)=>returns.slice(from,to+1).reduce((a,r)=>a*(1+r),1);let raw=initialCapital(fixture)*product(0,rows.length-1);for(let i=0;i<rows.length;i++){const r=rows[i];raw+=(r.contribution-r.draw_needed)*product(i,rows.length-1);}near(rows.at(-1).ending,Math.max(0,raw));for(const r of rows)near(r.living_gross_monthly*12+r.college_gross_lump+r.event_gross_draw,r.draw_needed);}
// Salary stop for the other adult never follows the optimized earner.
const wages=salaryNet(fixture,2027,2032);near(wages.gross,180000);assert.equal(salaryNet(fixture,2032,2032).gross,0);
// Shared education funds are paid once and a no-funding stress preserves the record.
let p=copy();p.children[1].fund_id='education_a';p.college_funds[0].balance=100000;const shared=project(p,'base',2032);near(shared.reduce((n,r)=>n+r.fund_used,0),100000);p.college.credit_funds=false;assert.equal(project(p,'base',2032).reduce((n,r)=>n+r.fund_used,0),0);assert.equal(p.college_funds[0].balance,100000);
// Arbitrary valid IDs cannot accidentally refer to inherited Object properties.
for(const id of ['__proto__','constructor','toString']){p=copy();p.college_funds[0].id=id;p.children[0].fund_id=id;near(project(p,'base',2032).reduce((n,r)=>n+r.fund_used,0),40000);}p=copy();p.children[0].plan='toString';assert.throws(()=>validate(p));
// Duplicate snapshots and education accounts do not increase spendable assets.
p=copy();p.accounts.push({...p.accounts[0],id:'duplicate_a',duplicate_of:p.accounts[0].id});near(initialCapital(p),2600000);p.accounts.push({id:'education_link',type:'education',balance:55000,unavailable:0,available_year:2027,duplicate_of:null});p.college_funds[0].account_id='education_link';near(initialCapital(p),2600000);near(project(p,'base',2032).reduce((n,r)=>n+r.fund_used,0),55000);
// Mortgage payoff removes only the nominal mortgage portion, not nonmortgage housing.
p=copy();p.spending.inflation=0;p.home.mortgage_end_year=2027;const mortgage=project(p,'base',2032);near(mortgage[0].living-mortgage[1].living,1600*12);
// Reversing a complete sequence uses the same annual returns, including recovery.
const early=returnSeries(fixture,fixture.scenarios.find(s=>s.id==='early')),late=returnSeries(fixture,fixture.scenarios.find(s=>s.id==='late'));assert.deepEqual(late,[...early].reverse());
// Known no-growth depletion arithmetic and withdrawal gross-up.
p=copy();p.horizon_years=3;p.reserve_real=0;p.comparison_stop_year=2027;p.accounts=[{id:'cash',type:'cash',balance:100,unavailable:0,available_year:2027,duplicate_of:null}];p.incomes=[];p.children=[];p.college_funds=[];p.home.mortgage_monthly=0;p.spending={inflation:0,phases:[{start_year:2027,monthly:5,includes_housing:true,healthcare_extra_annual:0}]};p.tax.withdrawal_effective_rate=.25;p.scenarios=[{id:'zero',label:'Zero',returns:[],reverse_returns:false,long_run_return:0}];const depleted=project(p,'zero');near(depleted[0].draw_needed,80);near(depleted[0].ending,20);near(depleted[1].draw_funded,20);near(depleted[1].shortfall,45);assert.equal(summarize(p).cases[0].first_unfunded_year,2028);assert.equal(earliestStop(p,p.scenarios[0]),null);
// A delayed accessible account enters once, with no invented pre-access gains.
p.accounts.push({id:'later',type:'brokerage',balance:30,unavailable:0,available_year:2028,duplicate_of:null});near(project(p,'zero')[1].released,30);near(project(p,'zero')[2].released,0);
// Progressive joint wages with separate payroll caps; synthetic schedules only.
p=copy();p.tax.salary={mode:'progressive',index_rate:0,national:{deduction:10000,brackets:[{up_to:100000,rate:.1},{up_to:null,rate:.2}]},state:{deduction:0,brackets:[{up_to:null,rate:.05}]},payroll:[{rate:.1,cap:50000,threshold:0,scope:'per_income',indexed:false}]};p.incomes[1].stop_year=2032;const progressive=salaryNet(p,2027,2032);near(progressive.national,42000);near(progressive.state,13500);near(progressive.payroll,10000);near(progressive.net,204500);
// Solver actually funds the selected reserve at the returned threshold.
p=copy();const rate=requiredReturn(p,p.reserve_real);assert.notEqual(rate,null);const path=project(p,p.scenarios[0],p.comparison_stop_year,rate);assert.ok(path.every(r=>r.shortfall<.01));near(path.at(-1).ending_real,p.reserve_real);
// A major cash event and invalid/missing inputs stay explicit.
p=copy();p.events=[{year:2027,kind:'outflow',amount:60000}];const event=project(p,'base',2032)[0];near(event.living_gross_monthly*12+event.college_gross_lump+event.event_gross_draw,event.draw_needed);
p=copy();p.tax.withdrawal_effective_rate=1;assert.throws(()=>validate(p));p=copy();delete p.spending.phases[0].monthly;assert.throws(()=>validate(p));p=copy();p.accounts[0].duplicate_of=p.accounts[0].id;assert.throws(()=>validate(p));p=copy();p.metadata.unresolved='unknown';assert.throws(()=>validate(p));p=copy();p.accounts[0].balance=1e308;assert.throws(()=>summarize(p));
console.log('Passed: independent balances, income timing, shared funds, overlap, mortgage payoff, sequence reversal, depletion, gross-up, progressive wages, cash events and solver.');
