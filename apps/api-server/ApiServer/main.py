from fastapi import FastAPI, WebSocket
import redis.asyncio as redis 

app = FastAPI()

# Redis pub-sub setup
r = redis.Redis(host="redis", port=6379)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.websocket("ws")
async def websocket_endpoint(websocket: WebSocket): 
    await websocket.accept()
    pubsub = r.pubsub()
    await pubsub.subscribe("events")
    try: 
        while True:
            message = await pubsub.get_message(ignore_subscribe_messages=True, timeout=1.0)
            if message: 
                await websocket.send_text(message["data"].decode())
    except Exception as e:
        print("Websocket disconnect", e)
    finally:
        await pubsub.unsubscribe("events")