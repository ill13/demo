import os
import arel
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

DEBUG=True
stage = os.environ.get('STAGE','dev')



app = FastAPI()
templates = Jinja2Templates("templates") # folder where your templates are stored
app.mount("/static", StaticFiles(directory="static"), name="static")

#static = Jinja2Templates("static")

#if _debug := os.getenv("DEBUG"):
if DEBUG := True:
    hot_reload = arel.HotReload(paths=[arel.Path(".")])
    app.add_websocket_route("/hot-reload", route=hot_reload, name="hot-reload")
    app.add_event_handler("startup", hot_reload.startup)
    app.add_event_handler("shutdown", hot_reload.shutdown)
    #templates.env.globals["DEBUG"] = _debug
    templates.env.globals["DEBUG"] = DEBUG
    templates.env.globals["hot_reload"] = hot_reload


@app.get("/")

def index(request: Request):
    return templates.TemplateResponse("index.html",context={"request":request,'title':'Demo0'})

# def index():
#     return{"hello":"world"}