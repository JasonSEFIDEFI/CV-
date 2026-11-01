import fs from 'node:fs/promises';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {Presentation,PresentationFile} from 'file:///C:/Users/jason/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/@oai/artifact-tool/dist/artifact_tool.mjs';
const root=process.cwd(), skill='C:/Users/jason/.codex/plugins/cache/openai-primary-runtime/presentations/26.1026.10807/skills/presentations';
const p=Presentation.create({slideSize:{width:1280,height:720}});
const navy='#123269',red='#C92032';
function text(s,t,x,y,w,h,size=30,color=navy,bold=false){let a=s.shapes.add({geometry:'textbox',position:{left:x,top:y,width:w,height:h},fill:'none',line:{fill:'none',width:0}});a.text=t;a.text.style={fontFamily:'Arial',fontSize:size,color,bold};return a;}
function slide(title,subtitle,lines,notes=''){let s=p.slides.add();s.background.fill='#FFFFFF';text(s,title,64,55,1152,130,48,navy,true);if(subtitle)text(s,subtitle,68,185,1140,80,27,red,true);lines.forEach((v,i)=>text(s,v,68,290+i*88,1135,76,29));text(s,`Independent unofficial proposal · Synthetic assumptions · ${p.slides.items.length}`,68,675,1130,26,16,'#68728A');s.speakerNotes.text=notes||'Independent unofficial proposal. All operating figures are planning assumptions. No Food City system integration, affiliation or committed sponsorship.';return s;}
slide('Food City\nCommunity Connect','A proposed neighborhood delivery and assistance platform',[
 'Customer, employee and management consoles',
 'One-store pilot proposal · October 31, 2026'
]);
slide('The community service proposition','Affordable access requires an explicit funding commitment',[
 'Paid grocery delivery at a proposed $4.95 fee',
 'Delivery fee waivers for approved transportation barriers',
 'Groceries remain customer funded',
 'One service workflow with private eligibility review'
]);
slide('One platform, three consoles','Working local prototype with persistent synthetic records',[
 'Customers build baskets, request assistance and track orders',
 'Employees choose paid assignments and record delivery outcomes',
 'Managers prepare orders, dispatch and review assistance',
 'Finance reviews a separate supplementary fuel reward ledger'
]);
slide('Order fulfillment','Managers control readiness. Employees choose assignments.',[
 'Placed, picking and ready establish store preparation status',
 'Employees add rural map routes and choose offered deliveries',
 'Departure starts the delivery leg',
 'Completion or failure closes the attempt and records time/miles'
]);
slide('Assistance policy','A proposed delivery fee benefit with a controlled reserve',[
 'Within radius or an employee-added route',
 'Manager decision with a reason and 30-day approval',
 'Up to four fee waivers, subject to remaining funding',
 'Early cancellations restore the reserved fee and allowance'
]);
slide('Employee participation','Voluntary acceptance of paid work',[
 'Delivery time is paid and tracked for labor review',
 'Mileage reimbursement is separate from wages',
 '$2 fuel reward per completed delivery, additional to compensation',
 'Manager approval and biweekly simulated reward issuance'
], 'U.S. DOL: employees may not volunteer services to for-profit private-sector employers. https://webapps.dol.gov/elaws/whd/FLSA/docs/volunteers.asp . Hours worked: https://www.dol.gov/agencies/whd/fact-sheets/22-flsa-hours-worked . HR/counsel must approve the labor model, overtime, reward taxation and regular-rate treatment. No real fuel vouchers or Gas N Go integration exist in this demo.');
slide('One-store service pilot','Four readiness weeks followed by eight service weeks',[
 'Five-mile radius plus employee-added rural map routes',
 '800 completions assumed, including 240 assisted deliveries',
 '6–8 interested employees, paid training and approved vehicles',
 'Initial 10/day cap, rising to 20/day only after service checks'
], 'Planning assumptions only. The 800-order base requires recovering ramp volume within approved capacity. At 20/day assume 10 delivery labor hours, 3.33 picking hours and 2 coordination hours. Store coverage and peak availability require validation.');
slide('Operating economics','The proposed fee does not cover delivery cost',[
 '$20.82 variable expense per completed order',
 '$18,413 operating expense for eight service weeks',
 '$2,772 customer fees plus $1,188 assumed sponsor transfers',
 '$14,453 operating funding gap after assumed sponsor transfers'
], 'Assumptions: 800 orders, 70% paid at $4.95, 30% assisted. Per completion: 30 delivery minutes and 10 picking minutes at $22 loaded/hour, 4.5 miles at $0.70/mile, $2 supplementary fuel reward, $1 supplies/payment placeholder. Exact variable cost $20.8166667. Coordination 80 hours at $22. Merchandise revenue/cost and tax excluded. Sponsor funds are uncommitted. No grocery margin or retention uplift assumed.');
let c=slide('Delivery time drives the funding gap','Eight-week operating gap after $4.95 receipts per completion',[], 'Scenario changes delivery minutes only. 800 completions. Picking 10 minutes, loaded labor $22/hour, mileage 4.5 × $0.70, $2 fuel reward, $1 other. Coordination $1,760. Receipts $3,960 include assumed sponsor transfers. No setup/contingency in chart. All values are assumptions.');
c.charts.add('bar',{position:{left:95,top:295,width:1080,height:325},categories:['20 min delivery','30 min delivery','40 min delivery'],series:[{name:'Operating gap ($)',values:[11520,14453.33,17386.67],fill:red}],hasLegend:false,dataLabels:{showValue:true,position:'outEnd'},yAxis:{numberFormat:'$#,##0'}});
slide('Pilot authorization request','Short-route reference gross spend cap: $38,425',[
 '$18,413 operations plus $15,000 readiness and setup',
 '$5,012 contingency, calculated at 15% of both',
 '$35,653 net funding after projected customer delivery fees',
 '$34,465 store funding if a sponsor commits $1,188'
], 'Rounded to dollars. Exact gross cap $38,425.33 = (18,413.3333 + 15,000) × 1.15. Net after customer fees $35,653.33. Store funding after assumed external sponsor $34,465.33. If assistance funds come from the store, they are an internal transfer and do not reduce its total funding requirement. Readiness allowance is a placeholder estimate, not a vendor quote.');
slide('Pilot measurement','Weekly review ties service quality to actual cost',[
 'At least 95% on time and 97% completion, with cohort counts',
 'Variable cost target of $21 or less, coordination reported separately',
 '40–60 assisted households, decisions within two business days',
 '100% ledger reconciliation and no unresolved serious incidents'
], 'Targets are hypotheses. Record promised windows, actual timestamps, failures, cancellations and denominator definitions. Prototype has partial demo metrics, not full pilot instrumentation. Track survey response rate, employee choice, overtime and store impact. Require at least 100 completions before interpreting on-time performance for scale.');
slide('Technical architecture','Local demonstration today, authorized adapters only in the future',[
 'Browser consoles call a role-checked Python JSON service',
 'SQLite stores orders, approvals, fund reservations and rewards',
 'Production needs identity, durable services and reconciliation',
 'No inventory, payment, payroll or fuel system connection exists'
]);
slide('Launch gates and risk controls','A functional demo does not authorize a live delivery service',[
 'HR and counsel approve pay, employee choice and reward treatment',
 'Insurer and operations approve vehicles and driver coverage',
 'Food-safety lead approves transport and failed-handoff procedures',
 'Security, finance and sponsor approve data controls and funding'
], 'Food safety source: FDA, https://www.fda.gov/food/hfp-constituent-updates/fda-highlights-best-practices-food-safety-online-delivery-services . Establish packaging, temperature and transport procedures. Pause for serious safety events, insurance lapse, privacy incident or unexplained fund mismatch. Exclude age-restricted items in pilot.');
slide('Decision and demonstration','Approve readiness work before approving live service',[
 'Review the local prototype using four fictional demo accounts',
 'Select a store owner and validate staffing and insurance',
 'Confirm the funding gap and identify a committed assistance fund',
 'Release live pilot funds only after readiness gates pass'
], 'Demo: customer places order and requests assistance, manager reviews and dispatches, employee accepts and completes, manager reviews reward and scorecard. Detailed architecture, assumptions, sensitivity, risks and pilot plan accompany the deck. This is an independent unofficial proposal with no Food City affiliation or endorsement.');
slide('Rural delivery route exceptions','The radius applies until an employee adds a corridor to the map',[
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
await fs.mkdir(path.join(root,'work/deck/render'),{recursive:true});
for(const i of [0,3,4,6,9,14]){let b=await p.export({slide:p.slides.items[i],format:'png',scale:1});await fs.writeFile(path.join(root,`work/deck/render/revised-${i+1}.png`),new Uint8Array(await b.arrayBuffer()));}
await (await PresentationFile.exportPptx(p)).save(path.join(root,'work/deck/final-illustrated-candidate.pptx'));
const {finalizePresentation}=await import(pathToFileURL(path.join(skill,'container_tools/artifact_tool_utils.mjs')).href);
console.log(await finalizePresentation({workspaceDir:root,candidatePath:path.join(root,'work/deck/final-illustrated-candidate.pptx'),finalPath:path.join(root,'outputs/Food-City-Community-Connect-Illustrated.pptx'),pythonExecutable:'C:/Users/jason/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe',integrityValidatorPath:path.join(skill,'container_tools/inspect_presentation_package_integrity.py'),layoutValidatorPath:path.join(skill,'container_tools/inspect_presentation_layout_geometry.py'),layoutArgs:['--expected-slide-size-emu','12192000,6858000','--validate-heading-fit'],fontPolicy:{basis:'design',families:['Aptos']},requiredNativeChartOwnerSlides:[9],materializeLiteralChartWorkbooks:true,verifyArtifactToolImport:true,receiptPath:path.join(root,'work/deck/final-illustrated-validation.json')}));
