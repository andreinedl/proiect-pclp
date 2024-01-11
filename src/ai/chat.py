from am_i_connected import CheckThereIsConnection
from pathlib import Path
import asyncio
import g4f

async def askChat(message):
    try:
        response = await g4f.ChatCompletion.create_async(
            model=g4f.models.default,
            messages=[{"role": "user", "content": message}],
            provider=g4f.Provider.GeekGpt,
            timeout=300,
        )
        return response
    except Exception as e:
        return 'Eroare! Te rog sa incerci din nou!'

async def getResponse(question):
    await asyncio.sleep(1)
    if CheckThereIsConnection():
        response = await askChat(question)
        return response
    else:
        response = "Nu exista o conexiune la internet! Te rog sa te conectezi la internet si sa incerci din nou!"
        return response