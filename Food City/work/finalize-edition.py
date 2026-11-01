from pathlib import Path
p=Path('work/deck/brochure-edition.mjs');s=p.read_text(encoding='utf-8-sig')
s=s.replace('outputs/Food-City-Community-Connect-Illustrated.pptx','outputs/Food-City-Community-Connect-Final.pptx').replace('work/deck/final-illustrated-candidate.pptx','work/deck/final-manager-candidate.pptx').replace('work/deck/final-illustrated-validation.json','work/deck/final-manager-validation.json')
s=s.replace('Employees choose paid assignments and record delivery outcomes','Managers release staff; employees choose paid deliveries')
s=s.replace('The route creator chooses which paid deliveries to accept','Manager release comes first, then the route creator accepts')
insert='''slide('Store manager staffing authority','Delivery availability requires an explicit manager decision',[
 'The store manager decides whether an employee can be spared',
 'Manager release enables acceptance and departure',
 'Employees choose assignments after release, with no pressure',
 'Recall blocks new trips while allowing a current trip to finish safely'
], 'Implemented server-side in the local prototype. Only management can change duty release. Both acceptance and departure check current release. Employee-added route coverage does not grant staffing permission. In-flight delivery completion remains possible after recall for safety. Production needs release expiry, schedule validation, paid hours and insurance checks.');
slide('Central drone hubs: long-term ambition','Abingdon is an illustrative hub location for feasibility review',[
 'Design fulfillment tasks to support future ground or drone carriers',
 'Evaluate payloads, safe delivery points and operating approvals',
 'Use a qualified flight operator with separate mission controls',
 'Keep ground fallback where drone delivery is unavailable'
], 'Vision: ultimately support eligible grocery deliveries by drone from central hubs. This is a design ambition, not demonstrated all-order capability. Abingdon is an example only, with no selected site or Food City agreement. No aircraft control exists in the prototype. Future hub, package, carrier assignment and drone mission entities preserve the customer order workflow. Drone economics are outside the employee pilot budget. FAA package delivery guidance: https://www.faa.gov/uas/advanced_operations/package_delivery_drone . Applicable approvals and current rules require operator and aviation-counsel review.');
'''
s=s.replace("for(const [idx,file]",insert+"for(const [idx,file]")
s=s.replace('for(const i of [0,3,4,6,9,14])','for(const i of [0,2,4,14,15,16])')
s=s.replace('work/deck/render/revised-${i+1}.png','work/deck/render/final-${i+1}.png')
Path('work/deck/final-edition.mjs').write_text(s,encoding='utf-8')
p=Path('work/format-plan.py');s=p.read_text(encoding='utf-8-sig');s=s.replace("body='\\n'.join(parts)","body='\\n'.join(parts)\nbody=body.replace('<h2>Executive concept</h2>','<figure style=\"margin:25px 0\"><img src=\"community-connect/assets/family.png\" alt=\"Illustrative happy grocery customers\" style=\"width:100%;max-height:360px;object-fit:cover\"><figcaption style=\"font-size:12px\">AI-generated illustration. Fictional people, not actual Food City customers. No endorsement implied.</figcaption></figure><h2>Executive concept</h2>')")
p.write_text(s,encoding='utf-8')
