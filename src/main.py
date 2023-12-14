from gui import gui
import spacy
if(spacy.util.is_package("en_core_web_sm") == False):
    spacy.cli.download("en_core_web_sm")
    
if __name__ == '__main__':
    gui.start()
