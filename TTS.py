# Import the required module for text 
# to speech conversion
from gtts import gTTS
from mutagen.mp3 import MP3
# This module is imported so that we can 
# play the converted audio
import os


def readTextFile(InputFilePath):
    text_array = []
    with open(InputFilePath) as my_file:
        for line in my_file:
            text_array.append(line)
            #print(line)
    return text_array
    txtarry_length = len(text_array)
    #print("TextFile Length : ",txtarry_length)


def GetTTSOutput(InputText, OutputFilePath, Lang ='en'):
    # The text that you want to convert to audio
    # mytext = 'Hello I'm Computer'
    mytext = InputText
      
    # Language in which you want to convert
    language = Lang
      
    # Passing the text and language to the engine, 
    # here we have marked slow=False. Which tells 
    # the module that the converted audio should 
    # have a high speed
    myobj = gTTS(text=mytext, lang=language, slow=False)
      
    # Saving the converted audio in a mp3 file named
    # welcome 
    # myobj.save("welcome.mp3")
    myobj.save(OutputFilePath)
      
    # Playing the converted file
    # os.system("mpg321 welcome.mp3")
 
def Getmusicduration(InputFilePath):
    audio = MP3(InputFilePath)
    #print(audio.info.length) 
    return(audio.info.length)
    
def TriggerTTSOut(text_array, OutputPath):
    txtarry_length = len(text_array)
    pathtomp3file = []
    mp3Length = []
    for i in range(txtarry_length):
        #print(OutputPath + "\\" + str(i) + ".mp3")
        #print(text_array[i])
        if text_array[i] != '\n':
            pathtomp3file.append(OutputPath + "\\" + str(i) + ".mp3")
            GetTTSOutput(text_array[i], OutputPath + "\\" + str(i) + ".mp3", Lang ='en')
            mp3Length.append(Getmusicduration(OutputPath + "\\" + str(i) + ".mp3"))
        else:
            pathtomp3file.append("None")
            mp3Length.append(1)
            #print("Empty Line")
    return pathtomp3file, mp3Length 
