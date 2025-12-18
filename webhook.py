from fastapi import APIRouter
from pydantic import BaseModel
from chatbot.engine import chatbot_reply

router = APIRouter()

class WebhookRequest(BaseModel):
    message: str
    phone: str | None = None   # optionnel

@router.post("/webhook")
async def webhook(data: WebhookRequest):
    reply = chatbot_reply(data.message)
    return {
        "reply": reply,
        "phone": data.phone
    }
