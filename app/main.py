from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from .rag import get_rag_response, detect_preference

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def get_chat_page():
    with open("static/index.html") as f:
        return HTMLResponse(content=f.read())

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    query = data.get("query", "")
    detect_preference(query)  # Store preferences if detected
    response = get_rag_response(query)
    return {"response": response}