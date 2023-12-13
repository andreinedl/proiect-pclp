from chatterbot import ChatBot, storage
from chatterbot.trainers import ListTrainer
chatbot = ChatBot('Capitanul Pitonescu')
trainer = ListTrainer(chatbot)
response = chatbot.get_response("intrebare")
print(response)
