import fs from 'node:fs/promises';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {PresentationFile,FileBlob} from 'file:///C:/Users/jason/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/@oai/artifact-tool/dist/artifact_tool.mjs';
const root=process.cwd(),skill='C:/Users/jason/.codex/plugins/cache/openai-primary-runtime/presentations/26.1026.10807/skills/presentations';
const p=await PresentationFile.importPptx(await FileBlob.load(path.join(root,'outputs/Food-City-Community-Connect.pptx')));
for(const [idx,file] of [[0,'porch.png'],[4,'family.png']]){
 const s=p.slides.items[idx];
 for(const sh of s.shapes.items){
  if(sh.position.top>=180 && sh.position.top<650){sh.position={...sh.position,width:570};}
 }
 const b=await fs.readFile(path.join(root,'outputs/community-connect/assets',file));
 s.images.add({blob:b.buffer.slice(b.byteOffset,b.byteOffset+b.byteLength),contentType:'image/png',alt:'AI-generated illustrative fictional grocery customers',fit:'cover',position:{left:690,top:280,width:520,height:350}});
 const cap=s.shapes.add({geometry:'textbox',position:{left:690,top:637,width:520,height:30},fill:'none',line:{fill:'none',width:0}});cap.text='AI-generated illustration. Fictional people, no endorsement.';cap.text.style={fontSize:13,color:'#52617B'};
 s.speakerNotes.text+='\nImagery generated using built-in image generation for this independent proposal. Fictional people, not actual Food City customers or a customer testimonial. Red and blue are proposal design accents.';
 const png=await p.export({slide:s,format:'png',scale:1});await fs.writeFile(path.join(root,`work/deck/render/illustrated-${idx+1}.png`),new Uint8Array(await png.arrayBuffer()));
}
const candidatePath=path.join(root,'work/deck/illustrated-candidate.pptx');await (await PresentationFile.exportPptx(p)).save(candidatePath);
const {finalizePresentation}=await import(pathToFileURL(path.join(skill,'container_tools/artifact_tool_utils.mjs')).href);
const result=await finalizePresentation({workspaceDir:root,candidatePath,finalPath:path.join(root,'outputs/Food-City-Community-Connect-Illustrated.pptx'),pythonExecutable:'C:/Users/jason/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe',integrityValidatorPath:path.join(skill,'container_tools/inspect_presentation_package_integrity.py'),layoutValidatorPath:path.join(skill,'container_tools/inspect_presentation_layout_geometry.py'),layoutArgs:['--expected-slide-size-emu','12192000,6858000','--validate-heading-fit'],fontPolicy:{basis:'design',families:['Aptos']},requiredNativeChartOwnerSlides:[9],materializeLiteralChartWorkbooks:true,verifyArtifactToolImport:true,receiptPath:path.join(root,'work/deck/illustrated-validation.json')});console.log('Validated illustrated deck:',result.finalPath);
