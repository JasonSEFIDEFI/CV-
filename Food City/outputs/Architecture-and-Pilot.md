# Food City Community Connect

**Independent, unofficial proposal.** Prepared October 31, 2026. No affiliation or endorsement. No connection to Food City inventory, checkout, loyalty, payroll or fuel systems. All numbers below are planning assumptions, not Food City operating data. Red (#C92032) and blue (#123269) are proposal design colors, not verified brand specifications.

## Executive concept

One platform serves households purchasing grocery delivery and households receiving a delivery fee waiver. Customers choose groceries and request assistance. Employees freely choose whether to accept available paid delivery assignments. Managers coordinate store preparation, eligibility, capacity and the fund. Fuel rewards provide an optional supplementary incentive, separate from wages, mileage reimbursement and overtime obligations.

The initial assistance benefit waives a $4.95 delivery fee. It does not pay for groceries, taxes or tips. A future grocery subsidy would require its own policy, accounting and funding. Do not promise free delivery solely based on age: proposed eligibility considers a transportation barrier, the service zone, funding and a documented decision. Offer a telephone-assisted channel in the real pilot for residents who cannot use the website.

## Product and service design

| Console | Primary actions | Information boundary |
|---|---|---|
| Customer | Build basket, place paid/assisted order, cancel early, request eligibility review, track status | Own orders and application only |
| Employee | See available offers, accept/release, depart, record completion/failure, minutes and miles, inspect rewards | Offers and own assignments/rewards, no eligibility reasons |
| Management | Pick/ready/offer, review assistance, cancel early, approve/issue demo rewards, inspect metrics/audit | Combined demo role, split into dispatcher, eligibility reviewer and finance approver in production |

Order lifecycle: placed → picking → ready → offered → accepted → out for delivery → delivered or failed. Customers cancel only while placed/picking. Management can cancel through offered. Employees can release an accepted order before departure. Delivery requires handoff confirmation. Failure records work time and mileage but earns no reward and requires an exception review before replacement or refund. No duplicate completion or reward issuance.

Dispatch is a manual offer board, not optimized routing. Managers should check staff coverage, paid hours, vehicle approval and capacity before offering. Drivers choose assignments voluntarily. A real system should expire unaccepted offers after 10 minutes, alert a dispatcher and offer a customer reschedule/refund if no driver is available. The local prototype does not run timers or send alerts.

Assistance lifecycle: pending → approved/denied with reason. Approvals last 30 days, with up to four fee waivers, subject to remaining fund balance. Proposed pilot: self-attested transportation barrier with reviewer confirmation, no diagnoses or income documents in the demo. Real enrollment must provide consent, a plain-language notice, appeal route, renewal reminders and alternatives when funding runs out. Managers should review appeals within two business days. Reserve $4.95 when an assisted order is placed, restore it on eligible cancellation, retain the charge on failed delivery pending manual review. Store the application ID on each order so cancellations restore the correct allowance. Benefit renewal creates a new application after expiry, including when the prior four uses have already been consumed.

Rewards: one $2 pending credit per successful order → finance approval → biweekly issuance. Prototype issuance is a ledger label only, with no redeemable voucher. Production needs unique batch and voucher IDs, vendor reconciliation, rejected-issue retries, reversals, expiry policy and employee disputes. Payroll/tax review determines treatment and any regular-rate effects. Do not use fuel rewards as a substitute for compensation or expense reimbursement.

## Local technical architecture

Browser (HTML/CSS/JavaScript) communicates over same-origin JSON with a Python standard-library HTTP server on 127.0.0.1:8765. Server checks session role and record ownership, validates transitions and persists to SQLite. Transactional writes reserve assistance funds and assign orders atomically. Database constraints enforce one reward per order. In-memory sessions use HttpOnly, SameSite cookies. No cloud services, packages, external APIs, telemetry or real accounts are required.

Entities: orders, assistance applications, fund balance, rewards and audit events. Catalog and demo identity fixtures live in source. Money uses integer cents. Timestamps use UTC. The server-generated activity log records actor, action, object and time. The seed contains nine orders across lifecycle states, one approved assistance case, and two pending rewards. It is a synthetic snapshot, not a measured history. Estimates and seeded dates should never be presented as pilot outcomes.

## Production target and gaps

Proposed architecture: accessible web/mobile views → authenticated API gateway → order, eligibility, dispatch and ledger modules → relational database. Add a transactional outbox and worker for payment and notification events. Maintain separate payment provider tokens, never card data. A future adapter layer could connect authorized inventory, POS, payroll or fuel services only after Food City grants access and approves contracts. Until then, use manual reconciliation and approved exports. No integration capability is claimed.

Use SSO/MFA for staff, customer account recovery, session expiry, TLS, CSRF protection, rate limits, validation and authorization tests. Separate reviewer and finance privileges, encrypt sensitive fields, log access to eligibility records, and record immutable ledger events. Introduce idempotency keys, optimistic version checks, refund/reward reversals, workload limits and external-provider reconciliation. Move from SQLite to managed PostgreSQL for concurrent stores and durable backups. Add monitoring for queue age, failures and fund reconciliation, daily encrypted backups with restore drills, dependency scanning and incident response. Proposed recovery targets: restore within four hours, lose no more than one hour of data, subject to validation.

Privacy proposal: collect only delivery contact/address and minimum eligibility decision metadata. Drivers see exact address only after assignment and lose access after closure. Keep medical records out of the platform. Proposed retention: remove detailed eligibility reasons within 90 days of closure, retain finance records under an approved schedule, and aggregate/de-identify operational metrics. Counsel and privacy leadership must approve retention and consent before use. The demo intentionally has no real contact/address fields and must never receive personal information.

Other deliberate gaps: real payment authorization/capture/refund, inventory/substitutions, taxes, assistance appeals UI, precise delivery windows, cold-chain sensors, routing, mileage verification, payroll/overtime calculation and reward redemption. Failed deliveries require manual resolution. Demo credentials and session handling do not meet production security needs. The local audit log is mutable by the database owner. Functional prototype readiness is distinct from live pilot readiness.

## One-store pilot

Proposed duration: four weeks of readiness followed by eight weeks of service. One store selected by leadership, a five-mile zone after route validation, 20 completed orders/day, five days/week, two windows/day, 800 completed orders total. Reserve 30% (240 orders) for delivery assistance. Target approximately 40–60 assisted households without implying all will order weekly. Recruit 6–8 interested employees with paid training and voluntary assignment acceptance. Staff managers must ensure grocery operations remain covered. No alcohol, tobacco, controlled medicines or other age-restricted items in the pilot.

| Period | Owner | Deliverable / gate |
|---|---|---|
| Readiness weeks 1–2 | Executive sponsor, operations, HR, risk, counsel | Named owner, signed scope, labor model, insurance and vehicle requirements, budget and funding commitments |
| Readiness weeks 3–4 | Store lead, IT/security, community coordinator | Background/driver checks as approved, safe handling training, consent/appeals process, dry runs and incident drill |
| Service weeks 1–2 | Store lead | Cap at 10/day, verify dispatch capacity, reconcile money daily, interview users |
| Service weeks 3–6 | Store lead and analyst | Raise to 20/day only after safety and service checks, weekly review and employee feedback |
| Service weeks 7–8 | Sponsor and finance | Evaluate unit costs, access outcomes and staff impact, decide stop/adjust/expand |

The financial base case assumes 800 completions despite the ramp. Recover volume only if capacity permits; otherwise report actual volume and the higher fixed cost per order. At 700 completions, using the same mix and unit assumptions, operating gap becomes $12,866.67 rather than $14,453.33. A two-window 20/day schedule with 30 delivery minutes/order needs about 10 delivery labor hours/day, plus 3.33 picking hours and 2 coordination hours. Availability, peak staffing and route safety must support that demand. No unpaid commute deliveries.

## Financial model

Eight-week base case. Grocery merchandise revenue and cost, taxes and tips are excluded. No basket margin, retention or charitable grant is credited as a proven benefit. Loaded labor rate is a placeholder inclusive of assumed overhead; finance must substitute actual wage, benefit, overtime and payroll assumptions. Mileage reimbursement of $0.70/mile is a budget input, not a claim of a legal or IRS rate.

| Per completed delivery | Calculation | Cost |
|---|---|---:|
| Paid delivery labor | 0.5 hour × $22/hour | $11.00 |
| Picking labor | 10 minutes × $22/hour | $3.67 |
| Vehicle reimbursement | 4.5 miles × $0.70 | $3.15 |
| Supplementary fuel reward | $2 per completion | $2.00 |
| Supplies / payment placeholder | $1 per completion | $1.00 |
| Total variable cost | Exact picking cost uses $22/6 | **$20.8167** |

| Eight-week base case | Calculation | Amount |
|---|---|---:|
| Variable expense | 800 × $20.8166667 | $16,653.33 |
| Store coordination | 40 days × 2 hours × $22 | $1,760.00 |
| Total operating expense | Variable + coordination | **$18,413.33** |
| Customer delivery fees | 560 paid × $4.95 | $2,772.00 |
| Proposed assistance sponsor transfer | 240 waivers × $4.95 | $1,188.00 |
| Operating gap after assumed sponsor transfer | Expense − both receipts | **$14,453.33** |
| Readiness/setup allowance | Training, IT, equipment, review | $15,000.00 |
| Contingency | 15% × (operating + setup) | $5,012.00 |
| Gross spend authorization | Operating + setup + contingency | **$38,425.33** |
| Net funding after customer fees | Gross spend − customer fees | **$35,653.33** |
| Store funding if sponsor commits $1,188 | Net funding − sponsor | **$34,465.33** |

Fee waivers consume a benefit budget; sponsor transfers count only if someone commits cash. They do not create new economic value when funded by the store itself. The assistance reserve in the demo is $600, of which $4.95 is consumed by one seeded completion. This is a demonstration fund, separate from the $1,188 pilot assumption. No donors or partners are committed.

At $4.95 receipt for every completed order (customer or sponsor), operating support needed is $18.0667/order at 800 completions, including coordination. With no sponsor, the support increases by $1,188 in total. Break-even fee at this volume is $23.0167 per completion before setup/contingency. This concept requires an explicit community-service budget or different economics. It is not financially self-sustaining at the proposed fee.

Sensitivity: 20 delivery minutes lowers the operating gap by $2,933.33 to $11,520.00. Forty minutes raises it to $17,386.67. Six route miles raises the base gap by $840 to $15,293.33. A $7.95 paid fee adds $1,680 in receipts at unchanged volume/mix, lowering the gap to $12,773.33; willingness to pay is untested. At 700 completions the operating gap is $12,866.67, with unchanged $1,760 coordination and $4.95 receipt per completion. Reforecast weekly using actual time, mileage, failures and overtime. These sensitivities change one input at a time.

## Measurement and decisions

| Metric | Definition / collection | Proposed target |
|---|---|---|
| On-time delivery | Completed within promised window / completed, excluding none silently | ≥95%, with at least 100 completions before scale decision |
| Completion | Delivered / placed in same matured cohort | ≥97%; separately report cancellations and failed attempts |
| Delivery cost | Actual labor, picking, mileage, supplies and rewards / delivered | ≤$21 variable, plus fixed coordination reported separately |
| Assistance reach | Unique approved households served, fee waivers, denial reasons and queue age | 40–60 households, review within 2 business days |
| Employee choice | Acceptance / offers, release rate, anonymous coercion concern | Zero retaliation concerns unresolved; no target that pressures acceptance |
| Safety | Incidents, handling deviations and near misses per 100 attempts | Zero serious incidents; investigate all deviations |
| Customer experience | Post-delivery survey response rate and rating | ≥4.5/5 with sample size and response bias disclosed |
| Store impact | Picking hours, queue time, overtime and service complaints | No material harm to store service; manager-defined baseline |
| Ledger accuracy | Reconciled waivers, funds, rewards and failed issues | 100% daily match, no duplicate reward |

The prototype scorecard calculates completions, staff-confirmed on-time percentage, earned delivery fees, delivery hours, miles, assisted completions and assistance balance. Exported JSON is a demo snapshot. Full pilot metrics above require promised-window timestamps, placement cohorts, surveys, staff scheduling, incident intake and reconciliation sources before launch. Record baseline operations in readiness week four. Weekly reviews should break out paid/assisted service and employee workload without exposing individual eligibility reasons.

Expand only after sponsor, operations, finance and risk approve eight-week results, service targets, reconciled costs, no unresolved serious incidents, and a funded next stage. Pause immediately for a serious safety event, coverage lapse, fund mismatch, unsafe vehicle or privacy incident. Freeze new assisted bookings when the reserve cannot cover the next waiver. Keep approved customers informed and provide partner referrals only with consent. Stop if the gap exceeds the approved budget or repeat failures remain unresolved after two weekly reviews.

## Risks and controls

Labor: paid deliveries, accurate time records, HR review of overtime and reward treatment. Insurance: written commercial-use coverage and employer liability approval before any route. Food safety: insulated transport, segregation, time/temperature procedure, failed-handoff return instructions and training. Privacy: minimum collection, role separation and access logging. Funding: committed reserve, atomic reservations, weekly reconciliation. Availability: capped windows, employee opt-in, backup paid coverage and rescheduling. Fairness: published criteria, consistent decisions, appeals and phone access. Fraud: unique rewards, separate approver, issuance reconciliation and exception audit. Reputation: independent proposal label and no claims about existing Food City services or partnerships.

## Source basis and required professional review

U.S. Department of Labor states that employees may not volunteer services to for-profit private-sector employers. This proposal therefore treats delivery as paid work with voluntary acceptance: https://webapps.dol.gov/elaws/whd/FLSA/docs/volunteers.asp . Hours-worked guidance: https://www.dol.gov/agencies/whd/fact-sheets/22-flsa-hours-worked . FDA delivery guidance identifies transportation, packaging and temperature control as food-safety considerations: https://www.fda.gov/food/hfp-constituent-updates/fda-highlights-best-practices-food-safety-online-delivery-services . Consulted October 31, 2026. These general sources do not approve the proposed program. HR, counsel, insurer, food-safety leadership and finance must approve state-specific operations before a live pilot.

