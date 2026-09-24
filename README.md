# Jason Duran Dutton

**Field engineering · Electrical integration and commissioning · Scientific software**

My professional foundation is hands-on electrical systems work: controls, sensor interfaces, commissioning, maintenance, fault isolation, and verification. Alongside that work, I develop independent physics research and computational tools. My proposed contribution to a quantum-hardware team is to connect measurements and software with the practical work of making complex equipment understandable and reliable.

## For Hillary — Friday, 25 September 2026

**Start with the engineering demonstration:** [Microwave calibration and drift diagnostic workbench](https://github.com/JasonSEFIDEFI/SEFI-PY/tree/main/SEFI-PY%20Evolution/research/calibration_workbench).

The prototype asks a field engineering question: **What changed, what should we measure next, and how do we verify recovery?** It uses synthetic microwave-transition measurements to compare conventional fitting and tracking with a geometric approach inspired by my SEFI research.

| Five-minute review | Link |
|---|---|
| Problem, implementation, and reproduction commands | [Workbench guide](https://github.com/JasonSEFIDEFI/SEFI-PY/blob/main/SEFI-PY%20Evolution/research/calibration_workbench/README.md) |
| Practical output for an engineer | [Service report](https://github.com/JasonSEFIDEFI/SEFI-PY/blob/main/SEFI-PY%20Evolution/research/calibration_workbench/sample_output/service_report.md) |
| Handling insufficient evidence | [Ambiguous-case report](https://github.com/JasonSEFIDEFI/SEFI-PY/blob/main/SEFI-PY%20Evolution/research/calibration_workbench/sample_output/ambiguous_report.md) |
| Actual results and limitations | [Validation record](https://github.com/JasonSEFIDEFI/SEFI-PY/blob/main/SEFI-PY%20Evolution/research/calibration_workbench/VALIDATION.md) |
| Professional experience | [Resume PDF](Master%20Resume.pdf) · [Resume source](Master%20Resume.tex) |

The visual demonstration is included as `sample_output/index.html`; download the workbench and open it locally. GitHub displays its source rather than hosting the page.

### What the prototype establishes

- A reproducible measurement-to-report workflow, with CSV replay and explicit operating assumptions.
- Comparisons using identical measurements and separate healthy threshold-calibration data.
- Detection of the simulated amplitude, detuning, and mixed-drift cases, plus an example where the tool requests additional measurements.
- Eleven passing tests covering this addition, including physical limits, observability, input checks, and recovery verification.

**It does not establish a SEFI advantage over conventional tracking.** The included benchmark shows similar detection delays and a recovery lag in both smoothed methods. All data are synthetic; no eleQtron equipment was tested. The prototype is neither hardware-ready quantum error correction nor a validated digital twin.

### Why this direction fits eleQtron

The public motivation is eleQtron researchers' discussion of [microwave-chain error and coherent storage transfer](https://indico.fysik.su.se/event/9371/contributions/15175/), alongside the company's [system-test work in RF characterization, debugging, validation, and automation](https://eleqtron.com/en/jobs/rf-radio-frequency-test-engineer-f-m-d/). This is an independent proposal, not an eleQtron assignment or endorsement.

**Proposed next conversation:** identify one calibration or diagnostic workflow with an RF validation or operations engineer, agree on relevant measurements and acceptance criteria, and test a small pilot against the team's existing method.

## Field engineering experience

The following roles and scope are documented in the linked resume:

- **Lead Electrician, pilot process research installation — Mineral Refining Company / Lone Mountain Refining, 2015–2016.** Led electrical integration; worked with control prints, ladder logic, sensor interfaces, installation verification, commissioning, and field testing on a Virginia Tech-directed pilot deployment.
- **Underground Electrical Repairman — Paramount Contura / Alpha Metallurgical Resources, 2022–2025.** Diagnostics and maintenance under demanding operational constraints.
- **Underground Electrician / Maintenance Foreman — Alpha Natural Resources, 2010–2016.** Electrical maintenance, fault isolation, and compliance responsibilities.
- **Fabricator, Welder, and Foreman — Dominion Steel, 2016–2018.** Shop and field coordination, quality, and production execution.

This experience is the basis for the proposed engineering contribution. The prototype does not imply prior hands-on operation of a trapped-ion quantum computer or specific RF instruments. Equipment-specific training and validation would be part of a new role.

The existing resume includes broader research positioning and material prepared for another opportunity; this README provides the focused introduction for the eleQtron conversation.

## Research and software portfolio

The broader research is available for technical review, without requiring it as the starting point for evaluating the engineering demonstration.

- [SEFI-PY software](https://github.com/JasonSEFIDEFI/SEFI-PY) and [QEC research stack](https://github.com/JasonSEFIDEFI/SEFI_QEC_Stack).
- [Vortex Research Console](https://github.com/JasonSEFIDEFI/SEFI-PY/tree/main/SEFI-PY%20Evolution/sim/vortex_console): classical field calculations, visual inspection, parameter sweeps, and saved checkpoints. See its [reviewer guide](https://github.com/JasonSEFIDEFI/SEFI-PY/blob/main/SEFI-PY%20Evolution/sim/vortex_console/REVIEWER_GUIDE.md) and [test report](https://github.com/JasonSEFIDEFI/SEFI-PY/blob/main/SEFI-PY%20Evolution/sim/vortex_console/TEST_REPORT.md).
- [Doctoral research portfolio](https://github.com/JasonSEFIDEFI/PhD) and [Dr. Ersoy discussion checkpoint](https://github.com/JasonSEFIDEFI/PhD/tree/main/10_DISSERTATION/research_direction_2026_09_23).
- Earlier September research overview: [PDF](research_updates/2026-09-23/hillary_research_overview_2026_09_23.pdf) · [Markdown](research_updates/2026-09-23/hillary_research_overview_2026_09_23.md). This records the foundational research discussion; the workbench above is the current engineering proposal.

### Manuscript navigation

| Topic | Source |
|---|---|
| GWFM worldline proposal | [GWFM manuscript](GWFM/GWFM_Full_Manuscript_Dutton.tex) |
| SEFI identity-space proposal | [SEFI construction](SEFI/SEFI_Formal_Mathematical_Construction.tex) |
| DEFI dynamics proposal | [DEFI construction](DEFI/DEFI_Formal_Construction.tex) |
| Photonic QEC proposal | [Photonic manuscript](Photonics%20Submission/SEFI_GWFM_Photonic_QEC_Stability_Geometry.tex) |
| Acoustic visualization concept | [BOSE manuscript](BOSE/BOSE.tex) |
| Unified framework proposal | [Unifying manuscript](Defining%20SEFI/unifiying.tex) |
| Identity-space construction | [SEFI Space](SS/SEFI_Space_Full_Manuscript_Dutton.tex) |
| Specialized displacement/warp proposal | [Warp manuscript](Advances/Warp.tex) |

SEFI, DEFI, and GWFM remain research proposals. Current classical numerical results do not establish observed matter, universal gravity, or hardware error-correction performance. Submission identifiers do not establish acceptance or peer-reviewed publication. My research preparation is independent; I do not hold an awarded PhD.

