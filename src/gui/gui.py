from nicegui import ui, context, app
from typing import List, Tuple
import webview
import socket
import sys
import threading
#import pyi_splash

#Import chatbot function
sys.path.append("..")
from ai.chat import getResponse


with socket.socket() as s:
    s.bind(('',0))
    openport=s.getsockname()[1]
    
#NiceGUI
################
@ui.page('/')
def main():

    messages: List[Tuple[str, str]] = []
    thinking: bool = False

    @ui.refreshable
    def chat_messages() -> None:
        for name, text in messages:
            ui.chat_message(text=text, name=name, sent=name == 'Utilizator')
        if thinking:
            ui.spinner(size='5rem').classes('self-center')
        if context.get_client().has_socket_connection:
            ui.run_javascript('window.scrollTo(0, document.body.scrollHeight)')

    async def send() -> None:
        nonlocal thinking
        message = text.value
        messages.append(('Utilizator', text.value))
        thinking = True
        text.value = ''
        chat_messages.refresh()

        response = await getResponse(message)
        messages.append(('Pitonescu', response))
        thinking = False
        chat_messages.refresh()

    anchor_style = r'a:link, a:visited {color: inherit !important; text-decoration: none; font-weight: 500}'
    ui.add_head_html(f'<style>{anchor_style}</style>')

    # the queries below are used to expand the contend down to the footer (content can then use flex-grow to expand)
    ui.query('.q-page').classes('flex')
    ui.query('.nicegui-content').classes('w-full')

    with ui.tabs().classes('w-full') as tabs:
        chat_tab = ui.tab('Chat')
    with ui.tab_panels(tabs, value=chat_tab).classes('w-full max-w-2xl mx-auto flex-grow items-stretch'):
        with ui.tab_panel(chat_tab).classes('items-stretch'):
            chat_messages()
  
    with ui.footer().classes('bg-white'), ui.column().classes('w-full max-w-3xl mx-auto my-6'):
        with ui.row().classes('w-full no-wrap items-center'):
            placeholder = 'Introdu mesajul...'
            text = ui.input(placeholder=placeholder).props('rounded outlined input-class=mx-3') \
                .classes('w-full self-center').on('keydown.enter', send)

################

app.on_startup(lambda: pyi_splash.close())
def start():
    ui.run(native=True, reload=False, port=openport, title='Capitanul Pitonescu')
