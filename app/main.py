from fastapi import FastAPI

from app.api.endpoints import users, budget, pdf, email, websocket

app = FastAPI(title="Chatbot API")

# Registrar los routers de los módulos
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(budget.router, prefix="/budget", tags=["Budget"])
app.include_router(pdf.router, prefix="/pdf", tags=["PDF"])
app.include_router(email.router, prefix="/email", tags=["Email"])
app.include_router(websocket.router, prefix="/ws", tags=["WebSocket"])


