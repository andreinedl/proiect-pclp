from nicegui import ui, app
import webview
import socket
import sys
import threading
#import pyi_splash

with socket.socket() as s:
    s.bind(('',0))
    openport=s.getsockname()[1]

#NiceGUI 
ui.label('Hello NiceGUI!')
ui.chat_message('Hi',
                name='Bianca',
                stamp='now',
                avatar='https://robohash.org/ui')

ui.chat_message('Hello there!',
                name='Capitanul Pitonescu',
                stamp='now',
                avatar='https://robohash.org/ui')

#app.on_startup(lambda: pyi_splash.close())

ui.run(native=True, reload=False, port=openport)