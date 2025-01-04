import uvicorn
import sys
import os
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from textSummarizer.pipeline.prediction import PredictionPipeline



app = FastAPI()

# Set up static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="pages")

@app.get("/", response_class=HTMLResponse, tags=["authentication"])
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/train", response_class=HTMLResponse)
async def training(request: Request):
    try:
        # Trigger training script
        os.system("python main.py")
        return templates.TemplateResponse("train.html", {"request": request, "message": "Training successful !!"})
    except Exception as e:
        return templates.TemplateResponse("train.html", {"request": request, "message": f"Error Occurred: {e}"})

@app.post("/predict", response_class=HTMLResponse)
async def predict_route(request: Request, text: str = Form(...)):
    try:
        obj = PredictionPipeline()
        summary = obj.predict(text)
        return templates.TemplateResponse("predict.html", {"request": request, "input_text": text, "summary": summary})
    except Exception as e:
        return templates.TemplateResponse("predict.html", {"request": request, "error": str(e)})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
