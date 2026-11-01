"""Independent unofficial proposal. Synthetic data only. Python 3.10+, no packages."""
import json, sqlite3, secrets, datetime, pathlib
import math
from contextlib import contextmanager
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from http.cookies import SimpleCookie
ROOT = pathlib.Path(__file__).resolve().parent
DB = ROOT / 'demo.sqlite3'
SESSIONS = {}
USERS = {'customer': ('customer', 1), 'neighbor': ('customer', 2), 'driver': ('employee', 3), 'manager': ('management', 4)}
def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
@contextmanager
def connect():
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
    try:
        with c: yield c
    finally: c.close()
def init():
    with connect() as c:
        c.executescript('''CREATE TABLE IF NOT EXISTS orders(id INTEGER PRIMARY KEY, customer INTEGER, basket TEXT, subtotal INTEGER, fee INTEGER, assisted INTEGER, status TEXT, driver INTEGER, miles REAL, minutes INTEGER, created TEXT, delivered TEXT, ontime INTEGER, application_id INTEGER, route TEXT DEFAULT 'Demo neighborhood', route_id INTEGER);
        CREATE TABLE IF NOT EXISTS routes(id INTEGER PRIMARY KEY, employee INTEGER, name TEXT, miles REAL, minutes INTEGER, direction TEXT);
        CREATE TABLE IF NOT EXISTS duty(employee INTEGER PRIMARY KEY, released INTEGER DEFAULT 0, note TEXT DEFAULT '', updated TEXT);
        CREATE TABLE IF NOT EXISTS applications(id INTEGER PRIMARY KEY, customer INTEGER, reason TEXT, status TEXT, note TEXT, expires TEXT, used INTEGER DEFAULT 0);
        CREATE TABLE IF NOT EXISTS rewards(id INTEGER PRIMARY KEY, order_id INTEGER UNIQUE, employee INTEGER, cents INTEGER, status TEXT);
        CREATE TABLE IF NOT EXISTS audit(id INTEGER PRIMARY KEY, actor INTEGER, action TEXT, detail TEXT, at TEXT);
        CREATE TABLE IF NOT EXISTS funding(id INTEGER PRIMARY KEY, remaining INTEGER);''')
        cols={r['name'] for r in c.execute('PRAGMA table_info(orders)')}
        if 'route' not in cols:c.execute("ALTER TABLE orders ADD COLUMN route TEXT DEFAULT 'Demo neighborhood'")
        if 'route_id' not in cols:c.execute('ALTER TABLE orders ADD COLUMN route_id INTEGER')
        if not c.execute('SELECT * FROM duty WHERE employee=3').fetchone():c.execute("INSERT INTO duty VALUES(3,0,'Awaiting store manager release',?)",(now(),))
        if not c.execute('SELECT * FROM funding').fetchone():
            c.execute("INSERT INTO routes VALUES(1,3,'Hazel Mountain corridor (synthetic)',18,45,'NE')")
            c.execute("INSERT INTO routes VALUES(2,3,'Rural valley corridor (synthetic)',22,60,'W')")
            c.execute('INSERT INTO funding VALUES(1,59505)')
            c.execute("INSERT INTO applications(customer,reason,status,note,expires) VALUES(2,'Transportation barrier, self-attested','approved','Synthetic approved case',?)", ((datetime.date.today()+datetime.timedelta(days=30)).isoformat(),))
            for i,status in enumerate(['placed','picking','ready','offered','accepted','offered','delivered','delivered','cancelled']):
                c.execute('INSERT INTO orders VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(1001+i,1 if i%2==0 else 2,'[{"name":"Weekly staples","qty":1,"cents":4250}]',4250,0 if i==7 else 495,int(i==7),status,3 if status in ['accepted','out_for_delivery','delivered'] else None,18 if i==3 else 22 if i==5 else 4.5,45 if i==3 else 60 if i==5 else 30,now(),now() if status=='delivered' else None,1 if i==6 else 0 if i==7 else None,1 if i==7 else None,'Hazel Mountain corridor (synthetic)' if i==3 else 'Rural valley corridor (synthetic)' if i==5 else 'Demo neighborhood',1 if i==3 else 2 if i==5 else None))
            c.execute('UPDATE applications SET used=1 WHERE id=1')
            for oid in [1007,1008]: c.execute("INSERT INTO rewards(order_id,employee,cents,status) VALUES(?,3,200,'pending')",(oid,))
CATALOG=[{'name':n,'cents':p} for n,p in [('Milk 1 gallon',389),('Whole wheat bread',249),('Eggs dozen',329),('Apples 3 lb',499),('Rice 2 lb',279),('Chicken breast 2 lb',899),('Frozen vegetables',219),('Oatmeal',349)]]
class Handler(BaseHTTPRequestHandler):
    def log_message(self,*a): pass
    def reply(self,data,status=200,cookie=None):
        b=json.dumps(data).encode(); self.send_response(status); self.send_header('Content-Type','application/json'); self.send_header('Cache-Control','no-store')
        if cookie:self.send_header('Set-Cookie',cookie)
        self.end_headers();self.wfile.write(b)
    def user(self):
        ck=SimpleCookie(self.headers.get('Cookie','')); return SESSIONS.get(ck['session'].value) if 'session' in ck else None
    def do_GET(self):
        if self.path in ['/assets/porch.png','/assets/family.png']:
            b=(ROOT/self.path.lstrip('/')).read_bytes();self.send_response(200);self.send_header('Content-Type','image/png');self.end_headers();self.wfile.write(b);return
        if self.path=='/':
            b=(ROOT/'index.html').read_bytes();self.send_response(200);self.send_header('Content-Type','text/html; charset=utf-8');self.end_headers();self.wfile.write(b);return
        if self.path!='/api/state': self.reply({'error':'Not found'},404);return
        u=self.user()
        if not u:self.reply({'error':'Sign in'},401);return
        role,uid=u
        with connect() as c:
            query='SELECT * FROM orders';params=()
            if role=='customer':query+=' WHERE customer=?';params=(uid,)
            if role=='employee':query+=" WHERE status='offered' OR driver=?";params=(uid,)
            orders=[dict(r) for r in c.execute(query,params)]
            apps=[dict(r) for r in c.execute('SELECT * FROM applications'+(' WHERE customer=?' if role=='customer' else ' WHERE 0' if role=='employee' else ''),(uid,) if role=='customer' else ())]
            rewards=[dict(r) for r in c.execute('SELECT * FROM rewards'+(' WHERE employee=?' if role=='employee' else ' WHERE 0' if role=='customer' else ''),(uid,) if role=='employee' else ())]
            metrics={}
            if role=='management':
                done=c.execute("SELECT COUNT(*),COALESCE(SUM(ontime),0),COALESCE(SUM(fee),0),COALESCE(SUM(minutes),0),COALESCE(SUM(miles),0),COALESCE(SUM(assisted),0) FROM orders WHERE status='delivered'").fetchone()
                metrics=dict(completed=done[0],ontime_percent=round(done[1]/done[0]*100,1) if done[0] else None,delivery_fees=done[2]/100,delivery_labor_hours=round(done[3]/60,2),miles=done[4],assisted_deliveries=done[5],fund_remaining=c.execute('SELECT remaining FROM funding').fetchone()[0]/100)
            self.reply(dict(role=role,uid=uid,catalog=CATALOG,orders=orders,duty=[dict(r) for r in c.execute('SELECT * FROM duty')] if role!='customer' else [],routes=[dict(r) for r in c.execute('SELECT * FROM routes')],applications=apps,rewards=rewards,metrics=metrics,audit=[dict(r) for r in c.execute('SELECT * FROM audit ORDER BY id DESC LIMIT 40')] if role=='management' else []))
    def do_POST(self):
        try:
            if self.headers.get('Origin') and self.headers['Origin'] not in ['http://127.0.0.1:8765','http://localhost:8765']: raise ValueError('Invalid origin')
            d=json.loads(self.rfile.read(min(int(self.headers.get('Content-Length',0)),20000)))
            if self.path=='/api/login':
                if d.get('username') not in USERS or d.get('password')!='demo':self.reply({'error':'Invalid demo credentials'},401);return
                token=secrets.token_urlsafe(32);SESSIONS[token]=USERS[d['username']];self.reply({'ok':True},cookie=f'session={token}; HttpOnly; SameSite=Strict; Path=/');return
            if self.path=='/api/logout':
                ck=SimpleCookie(self.headers.get('Cookie',''))
                if 'session' in ck:SESSIONS.pop(ck['session'].value,None)
                self.reply({'ok':True},cookie='session=; Max-Age=0; Path=/');return
            u=self.user()
            if not u:self.reply({'error':'Sign in'},401);return
            role,uid=u
            with connect() as c:
                c.execute('BEGIN IMMEDIATE')
                def require(condition,message='Action unavailable for this role or state'):
                    if not condition:raise ValueError(message)
                a=d.get('action');oid=d.get('id');o=c.execute('SELECT * FROM orders WHERE id=?',(oid,)).fetchone()
                if a=='duty':
                    require(role=='management');employee=int(d.get('employee',3));require(employee==3,'Unknown demo employee');note=d.get('note','').strip();require(3<=len(note)<=200,'Enter a staffing decision reason')
                    c.execute('UPDATE duty SET released=?,note=?,updated=? WHERE employee=?',(int(bool(d.get('released'))),note,now(),employee))
                elif a=='add_route':
                    require(role=='employee');name=d.get('name','').strip();miles=float(d.get('miles',0));minutes=int(d.get('minutes',0));direction=d.get('direction')
                    require(3<=len(name)<=100 and math.isfinite(miles) and miles>0 and minutes>0 and direction in ['N','NE','E','SE','S','SW','W','NW'],'Enter a route name, positive estimates and direction')
                    c.execute('INSERT INTO routes(employee,name,miles,minutes,direction) VALUES(?,?,?,?,?)',(uid,name,miles,minutes,direction))
                elif a=='order':
                    require(role=='customer');items=[];total=0
                    for i,p in enumerate(CATALOG):
                        q=int(d.get('quantities',{}).get(str(i),0));require(0<=q<=10,'Quantity must be 0–10')
                        if q:items.append(dict(name=p['name'],qty=q,cents=p['cents']));total+=q*p['cents']
                    require(total>=1500,'Minimum basket is $15')
                    assisted=bool(d.get('assisted'));fee=495;app=None
                    if assisted:
                        app=c.execute("SELECT * FROM applications WHERE customer=? AND status='approved' AND expires>=? AND used<4 ORDER BY id DESC LIMIT 1",(uid,datetime.date.today().isoformat())).fetchone()
                        require(app is not None,'Current approval with remaining allowance required')
                        require(c.execute('SELECT remaining FROM funding').fetchone()[0]>=495,'Assistance fund exhausted')
                        c.execute('UPDATE funding SET remaining=remaining-495');c.execute('UPDATE applications SET used=used+1 WHERE id=?',(app['id'],));fee=0
                    route=d.get('route','Demo neighborhood').strip();miles=float(d.get('estimate_miles',4.5));minutes=int(d.get('estimate_minutes',30))
                    require(2<=len(route)<=100 and math.isfinite(miles) and miles>0 and minutes>0,'Enter a route description and positive estimates')
                    rid=int(d.get('route_id') or 0);mapped=c.execute('SELECT * FROM routes WHERE id=?',(rid,)).fetchone() if rid else None
                    require(not rid or mapped is not None,'Choose a listed employee route')
                    require(miles<=5 or mapped is not None,'Outside the 5-mile radius: an employee-added map route is required')
                    if mapped:route=mapped['name'];miles=mapped['miles'];minutes=mapped['minutes']
                    c.execute('INSERT INTO orders(customer,basket,subtotal,fee,assisted,status,miles,minutes,created,application_id,route,route_id) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)',(uid,json.dumps(items),total,fee,int(assisted),'placed',miles,minutes,now(),app['id'] if app else None,route,rid or None))
                elif a=='apply':
                    require(role=='customer');reason=d.get('reason','').strip();require(5<=len(reason)<=200,'Enter a short reason, without sensitive details')
                    require(not c.execute("SELECT id FROM applications WHERE customer=? AND status IN ('pending','approved') AND (expires>=? OR status='pending')",(uid,datetime.date.today().isoformat())).fetchone(),'An active application already exists')
                    c.execute("INSERT INTO applications(customer,reason,status,note,expires) VALUES(?,?,'pending','','')",(uid,reason))
                elif a=='review':
                    require(role=='management');status=d.get('decision');require(status in ['approved','denied']);note=d.get('note','').strip();require(5<=len(note)<=200,'A review reason is required')
                    require(c.execute("SELECT id FROM applications WHERE id=? AND status='pending'",(oid,)).fetchone())
                    c.execute('UPDATE applications SET status=?,note=?,expires=? WHERE id=?',(status,note,(datetime.date.today()+datetime.timedelta(days=30)).isoformat(),oid))
                elif a=='reward':
                    require(role=='management');r=c.execute('SELECT * FROM rewards WHERE id=?',(oid,)).fetchone();require(r is not None)
                    require(r['status'] in ['pending','approved']);c.execute('UPDATE rewards SET status=? WHERE id=?',('approved' if r['status']=='pending' else 'issued',oid))
                else:
                    require(o is not None,'Order not found');s=o['status']
                    if a=='cancel':
                        require((role=='customer' and o['customer']==uid and s in ['placed','picking']) or (role=='management' and s in ['placed','picking','ready','offered']));ns='cancelled'
                        if o['assisted']:
                            c.execute('UPDATE funding SET remaining=remaining+495');c.execute('UPDATE applications SET used=MAX(0,used-1) WHERE id=?',(o['application_id'],))
                    elif a in ['pick','ready','offer']:
                        require(role=='management');expected,ns={'pick':('placed','picking'),'ready':('picking','ready'),'offer':('ready','offered')}[a];require(s==expected)
                    elif a=='accept':
                        require(role=='employee' and s=='offered')
                        require(c.execute('SELECT employee FROM duty WHERE employee=? AND released=1',(uid,)).fetchone(),'Store manager must release you for delivery duty first')
                        if o['route_id']:require(c.execute('SELECT id FROM routes WHERE id=? AND employee=?',(o['route_id'],uid)).fetchone(),'Only the employee who added this route can accept its deliveries')
                        require(not c.execute("SELECT id FROM orders WHERE driver=? AND status IN ('accepted','out_for_delivery')",(uid,)).fetchone(),'Complete the current assignment first');ns='accepted';c.execute('UPDATE orders SET driver=? WHERE id=?',(uid,oid))
                    elif a=='release':require(role=='employee' and o['driver']==uid and s=='accepted');ns='offered';c.execute('UPDATE orders SET driver=NULL WHERE id=?',(oid,))
                    elif a=='depart':
                        require(role=='employee' and o['driver']==uid and s=='accepted');require(c.execute('SELECT employee FROM duty WHERE employee=? AND released=1',(uid,)).fetchone(),'Manager release is required before departure');ns='out_for_delivery'
                    elif a in ['deliver','fail']:
                        require(role=='employee' and o['driver']==uid and s=='out_for_delivery');ns='delivered' if a=='deliver' else 'failed'
                        minutes=int(d.get('minutes',30));miles=float(d.get('miles',4.5));require(minutes>0 and math.isfinite(miles) and miles>=0,'Check time and mileage')
                        c.execute('UPDATE orders SET minutes=?,miles=? WHERE id=?',(minutes,miles,oid))
                        if a=='deliver':
                            require(d.get('proof')=='confirmed','Confirm handoff and safe handling');c.execute('UPDATE orders SET delivered=?,ontime=? WHERE id=?',(now(),int(bool(d.get('ontime'))),oid));c.execute("INSERT INTO rewards(order_id,employee,cents,status) VALUES(?,?,200,'pending')",(oid,uid))
                    else:raise ValueError('Unknown action')
                    c.execute('UPDATE orders SET status=? WHERE id=?',(ns,oid))
                c.execute('INSERT INTO audit(actor,action,detail,at) VALUES(?,?,?,?)',(uid,a,str(oid or 'new'),now()))
            self.reply({'ok':True})
        except (ValueError,TypeError,KeyError,json.JSONDecodeError) as e:self.reply({'error':str(e)},400)
        except Exception:self.reply({'error':'Unable to complete action'},500)
if __name__=='__main__':
    init();print('Community Connect: http://127.0.0.1:8765 (Ctrl+C to stop)');ThreadingHTTPServer(('127.0.0.1',8765),Handler).serve_forever()
