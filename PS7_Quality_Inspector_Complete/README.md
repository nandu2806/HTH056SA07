# PS-07 Complete Full-Stack Website
## Includes
- React + Vite frontend
- FastAPI Python backend
- SQLite database created automatically
- Image upload
- Laptop/mobile camera capture
- Pass / Fail / Human Review
- Confidence, defect score and calibrated threshold
- Inspection history

## Run backend
cd backend
python -m venv .venv
Windows: .venv\\Scripts\\activate
macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000

## Run frontend
Open another terminal:
cd frontend
npm install
npm run dev
Then open the URL shown by Vite, normally http://localhost:5173

## Database
SQLite file `backend/quality_inspector.db` is generated automatically.

## Important
The included detector is a working prototype heuristic, not a trained industrial defect model. For a stronger hackathon submission, replace `detector.py` with a validated manufacturing-defect model and document false-accept/false-reject calibration.