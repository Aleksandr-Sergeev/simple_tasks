import sys
import asyncio
from websockets import connect


class EchoWebsocket:
    def __await__(self):
        # see: http://stackoverflow.com/a/33420721/1113207
        return self._async_init().__await__()

    async def _async_init(self):
        self._conn = connect("wss://echo.websocket.org")
        self.websocket = await self._conn.__aenter__()
        return self

    async def close(self):
        await self._conn.__aexit__(*sys.exc_info())

    async def send(self, message):
        await self.websocket.send(message)

    async def receive(self):
        return await self.websocket.recv()


async def main():
    echo = await EchoWebsocket()
    try:
        await echo.send("Hello!")
        print(await echo.receive())  # "Hello!"
    finally:
        await echo.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())