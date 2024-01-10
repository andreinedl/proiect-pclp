from gui import gui as gui
import spacy
if(spacy.util.is_package("en_core_web_sm") == False):
    spacy.cli.download("en_core_web_sm")
    
if(spacy.util.is_package("ro_core_news_sm") == False):
    spacy.cli.download("ro_core_news_sm")
    
if __name__ == '__main__':
    gui.start()
