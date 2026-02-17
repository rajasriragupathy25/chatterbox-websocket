from fastapi import FastAPI, WebSocket
import uvicorn

app = FastAPI()

@app.get("/")
async def home():
    return {"status": "Chatterbox WebSocket Server is active"}

@app.websocket("/ws")
async def chat_socket(websocket: WebSocket):
    await websocket.accept()
    print("A client has connected!")

    try:
        while True:
            data = await websocket.receive_text()
            print("Message from client:", data)
            response = f"Server received -> {data}"
            await websocket.send_text(response)

    except Exception:
        print("Client connection closed.")

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
