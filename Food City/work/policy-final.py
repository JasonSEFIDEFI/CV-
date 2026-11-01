from pathlib import Path
p=Path('outputs/Architecture-and-Pilot.md');s=p.read_text(encoding='utf-8-sig');start=s.index('## Rural route policy');end=s.index('## Financial model',start)
s=s[:start]+'''## Radius rule and employee route exceptions

The default delivery radius is five miles. Outside that radius, an employee must add a corridor to the delivery map before a customer can book against it. That route extends coverage for willing participation along a rural or homeward journey, including mountain communities. Adding a route does not require accepting every order. The employee who adds the route chooses whether to accept deliveries on that corridor, with no penalty for declining. Safe access, vehicle coverage, paid duty capacity, handling and funding still apply.

The prototype includes a synthetic coverage map, two seeded employee-added corridors of 18 and 22 delivery miles, and an employee form to add more. Outside-radius bookings without a listed route fail validation. Customers select an employee-added route for an exception. The employee who added it must accept the assignment. The demo uses entered delivery miles as a simplified radius proxy, and its map is a schematic. Production must distinguish straight-line radius from driving distance, use authorized geocoding, validate exact address-to-corridor membership, constrain detours, and expire or withdraw unavailable routes. A route name alone cannot establish actual geographic coverage.

Homeward deliveries remain employer-directed delivery duties with a reviewed pay and mileage policy. Distinguish normal commuting from compensable delivery activity using HR-approved time and mileage rules. Record attributable delivery time and reimbursable miles. An assistance applicant outside the default radius can qualify when an employee-added route covers the household.

'''+s[end:]
s=s.replace('employee-selected rural routes with no fixed radius','a five-mile default radius with employee-added rural map routes').replace('rural routes without a fixed radius','a five-mile default radius with employee-added rural map routes')
s=s.replace('Customer | Build basket','Customer | Select coverage or employee route, build basket').replace('Employee | See available offers','Employee | Add coverage routes to map, see available offers')
p.write_text(s,encoding='utf-8')
p=Path('outputs/community-connect/README.md');s=p.read_text(encoding='utf-8-sig');s=s[:s.index('## Rural routes')]+'''## Radius and employee-added routes

The default radius is five miles. An employee can add a rural or homeward corridor to the delivery map, creating a coverage exception. Customers outside the radius must choose a listed employee-added route. Only the employee who added that route can accept its deliveries. Adding a route does not commit the employee to every order. Safe access, paid duty, insurance, handling and funding still apply.

The map is a synthetic schematic, not live geography. Entered delivery miles act as a simplified radius proxy. Real deployment needs address-to-route validation and separate straight-line radius and road-mile calculations. Two synthetic rural corridors appear at startup. Sign in as driver to add another, then as customer to select it.\n''';p.write_text(s,encoding='utf-8')
p=Path('work/build-brochure.py');s=p.read_text(encoding='utf-8-sig').replace('No fixed service radius. Employees choose rural and homeward routes, subject to safe access and paid work capacity.','The five-mile radius applies unless an employee adds a rural or homeward corridor to the delivery map. Employees choose which route deliveries to accept.');p.write_text(s,encoding='utf-8')
