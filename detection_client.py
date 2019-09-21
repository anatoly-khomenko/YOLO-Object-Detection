import cv2
import asyncio
import websockets


video = cv2.VideoCapture(0)
video.set(cv2.CAP_PROP_FRAME_WIDTH, 424)
video.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)


async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        while True:
            check, frame = video.read()
            print(frame.shape)
            print(len(frame))
            buffer = frame.tobytes()
            print(len(buffer))
            await websocket.send(buffer)
            # print(f"> {name}")

            greeting = await websocket.recv()
            print(greeting)
        video.release()


asyncio.get_event_loop().run_until_complete(hello())
asyncio.get_event_loop().run_forever()

