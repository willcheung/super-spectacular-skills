import fs from 'node:fs/promises';import path from 'node:path';import {fileURLToPath}from'node:url';import{summarize}from'./model.mjs';
const [input,output]=process.argv.slice(2);if(!input||!output){console.error('Usage: node generate-dashboard.mjs inputs.json output-directory');process.exit(1);}
try{
 const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..'),p=JSON.parse(await fs.readFile(input,'utf8')),results=summarize(p),template=await fs.readFile(path.join(root,'assets/dashboard.html'),'utf8');
 const engine=(await fs.readFile(path.join(root,'scripts/model.mjs'),'utf8')).replace(/^export /gm,'');
 const slash=String.fromCharCode(92);const safe=value=>JSON.stringify(value).replaceAll('<',slash+'u003c').replaceAll(String.fromCharCode(0x2028),slash+'u2028').replaceAll(String.fromCharCode(0x2029),slash+'u2029');
 const html=template.replace('/* MODEL_ENGINE */',()=>engine).replace('/* MODEL_INPUT */',()=>safe(p));
 await fs.mkdir(output,{recursive:true});await fs.writeFile(path.join(output,'dashboard.html'),html);await fs.writeFile(path.join(output,'results.json'),JSON.stringify(results,null,2));
 for(const [index,c]of results.cases.entries()){const keys=Object.keys(c.rows[0]).filter(k=>k!=='ages');const escaped=v=>'"'+String(typeof v==='object'?JSON.stringify(v):v??'').replaceAll('"','""')+'"';const csv=[keys.join(','),...c.rows.map(r=>keys.map(k=>escaped(r[k])).join(','))].join(String.fromCharCode(10));const id=c.id.replace(/[^a-z0-9_-]/gi,'_');await fs.writeFile(path.join(output,'forecast-'+String(index+1).padStart(2,'0')+'-'+id+'.csv'),csv);}
 console.log('Generated editable dashboard, results and '+results.cases.length+' scenario CSVs.');
}catch(e){console.error(e.message);process.exit(1);}
