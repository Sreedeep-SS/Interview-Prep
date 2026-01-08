
---

## `cheatsheets/python/fastapi.md`

# FastAPI — Quick Cheatsheet

## Minimal app
```python
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
app = FastAPI()

class Item(BaseModel):
    id: int
    name: str

@app.post("/items")
async def create_item(item: Item):
    return item
```
#### run: uvicorn main:app --reload --port 8000


# WebSocket

```python
from fastapi import WebSocket
@app.websocket("/ws")
async def chat(ws: WebSocket):
    await ws.accept()
    data = await ws.receive_text()
    await ws.send_text(f"echo: {data}")
```
