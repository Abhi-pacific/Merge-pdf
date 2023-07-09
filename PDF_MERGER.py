from PyPDF2 import PdfWriter
import pyttsx3
import os

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
        print(r'format for entering the path D:\\rog_wall\\certificates')
        engine.runAndWait()
    def merger(self):
        merge = PdfWriter()
        print(os.getcwd())
        path = input('Enter the path of the folder : ')
        print(path)
        new_path = os.chdir(path)
        for file in os.listdir():
            if file.endswith('.pdf'):
                merge.append(file)
        merge.write('merged_pdf.pdf')
        merge.close()



def main():
    pd = Pdf_Merge()
    pd.merger()
main()