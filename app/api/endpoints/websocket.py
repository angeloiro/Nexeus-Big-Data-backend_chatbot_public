### **app/api/endpoints/websocket.py** (WebSocket para chat en tiempo real)
from fastapi import APIRouter, WebSocket, WebSocketDisconnect

router = APIRouter()

@router.websocket("/chat/{user_id}")
async def websocket_chat(websocket: WebSocket, user_id: str):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Recibido: {data}")
    except WebSocketDisconnect:
        print(f"Conexión cerrada con {user_id}")
