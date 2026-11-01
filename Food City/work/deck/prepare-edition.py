from pathlib import Path
s=Path('work/deck/build.mjs').read_text(encoding='utf-8-sig')
s=s.replace('Transportation barrier within the proposed five-mile zone','Within radius or an employee-added route')
s=s.replace('Five-mile zone, two windows daily, five service days per week','Five-mile radius plus employee-added rural map routes')
s=s.replace('Offered assignments allow employee acceptance or release','Employees add rural map routes and choose offered deliveries')
s=s.replace("'Proposed gross spend cap: $38,425'","'Short-route reference gross spend cap: $38,425'")
s=s.replace("families:['Arial']","families:['Aptos']").replace('verifyArtifactToolImport:true','materializeLiteralChartWorkbooks:true,verifyArtifactToolImport:true')
s=s.replace("outputs/Food-City-Community-Connect.pptx","outputs/Food-City-Community-Connect-Illustrated.pptx").replace("work/deck/candidate.pptx","work/deck/final-illustrated-candidate.pptx").replace("work/deck/validation.json","work/deck/final-illustrated-validation.json")
insert='''slide('Rural delivery route exceptions','The radius applies until an employee adds a corridor to the map',[
 'Employees can add homeward routes, including mountain communities',
 'Outside-radius customers select a listed employee-added route',
 'The route creator chooses which paid deliveries to accept',
 '18-mile, 45-minute scenario: $26,413 operating gap over eight weeks'
], 'Default radius five miles. Employee-added corridors create exceptions. Adding a route does not commit an employee to every order. Safe access, paid duty, insurance and funding still apply. Demo map is synthetic and entered delivery miles are a radius proxy. Production requires address-to-route validation and separate straight-line and road-mile calculations. At 18 miles and 45 delivery minutes, 800 completions, variable expense $35.7667/order, operating expense $30,373.33, receipts $3,960, gap $26,413.33. Including $15,000 setup and 15% contingency gives $52,179.33 gross authorization. Short-route budget is only a reference until actual rural costs are measured.');
for(const [idx,file] of [[0,'porch.png'],[4,'family.png']]){
 const sl=p.slides.items[idx];
 for(const sh of sl.shapes.items){if(sh.position.top>=180 && sh.position.top<650)sh.position={...sh.position,width:570};}
 const b=await fs.readFile(path.join(root,'outputs/community-connect/assets',file));
 sl.images.add({blob:b.buffer.slice(b.byteOffset,b.byteOffset+b.byteLength),contentType:'image/png',alt:'AI-generated illustrative fictional grocery customers',fit:'cover',position:{left:690,top:280,width:520,height:350}});
 text(sl,'AI-generated illustration. Fictional people, no endorsement.',690,638,520,26,13,'#52617B');
 sl.speakerNotes.text+=' Illustrative image generated using the built-in image-generation tool. Fictional people, not actual Food City customers or endorsement.';
}
'''
s=s.replace("await fs.mkdir(path.join(root,'work/deck/render')",insert+"await fs.mkdir(path.join(root,'work/deck/render')")
s=s.replace("for(let i=0;i<p.slides.items.length;i++){let b=", "for(const i of [0,3,4,6,9,14]){let b=")
s=s.replace('work/deck/render/${i+1}.png','work/deck/render/revised-${i+1}.png')
Path('work/deck/brochure-edition.mjs').write_text(s,encoding='utf-8')
