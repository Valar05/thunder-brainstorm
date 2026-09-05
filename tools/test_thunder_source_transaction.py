import importlib.util,json,os,subprocess,tempfile,unittest
from pathlib import Path
S=Path(__file__).with_name('thunder_source_transaction.py')
spec=importlib.util.spec_from_file_location('tx',S);tx=importlib.util.module_from_spec(spec);spec.loader.exec_module(tx)
def cmd(cwd,*a):
 r=subprocess.run(list(a),cwd=cwd,text=True,capture_output=True,check=False)
 if r.returncode: raise RuntimeError((a,r.stdout,r.stderr))
 return r.stdout.strip()
def init_repo(root):
 repo=root/'repo';repo.mkdir();cmd(repo,'git','init','-q');cmd(repo,'git','config','user.name','T');cmd(repo,'git','config','user.email','t@x')
 (repo/'thunder_brainstorm.py').write_text('import sys\n')
 idx=repo/'generated/index_combined/mechanic_source_refs.jsonl';idx.parent.mkdir(parents=True);idx.write_text('')
 cmd(repo,'git','add','.');cmd(repo,'git','commit','-qm','base');return repo
def gap(repo,out):
 a=type('A',(),{'repo':str(repo),'index':'generated/index_combined/mechanic_source_refs.jsonl','python':'python','query':'missing thing','limit':5,'capability':'cap','project':'p','owner_evidence':['p/owner.py:1'],'out':str(out)})
 tx.create_gap(a);return json.loads(out.read_text())
def packet(g):
 src={'origin':'github','repo':'Valar05/example','commit':'a'*40,'path':'x.py','line':1,'symbol':'owner','license':'MIT','sha256':'b'*64,'compatibility':'python3','behavioral_contract':'does the bounded thing','deviations':[]}
 return tx.sealed({'schema':tx.PACKET_SCHEMA,'gap_seal':g['gap_seal'],'search_order':g['jit_order'],'sources':[src]},'packet_seal')
class T(unittest.TestCase):
 def setUp(self):self.t=tempfile.TemporaryDirectory();self.root=Path(self.t.name);self.repo=init_repo(self.root);self.recovery=self.root/'recovery'
 def tearDown(self):self.t.cleanup()
 def test_gap_requires_clean_and_no_local_hit(self):
  g=gap(self.repo,self.root/'gap.json');self.assertEqual(g['local_result'],'NO_REUSABLE_SOURCE');self.assertTrue(g['external_only'])
  (self.repo/'dirty').write_text('x')
  with self.assertRaisesRegex(tx.ThunderSourceError,'dirty'):gap(self.repo,self.root/'g2.json')
 def test_packet_provenance_and_gap_binding(self):
  g=gap(self.repo,self.root/'gap.json');p=packet(g);tx.validate_packet(p,g);p['sources'][0].pop('license')
  p=tx.sealed(p,'packet_seal')
  with self.assertRaisesRegex(tx.ThunderSourceError,'fields'):tx.validate_packet(p,g)
 def test_publish_one_commit_clean_fast_forward(self):
  gp=self.root/'gap.json';g=gap(self.repo,gp);pp=self.root/'packet.json';tx.save(pp,packet(g));entry=cmd(self.repo,'git','rev-parse','HEAD')
  a=type('A',(),{'repo':str(self.repo),'gap':str(gp),'packet':str(pp),'test_commands':'[["python","-m","py_compile","thunder_brainstorm.py"]]','dirty_window_seconds':60.0,'temp_root':str(self.root),'recovery_dir':str(self.recovery)})
  r=tx.publish(a);self.assertTrue(r['ok']);self.assertNotEqual(entry,r['commit']);self.assertEqual(cmd(self.repo,'git','rev-list','--count',f'{entry}..HEAD'),'1');self.assertEqual(cmd(self.repo,'git','status','--porcelain=v1'),'');self.assertLess(r['dirty_window_seconds'],60)
  self.assertTrue((self.repo/'generated/jit_source_packets'/f"{packet(g)['packet_seal']}.json").is_file())
 def test_failure_preserves_canonical_and_recovery(self):
  gp=self.root/'gap.json';g=gap(self.repo,gp);pp=self.root/'packet.json';tx.save(pp,packet(g));entry=cmd(self.repo,'git','rev-parse','HEAD')
  a=type('A',(),{'repo':str(self.repo),'gap':str(gp),'packet':str(pp),'test_commands':'[["python","-c","raise SystemExit(7)"]]','dirty_window_seconds':60.0,'temp_root':str(self.root),'recovery_dir':str(self.recovery)})
  with self.assertRaisesRegex(tx.ThunderSourceError,'recovery='):tx.publish(a)
  self.assertEqual(cmd(self.repo,'git','rev-parse','HEAD'),entry);self.assertEqual(cmd(self.repo,'git','status','--porcelain=v1'),'');self.assertEqual(len(list(self.recovery.glob('*.json'))),1)
 def test_portable_lock_live_ambiguous_and_dead_recovery(self):
  lock=tx.acquire(self.repo,'x')
  with self.assertRaisesRegex(tx.ThunderSourceError,'held'):tx.acquire(self.repo,'y')
  tx.release(lock);lock.mkdir()
  with self.assertRaisesRegex(tx.ThunderSourceError,'ambiguous'):tx.acquire(self.repo,'y')
  lock.rmdir();lock=tx.acquire(self.repo,'x');owner=json.loads((lock/'owner.json').read_text());journal=json.loads((lock/'journal.json').read_text());owner['pid']=99999999;journal['pid']=99999999;tx.save(lock/'owner.json',tx.sealed(owner,'owner_seal'));tx.save(lock/'journal.json',tx.sealed(journal,'journal_seal'))
  self.assertEqual(tx.recover_lock(self.repo)['action'],'recovered')
if __name__=='__main__':unittest.main()
