# Focused review checks, not a full notebook reproduction.
# Run with Python 3 and NumPy: python Review_support/verify_companion.py
# Snapshot: hamamh66/uvif-cognitive-equilibrium, commit 2d33c2158b24b17b4c4697d39a7d770e9712979e
import json,itertools
from pathlib import Path
import numpy as np
j=json.loads((Path(__file__).resolve().parent / 'companion_snapshot.ipynb').read_text());ns={'np':np}
exec(''.join(j['cells'][4]['source']),ns)
EE,AA=ns['EE'],ns['AA']; envs=list(itertools.product(np.round(np.linspace(.2,1,9),3),np.round(np.linspace(.1,.9,5),3),[5,20,60,150]))
threshold=.15; bound=0.; records=[];h1matches=0
for R,T,H in envs:
 base=ns['f_epistemic'](EE)+ns['f_action'](EE,AA)-ns['f_drag'](EE,R)-ns['f_sustain'](EE,AA,R,H)
 loss=ns['f_protect'](EE,AA,T)
 fixed_weight_score=base-loss
 h1matches+=np.argmax(fixed_weight_score)==np.argmax(ns['uvif_objective'](EE,AA,R,T,H))
 feasible=loss<=threshold;best=np.max(base[feasible]);violation=np.maximum(loss-threshold,0)
 if np.any(~feasible):bound=max(bound,float(np.max((base[~feasible]-best)/violation[~feasible])))
 records.append((base,loss,feasible))
coef=max(23.0,bound+1);matches=0
for base,loss,feasible in records:
 hard=np.argmax(np.where(feasible,base,-np.inf));soft=np.argmax(base-coef*np.maximum(loss-threshold,0));matches+=hard==soft
result={'environment_count':len(envs),'H1_state_aware_fixed_unit_weights_exact_matches':int(h1matches),'H3_constructive_finite_hinge_coefficient':coef,'H3_exact_grid_policy_matches':int(matches),'scope':'Constructive audit on the 180 declared environments and the 51x51 policy grid; not a held-out fitted comparison or proof for continuous policies.'}
(Path(__file__).resolve().parent / 'comparator_audit.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
