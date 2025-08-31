from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from api.chat.models import ChatMessagePayload, ChatMessage
from api.db import get_session

router = APIRouter()

@router.get("/")
def chat_health():
    return {"status": "ok"}

@router.get("/recent/")
def chat_list_messages(session: Session = Depends(get_session)):
    query = select(ChatMessage) # sql -> query
    results = session.exec(query).fetchall()[:10]
    return results 

@router.post("/", response_model=ChatMessage)
def chat_create_message(
    payload: ChatMessagePayload,
    session: Session = Depends(get_session)
):
    data = payload.model_dump()
    obj = ChatMessage.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj