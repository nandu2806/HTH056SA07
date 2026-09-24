from fastapi import FastAPI,UploadFile,File,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import uuid
from database import init_db,add,all_rows
from detector import inspect_image
BASE=Path(__file__).parent;UPLOADS=BASE/"uploads";UPLOADS.mkdir(exist_ok=True)
app=FastAPI(title="PS-07 Quality Inspector API")
app.add_middleware(CORSMiddleware,allow_origins=["*"],allow_credentials=True,allow_methods=["*"],allow_headers=["*"])
init_db()
@app.get("/")
def root():return {"status":"online"}
@app.get("/api/health")
def health():return {"status":"healthy","database":"SQLite"}
@app.get("/api/inspections")
def inspections():return all_rows()
@app.post("/api/inspect")
async def inspect(image:UploadFile=File(...)):
 if not image.content_type or not image.content_type.startswith("image/"):raise HTTPException(400,"Only images are accepted")
 data=await image.read()
 if len(data)>10*1024*1024:raise HTTPException(413,"Image must be smaller than 10 MB")
 suffix=Path(image.filename or ".jpg").suffix or ".jpg";path=UPLOADS/(uuid.uuid4().hex+suffix);path.write_bytes(data)
 try:decision,confidence,score,threshold,reason=inspect_image(path)
 except Exception as e:raise HTTPException(422,str(e))
 i=add((image.filename or path.name,decision,confidence,score,threshold,reason))
 return {"id":i,"filename":image.filename,"decision":decision,"confidence":confidence,"defect_score":score,"threshold":threshold,"reason":reason}