from chatterbot import ChatBot, storage, corpus
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from pathlib import Path, PurePosixPath
import os
chatbot = ChatBot('Capitanul Pitonescu')
trainer = ChatterBotCorpusTrainer(chatbot)

enModels = str(PurePosixPath(Path(os.getcwd()))) + "/src/ai/models/en/"

trainer.train(
   enModels
)

while True:
    intrebare = input("Intrebare: ")
    response = chatbot.get_response(intrebare)
    print(response)
    
#doTrain()