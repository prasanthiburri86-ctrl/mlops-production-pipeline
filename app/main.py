from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.model_loader import predict

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict", response_class=HTMLResponse)
def make_prediction(
    request: Request,
    age: int = Form(...),
    salary: int = Form(...),
    experience: int = Form(...)
):
    result = predict(age, salary, experience)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "prediction": "Will Purchase" if result == 1 else "Won't Purchase"
        }
    )