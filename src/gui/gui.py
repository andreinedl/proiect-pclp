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
ui.title('Capitanul Pitonescu')

#app.on_startup(lambda: pyi_splash.close())

def start():
    ui.run(native=True, reload=False, port=openport)