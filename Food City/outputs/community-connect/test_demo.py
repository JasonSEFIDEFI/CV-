import unittest,tempfile,pathlib,threading,json,urllib.request,urllib.error,http.cookiejar
import server
class Workflow(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp=tempfile.TemporaryDirectory();server.DB=pathlib.Path(cls.tmp.name)/'test.db';server.init()
        cls.http=server.ThreadingHTTPServer(('127.0.0.1',0),server.Handler);threading.Thread(target=cls.http.serve_forever,daemon=True).start();cls.url='http://127.0.0.1:'+str(cls.http.server_port)
    @classmethod
    def tearDownClass(cls):cls.http.shutdown();cls.http.server_close();cls.tmp.cleanup()
    def client(self,name):
        op=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
        self.call(op,'login',dict(username=name,password='demo'));return op
    def call(self,op,path,data=None):
        req=urllib.request.Request(self.url+'/api/'+path,data=json.dumps(data).encode() if data is not None else None,headers={'Content-Type':'application/json'})
        with op.open(req) as r:return json.load(r)
    def test_end_to_end(self):
        customer=self.client('customer');manager=self.client('manager');driver=self.client('driver');neighbor=self.client('neighbor')
        def action(op,a,id=None,**kw):return self.call(op,'action',dict(action=a,id=id,**kw))
        with self.assertRaises(urllib.error.HTTPError):action(customer,'add_route',name='Mountain demo',miles=18,minutes=45,direction='NE')
        with self.assertRaises(urllib.error.HTTPError):action(customer,'order',quantities={'0':4},estimate_miles=18,estimate_minutes=45)
        action(driver,'add_route',name='Mountain neighbors demo',miles=18,minutes=45,direction='NE')
        rid=max(r['id'] for r in self.call(customer,'state')['routes'])
        action(customer,'order',quantities={'0':4},estimate_miles=18,estimate_minutes=45,route_id=rid)
        rural=max(self.call(customer,'state')['orders'],key=lambda o:o['id']);self.assertEqual(rural['route_id'],rid);self.assertEqual(rural['miles'],18)
        action(customer,'cancel',rural['id'])
        with self.assertRaises(urllib.error.HTTPError):action(customer,'pick',1001)
        with self.assertRaises(urllib.error.HTTPError):action(driver,'depart',1005)
        with self.assertRaises(urllib.error.HTTPError):action(driver,'duty',released=True,note='Cannot self release')
        action(manager,'duty',employee=3,released=True,note='Store coverage confirmed')
        with self.assertRaises(urllib.error.HTTPError):action(customer,'order',quantities={'0':4},assisted=True)
        action(customer,'apply',reason='Synthetic transportation barrier');apps=self.call(manager,'state')['applications'];aid=max(a['id'] for a in apps)
        action(manager,'review',aid,decision='approved',note='Self-attestation reviewed')
        action(customer,'order',quantities={'0':4},assisted=True);oid=max(o['id'] for o in self.call(customer,'state')['orders'])
        before=self.call(manager,'state')['metrics']['fund_remaining']
        with self.assertRaises(urllib.error.HTTPError):action(neighbor,'cancel',oid)
        action(customer,'cancel',oid);self.assertAlmostEqual(self.call(manager,'state')['metrics']['fund_remaining'],before+4.95)
        action(customer,'order',quantities={'0':4},assisted=True);oid=max(o['id'] for o in self.call(customer,'state')['orders'])
        with self.assertRaises(urllib.error.HTTPError):action(manager,'offer',oid)
        for a in ['pick','ready','offer']:action(manager,a,oid)
        action(driver,'depart',1005);action(driver,'deliver',1005,proof='confirmed',minutes=28,miles=4,ontime=True)
        action(driver,'accept',1006);action(driver,'depart',1006);action(driver,'fail',1006,minutes=34,miles=5)
        action(driver,'accept',oid);action(driver,'release',oid);action(driver,'accept',oid);action(driver,'depart',oid)
        action(manager,'duty',employee=3,released=False,note='Return to store after current delivery')
        with self.assertRaises(urllib.error.HTTPError):action(driver,'deliver',oid,proof='')
        action(driver,'deliver',oid,proof='confirmed',minutes=32,miles=4.8,ontime=True)
        with self.assertRaises(urllib.error.HTTPError):action(driver,'deliver',oid,proof='confirmed')
        rewards=self.call(manager,'state')['rewards'];rid=[r['id'] for r in rewards if r['order_id']==oid];self.assertEqual(len(rid),1)
        with self.assertRaises(urllib.error.HTTPError):action(driver,'reward',rid[0])
        action(manager,'reward',rid[0]);action(manager,'reward',rid[0])
        with self.assertRaises(urllib.error.HTTPError):action(manager,'reward',rid[0])
        self.assertFalse(self.call(driver,'state')['applications']);self.assertTrue(all(o['customer']==1 for o in self.call(customer,'state')['orders']))
        # Allowance and exhausted-fund checks use the isolated database.
        with server.connect() as c:c.execute('UPDATE applications SET used=4 WHERE customer=1')
        with self.assertRaises(urllib.error.HTTPError):action(customer,'order',quantities={'0':4},assisted=True)
        with server.connect() as c:c.execute('UPDATE funding SET remaining=0')
        with self.assertRaises(urllib.error.HTTPError):action(neighbor,'order',quantities={'0':4},assisted=True)
if __name__=='__main__':unittest.main()

