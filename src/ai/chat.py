from chatterbot import ChatBot, storage, corpus
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from pathlib import Path, PurePosixPath
import asyncio
import os
chatbot = ChatBot('Capitanul Pitonescu', 
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        database_uri='sqlite:///src/ai/db/database.sqlite3', 
        logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch'
        ]
    )
trainer = ChatterBotCorpusTrainer(chatbot)

def doTrain():
    enModels = str(PurePosixPath(Path(os.getcwd()))) + "/src/ai/models/en/"
    trainer.train(
        enModels
    )

def runStandalone():
    while True:
        question = input("Intrebare: ")
        response = chatbot.get_response(question)
        print(response)

async def getResponse(question):
    await asyncio.sleep(1)
    response = f"{chatbot.get_response(question)}"
    return response
    
#doTrain()
#runStandalone()