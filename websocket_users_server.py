import asyncio
import websockets
from websockets import ServerConnection

async def echo(websocket: ServerConnection):
    async for message in websocket:
        for _ in range(1, 6):
            print(f"{_} Получено сообщение от пользователя: {message}")
            await websocket.send(message)

async def main():
    server = await websockets.serve(echo, "localhost", 8765)
    print("Websocket server start at ws.")
    await server.wait_closed()

asyncio.run(main())
