from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Dict, Any, Optional
import logging

from src.agents.basic import AgentBasic
from src.agents.tools import AgentWithTools, OrderDetails
from src.agents.isRude import AgentIsRude

logger = logging.getLogger(__name__)
router = APIRouter()

class BasicRequest(BaseModel):
    message: str = Field(
        description="Сообщение для базового агента",
        examples=[
            "Привет, как дела?",
            "Что ты умеешь делать?",
            "Расскажи о себе"
        ]
    )

class ToolsRequest(BaseModel):
    message: str = Field(
        description="Сообщение для агента с инструментами",
        examples=["Где мой заказ #12345?", "Когда доставят заказ #67890?"]
    )
    order_id: str = Field(
        description="Идентификатор заказа",
        examples=["#12345", "#67890"]
    )
    customer_name: str = Field(
        description="Имя клиента",
        examples=["Иван Петров", "Петр Иванов"]
    )
    email: str = Field(
        description="Email клиента",
        examples=["ivan@example.com", "petr@example.com"]
    )

class IsRudeRequest(BaseModel):
    message: str = Field(
        description="Сообщение для проверки на грубость",
        examples=[
            "Ты тупой бот!",
            "Спасибо за помощь!",
            "Я очень расстроен качеством обслуживания"
        ]
    )

class MessageResponse(BaseModel):
    response: str
    metadata: Optional[Dict[str, Any]] = None

@router.post("/chat/basic", response_model=MessageResponse)
async def basic_chat(request: BasicRequest):
    """Чат с базовым агентом"""
    try:
        response = await AgentBasic.run(request.message)
        return MessageResponse(response=str(response.data))
    except Exception as e:
        logger.error(f"Ошибка при обработке сообщения: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/chat/tools", response_model=MessageResponse)
async def tools_chat(request: ToolsRequest):
    """Чат с агентом для проверки статуса заказа"""
    try:
        order_details = OrderDetails(
            order_id=request.order_id,
            customer_name=request.customer_name,
            email=request.email
        )
        response = await AgentWithTools.run(
            user_prompt=request.message,
            deps=order_details
        )
        return MessageResponse(
            response=str(response.data.response),
            metadata={
                "needs_escalation": response.data.needs_escalation,
                "follow_up_required": response.data.follow_up_required,
                "sentiment": response.data.sentiment
            }
        )
    except Exception as e:
        logger.error(f"Ошибка при обработке сообщения: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/chat/isrude", response_model=MessageResponse)
async def isrude_chat(request: IsRudeRequest):
    """Проверка сообщения на грубость"""
    try:
        response = await AgentIsRude.run(request.message)
        return MessageResponse(
            response="Анализ сообщения завершен",
            metadata={
                "is_offensive": response.data.is_offensive,
                "sentiment": response.data.sentiment
            }
        )
    except Exception as e:
        logger.error(f"Ошибка при обработке сообщения: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e)) 