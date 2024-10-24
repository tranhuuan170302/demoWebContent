from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from controller.chatController import respond_to_message
import uvicorn

async def homepage(request):
    return JSONResponse({"message": "Hello, World!"})

async def load_url(request):
    url = request.query_params.get("url", "")
    # Gọi hàm load_url ở đây nếu cần
    # clean_text = await load_url_function(url)
    return JSONResponse({"url": url})  # Trả về URL để kiểm tra

# Định nghĩa các route
routes = [
    Route("/chat", respond_to_message, methods=['GET'])
]

# Tạo ứng dụng Starlette
app = Starlette(routes=routes)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
