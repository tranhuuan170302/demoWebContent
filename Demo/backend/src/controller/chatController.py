# controllers/chatbot_controller.py
# from models.message_model import save_message, get_all_messages
from starlette.responses import JSONResponse
from sevices.chatService import ChatService
from starlette.requests import Request

chat_service = ChatService()
async def respond_to_message(request : Request):
    data = await request.json()
    print('USE MESSAGE: ' , data.get('message'))
    # Logic phản hồi đơn giản
    result = await chat_service.processChatMessage(data.get('message'))
    return JSONResponse({"response": result})

