from PyPDF2 import PdfWriter
import pyttsx3

class Pdf_Merge:
    def __init__(self):
        self.voice_setup()
    def voice_setup(self):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice',voices[1].id)
        engine.setProperty('rate',150)
        engine.setProperty('volume',1.0)
        self.voice_command(engine)
    def voice_command(self,engine):
        engine.say('Welcome to PDF merger')
        engine.say('dont forget to follow Abhishek on Github')
        print('Welcome to PDF-Merger')
        engine.runAndWait()


def main():
    pd = Pdf_Merge()
main()