from PIL import Image
import numpy as np
def inspect_image(path,false_accept_cost=10.0,false_reject_cost=3.0):
 img=Image.open(path).convert("RGB").resize((256,256));a=np.asarray(img,dtype=np.float32)/255.0;g=a.mean(axis=2)
 dx=np.abs(g[:,1:]-g[:,:-1]).mean();dy=np.abs(g[1:,:]-g[:-1,:]).mean()
 texture=float(min(1,(dx+dy)*7));contrast=float(min(1,g.std()*3))
 ratio=false_accept_cost/max(.001,false_reject_cost)
 threshold=float(max(.30,min(.70,.58-.06*np.log10(max(1,ratio)))))
 score=float(max(0,min(1,.65*texture+.35*contrast)))
 confidence=float(max(.50,min(.99,abs(score-threshold)*1.8+.50)))
 if abs(score-threshold)<=.08: decision="Human Review";reason="Borderline confidence near the calibrated decision threshold."
 elif score>threshold: decision="Fail";reason="Image irregularity score is above the calibrated threshold."
 else: decision="Pass";reason="Image remains below the calibrated defect threshold."
 return decision,confidence,score,threshold,reason