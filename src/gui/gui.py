from nicegui import ui, context, app
from typing import List, Tuple
import webview
import socket
import sys
import threading

#Importare modul AI
sys.path.append("..")
from ai.chat import getResponse

#Gasire port random pentru interfata web
with socket.socket() as s:
    s.bind(('',0))
    openport=s.getsockname()[1]

    messages: List[Tuple[str, str]] = []
    
ui.query('.nicegui-content').classes('w-full')
initialMessage: bool = False #Afisare mesaj initial, fals daca nu a mai fost afisat

## GUI ##
@ui.page('/')
def main():
    @ui.refreshable    
    def chat_messages() -> None:
        global initialMessage
        if(initialMessage==False):
            messages.append(('Capitanul Pitonescu', 'Salut, sunt Capitanul Pitonescu! Cum te pot ajuta?'))
            initialMessage = True
            
        for name, text in messages:
            ui.chat_message(text=text, name=name, sent=name == 'Utilizator').classes('m-4')
        if context.get_client().has_socket_connection:
            ui.run_javascript("$('#c11').animate({scrollTop: $('#c10').get(0).scrollHeight}, 2000);") ## Se foloseste de jQuery, id-ul div-ului pt chat fiind c11 

    # Functie pentru apelarea functiei getResponse din modulul AI + adaugare mesaje
    async def send() -> None:
        if(text.value==''):
            ui.notify('Nu ai introdus niciun mesaj!', type='error')
        else:
            message = text.value
            messages.append(('Utilizator', text.value))
            text.value = ''
            chat_messages.refresh()

            response = await getResponse(message)
            messages.append(('Pitonescu', response))
            chat_messages.refresh()
            
    #Includere jQuery
    ui.add_body_html('<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>')
    
    #Setare Dark Mode ca default
    darkMode = ui.dark_mode()
    darkMode.enable()
            
    with ui.splitter(limits=[10, 10], value=10).classes('w-full h-full fixed') as splitter:
        with splitter.before:
            with ui.tabs().props('vertical') as tabs:
                chat = ui.tab('Chat', icon='chat')
            ui.button(icon='light_mode', on_click=lambda: darkMode.toggle()).classes('mb-8')
        with splitter.after:
            with ui.tab_panels(tabs, value=chat).props('vertical').classes('w-full items-stretch flex-grow'):
                with ui.tab_panel(chat).classes('items-stretch'):
                    with ui.column().classes('w-fill h-[85vh] items-stretch flex-grow shrink overflow-y-auto'):
                        chat_messages()
                    with ui.column().classes('w-full h-[15vh]'):
                        with ui.row().classes('w-full border-r-8 border-transparent'):
                            placeholder = 'Introdu mesajul...'
                            text = ui.input(placeholder=placeholder).props('rounded outlined input-class=mx-3').classes('w-full self-center border-b-8 border-transparent').on('keydown.enter', send)

                
def start():
    ui.run(native=True, reload=False, port=openport, title='Capitanul Pitonescu', window_size=(1200, 600)) # Native mode - mod window, nu ca webpage
