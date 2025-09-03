from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from api.chat.models import ChatMessagePayload, ChatMessage, ChatMessageListItem
from api.db import get_session
from api.chat.ai_service import llm_base

router = APIRouter()

@router.get("/")
def chat_health():
    return {"status": "ok"}

@router.post("/ask-ai")
def get_ai_response(
    payload: ChatMessagePayload,
):
    
    response = llm_base.invoke(payload.message)
    return response.content

@router.get("/recent/", 
            response_model = List[ChatMessageListItem],
            description = "The most recent prompts users provided",
            status_code = status.HTTP_200_OK 
            )
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