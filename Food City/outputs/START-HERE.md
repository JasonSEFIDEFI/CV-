# Food City Community Connect

Independent, unofficial proposal. Synthetic data only. No Food City affiliation, system connection or endorsement.

## Current edition

- `Food-City-Community-Connect-Final.pptx`: executive pitch, customer illustrations, rural route exceptions, manager staffing authority and drone hub roadmap.
- `Food-City-Community-Connect-Brochure.pdf`: four-page red-and-blue brochure with illustrative customer imagery.
- `Architecture-and-Pilot.html`: readable technical architecture, policies, one-store pilot, financial assumptions and risks. Markdown source is also included.
- `Community-Connect-Prototype.zip`: runnable local app, source, synthetic fixtures, images and workflow checks.
- `community-connect/README.md`: detailed run instructions and demonstration sequence.
- `Food-City-Complete-Workspace.zip`: complete project snapshot, including sources, assets, build scripts, previews and validation records. A manifest records file hashes.

## Run the prototype

With Python 3.10+ installed, open the `community-connect` folder and run `python server.py`, or double-click `Start-Demo.cmd` on Windows. Open http://127.0.0.1:8765 . Demo usernames: `customer`, `neighbor`, `driver`, `manager`. Password for each: `demo`.

## Final operating decisions

1. The default five-mile radius applies unless an employee adds a rural corridor to the delivery map.
2. Outside-radius orders must select a listed employee route. The route creator chooses which deliveries to accept.
3. The store manager decides whether an employee can be spared. Manager release is required for acceptance and departure. Route creation alone never grants permission to leave the store.
4. Employee participation is voluntary to accept, with paid delivery duties. Fuel rewards supplement wages and mileage reimbursement.
5. Recalling staff blocks new trips while allowing a delivery already underway to finish safely.
6. Assistance waives delivery fees after review, subject to allowance and funding. Groceries remain customer funded.
7. Central drone hubs, including Abingdon as a feasibility example, are a long-term design ambition. No flight control or aircraft integration is implemented.

## Demonstration first steps

Sign in as manager and release employee 3 for delivery duty with a staffing reason. Then sign in as driver to complete or release the seeded assignment, inspect rural routes, and add a new synthetic corridor. As customer, select that route and place a basket of at least $15. Manager prepares and offers the order. Driver chooses whether to accept, departs and records completion. Manager reviews the resulting reward and scorecard.

The map is a synthetic schematic and uses entered delivery miles as a simplified radius proxy. Production requires exact address and corridor validation. All customer scenes are AI-generated illustrations of fictional people, not actual Food City customers.
