from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from database import logs_collection, reports_collection
from ai import analyze_log

app = FastAPI(title="LogAI", version="1.0")

# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve frontend files
app.mount("/static", StaticFiles(directory="../frontend"), name="static")

@app.get("/")
def home():
    return FileResponse("../frontend/index.html")

@app.get("/health")
def health():
    return {"status": "LogAI is running ✅"}

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    contents = await file.read()
    log_text = contents.decode("utf-8")
    analysis = analyze_log(log_text)
    logs_collection.insert_one({
        "filename": file.filename,
        "log_text": log_text,
        "analysis": analysis
    })
    return {"analysis": analysis}