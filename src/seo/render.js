const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const [SC,OUT]=process.argv.slice(2);const b=await chromium.launch();
fs.writeFileSync(SC+'/seo/og-tmp.html',fs.readFileSync(SC+'/seo/og.html','utf8').replaceAll('SITE',OUT));
let p=await b.newPage({viewport:{width:1200,height:630}});await p.goto('file://'+SC+'/seo/og-tmp.html');await p.waitForTimeout(1500);
await p.screenshot({path:OUT+'/images/og-image.jpg',type:'jpeg',quality:85});
for (const [n,sz] of [['apple-touch-icon.png',180],['favicon-32.png',32],['icon-512.png',512]]){
 fs.writeFileSync(SC+'/seo/ic.html',`<body style="margin:0"><img src="file://${OUT}/brand/favicon.svg" style="width:${sz}px;height:${sz}px;display:block"></body>`);
 const q=await b.newPage({viewport:{width:sz,height:sz}});await q.goto('file://'+SC+'/seo/ic.html');await q.waitForTimeout(200);await q.screenshot({path:OUT+'/'+n,omitBackground:true});await q.close();}
await b.close()})();
