# Food City Community Connect

Independent, unofficial proposal. No affiliation, endorsement, Food City integration, real customer data, payments, messages or fuel vouchers. All names, orders, prices and addresses/service areas are fictional. Use only on your own computer.

## Run

1. Install Python 3.10 or newer if needed.
2. Extract the entire ZIP. Open a terminal in the `community-connect` folder.
3. Run `python server.py` (Windows may also support `py server.py`).
4. Open http://127.0.0.1:8765 in a browser. Stop with Ctrl+C.

No third-party packages or internet connection required. The server listens only on the local loopback address. Data persists in `demo.sqlite3`, created on first run. To reset, stop the server and delete that file, then restart. Never expose this demo server to a network. Demo accounts share password `demo`: `customer`, `neighbor` (approved assistance), `driver`, `manager`. Use separate browser profiles for simultaneous roles; tabs in one profile share a login.

## Guided demonstration

1. Customer: add a basket worth at least $15, place a paid order and request assistance using a short synthetic transportation-barrier reason.
2. Manager: release the employee for delivery duty with a staffing reason, then approve the application with a rationale. Progress the order through picking, ready, and offer.
3. Driver: finish the seeded active assignment first, then accept the offered order. Release before departure if unavailable, or depart. Enter minutes and miles, confirm safe handoff and on-time status, complete delivery.
4. Manager: approve the automatically created $2 fuel reward and record simulated issuance. Export the scorecard. Verify the order appears once in the reward ledger.
5. Neighbor: place an assisted order and see the $0 fee. Manager sees the fund reduce by $4.95. Cancellation before departure restores that reservation.

## Implemented boundaries

Server enforces roles and ownership, state transitions, single active driver assignment, current assistance approval, four-use allowance, atomic fund reservations, unique reward per delivery, session cookies, and an activity log. Failed deliveries remain exceptions for management review and generate no reward. Time/miles are recorded for labor review, including failure. Seeded examples span all principal states and intentionally show an on-time miss.

Assistance covers delivery fees only. Approval is a demonstration policy, not a claim of actual benefit eligibility. Grocery totals exclude tax and substitutions. Route miles and time are estimates until employee entry. No GPS, routing, payment capture, stock reservation, SMS, real ID verification, payroll calculation, overtime validation, safety verification, voucher redemption, or production identity provider. Management is one combined demo role; real deployment should separate eligibility, dispatch and finance permissions.

The demo uses simple shared credentials and in-memory sessions, no session expiry, no TLS, and minimal hardening. It has no production backup or monitoring. The audit table is useful for demonstration but not tamper-proof. See the architecture and pilot document for the production design and decision gates.

## Checks

Run `python test_demo.py` to exercise workflow and authorization using an isolated temporary database. It does not change your demo database.


## Radius and employee-added routes

The default radius is five miles. An employee can add a rural or homeward corridor to the delivery map, creating a coverage exception. Customers outside the radius must choose a listed employee-added route. Only the employee who added that route can accept its deliveries. Adding a route does not commit the employee to every order. Safe access, paid duty, insurance, handling and funding still apply.

The map is a synthetic schematic, not live geography. Entered delivery miles act as a simplified radius proxy. Real deployment needs address-to-route validation and separate straight-line radius and road-mile calculations. Two synthetic rural corridors appear at startup. Sign in as driver to add another, then as customer to select it.

## Store manager authority

Only management can release an employee for delivery duty. Both acceptance and departure require that release. Employees cannot release themselves. Recalling an employee blocks new acceptance/departure, while a delivery already in progress can safely finish. Employee route entries do not override this staffing decision.

## Drone roadmap

The architecture plan includes future central drone hubs, with Abingdon as an illustrative location for feasibility review. No aircraft connection, live mission simulation or flight control is implemented. Employee ground delivery remains the functional prototype mode.
