#from gui import gui
import spacy
if(spacy.util.is_package("en_core_web_sm") == True):
    spacy.cli.download("en_core_web_sm")
else:
    print("en_core_web_sm is already installed")

#if __name__ == '__main__':
 #   gui.start()
