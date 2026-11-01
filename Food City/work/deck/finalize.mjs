import path from 'node:path';
import {pathToFileURL} from 'node:url';
const root=process.cwd(),skill='C:/Users/jason/.codex/plugins/cache/openai-primary-runtime/presentations/26.1026.10807/skills/presentations';
const {finalizePresentation}=await import(pathToFileURL(path.join(skill,'container_tools/artifact_tool_utils.mjs')).href);
console.log(await finalizePresentation({workspaceDir:root,candidatePath:path.join(root,'work/deck/candidate.pptx'),finalPath:path.join(root,'outputs/Food-City-Community-Connect.pptx'),pythonExecutable:'C:/Users/jason/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe',integrityValidatorPath:path.join(skill,'container_tools/inspect_presentation_package_integrity.py'),layoutValidatorPath:path.join(skill,'container_tools/inspect_presentation_layout_geometry.py'),layoutArgs:['--expected-slide-size-emu','12192000,6858000','--validate-heading-fit'],fontPolicy:{basis:'design',families:['Aptos']},requiredNativeChartOwnerSlides:[9],materializeLiteralChartWorkbooks:true,verifyArtifactToolImport:true,receiptPath:path.join(root,'work/deck/validation.json')}));


