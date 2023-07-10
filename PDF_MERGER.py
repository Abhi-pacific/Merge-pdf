from PyPDF2 import PdfWriter
import pyttsx3
import os

class Pdf_Merge:
    def __init__(self):
        self.voice_setup()

    # Full setup for the voice
    def voice_setup(self):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice',voices[1].id)
        engine.setProperty('rate',150)
        engine.setProperty('volume',1.0)
        self.voice_command(engine)
    # Welcome voice 
    def voice_command(self,engine):
        engine.say('Welcome to PDF merger')
        engine.say('dont forget to follow Abhishek on Github')
        print('Welcome to PDF-Merger')
        engine.say('Please follow below instructions to merge your PDF')
        engine.runAndWait()
        print('\n\nCreate a folder with any name without space and special characters')
        print('Paste both the PDF file in that folder ')
        print('Syntax for the path is :')
        print(r'(D:\\rog_wall\\certificates)')
        self.merger(engine)
    # Merge code start from here
    def merger(self,engine):
        merge = PdfWriter()
        while True:
            for_exit =int(input('If you want to exit press 1 : '))
            # using 1 for exit in if condition
            if for_exit == 1:
                engine.say('Exiting... thank you for using me')
                engine.runAndWait()
                raise SystemExit('Thank you for using me')
            path = input('Enter the path of the folder : ')
            engine.say('Your entered path is ')
            print('Your entered path is :{:^8}'.format(path))
            try:
                os.chdir(path)
                for file in os.listdir():
                    if file.endswith('.pdf'):
                        merge.append(file)
                engine.say('Please Enter name for new file : ')
                engine.runAndWait()
                print('Please do not add .pdf in name')
                new_file_name = input('Please Enter name for new file ')
                merge.write(new_file_name+'.pdf')
                merge.close()
                engine.say('New PDF created, Thanks for using me')
                engine.runAndWait()
                raise SystemExit('Thanks you for using me')
            except FileNotFoundError:
                engine.say('I believe your entered path is wrong')
                engine.runAndWait()
                print('Wrong Path...')



def main():
    pd = Pdf_Merge()
main()