from typing import Annotated
from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from questionsGenerator import questionsGenerator
from fastapi.responses import HTMLResponse



app = FastAPI()

templates = Jinja2Templates(directory="templates")

#repsonse class defines the type of response returned by the endpoint. Can be HTMLResponse, JSONResponse, etc.
@app.get("/home", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request}) #request: Request is passed so Jinja2 can access it in your template.
``

# #request contains headers, cookies, query parameters, and other information about the HTTP request.

# @app.post("/generate_questions")
# async def login(url: Annotated[str, Form()], role: Annotated[str, Form()], input_str: Annotated[str, Form()]):
#     questions = questionsGenerator(url, role, input_str).generateListeningTest()
#     return questions
