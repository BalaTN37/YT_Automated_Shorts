from TTS import *
from handleSrt import *
from music import *
from videoEdit import *
from random import randrange
import glob
    
#User Input 

print(("1-TTS, 2-Merge Videos, 3-Replace audio in loop"))
print(("4-Replace audio wih 90deg, 5-Port2LandScape, 6-Stabilizevideo "))
print(("7-SplitVideos, 8-Make it 9_16, 9-Convert 16_9 2 9_16 : Split to Audio"))
print((""))

UserChoice = int(input("Enter Input : "))
#Disabled for development
#UserChoice = 5
print("UserChoice : ", UserChoice)

if(UserChoice==1): #TTS Merge Audio
    #noOfVideo = input("Enter no of videos to be created :") #Disabled for development
    noOfVideo = 1
    inputVideo = "D:\\GIT\\TTS\\16_9_Inverse_5.mp4"

    inputTxtFile_array = []
    for i in range(int(noOfVideo)):
        #temp_pathtotxtfile = input("Enter Path to File ")   #Disabled for development
        temp_pathtotxtfile = "D:\GIT\TTS\input_text.txt"
        inputTxtFile_array.append(temp_pathtotxtfile)

    #OutputPath = input("Enter OutputPath :") #Disabled for development
    OutputPath = "D:\GIT\TTS\output"
    #print("Received File Paths : ", inputTxtFile_array)
    #End of User Input 

    for i in range(int(noOfVideo)):
        text_array = readTextFile(inputTxtFile_array[i])
        if not os.path.exists(OutputPath+"\\"+str(i)):
            os.makedirs(OutputPath+"\\"+str(i))
        pathtomp3file, mp3Length = TriggerTTSOut(text_array,OutputPath+"\\"+str(i))
        increasesoundvolume(pathtomp3file)
        print("Input Texts", text_array)
        print("Path to mp3 File", pathtomp3file)
        print("mp3 length", mp3Length)

    for i in range(int(noOfVideo)):
        createSubtitle(mp3Length, text_array, OutputPath, i)
        mergeSubtitle(inputVideo, OutputPath+"\\Output_"+str(i)+".srt", OutputPath, i)
        mergeMP3toVideo(OutputPath+"\output_"+str(i)+".mp4", pathtomp3file, mp3Length, OutputPath, i)

elif(UserChoice == 2):
    noOfVideo = input("Enter no of videos to be merged :")
    #OutputPath = input("Enter OutputPath :") #Disabled for development
    OutputPath = "D:\GIT\TTS\output"
    OutputPath_TxtFilePath = OutputPath + "inputVideoList.txt"
    f= open(OutputPath_TxtFilePath ,"w+")
    for i in range(int(noOfVideo)):
        inputTempFilePath = input("Enter File Path : ")
        inputTempFilePath = "file '" + inputTempFilePath + "'"
        f.write(inputTempFilePath + "\n")        
        #print(inputTempFilePath)
    f.close()
    mergeVideo(OutputPath_TxtFilePath,OutputPath)
    
elif(UserChoice == 3 or UserChoice == 4):            
    OutputPath = "D:\GIT\TTS\output"
    inPutaudioPath = input("Enter audio Path :")
    InputvideoPath = input("Enter video Path :")
    OutFilePath = mergeAudioVideo(inPutaudioPath, InputvideoPath, OutputPath)
    if(UserChoice == 4):
        ChangePortrait2LandScape(OutFilePath, OutputPath)
    #mergevideos()
    #Burn Subtitle

elif(UserChoice == 5):
    InputvideoPath = input("Enter video Path :")
    OutputPath = "D:\GIT\TTS\output"
    ChangePortrait2LandScape(InputvideoPath,OutputPath)
    
elif(UserChoice == 6):
    InputvideoPath = input("Enter video Path :")
    OutputPath = "D:\GIT\TTS\output"
    StabilizeVideo(InputvideoPath, OutputPath)
    
elif(UserChoice == 7):
    InputvideoPath = input("Enter video Path :")
    OutputPath = "D:\GIT\TTS\output"
    SplitVideo(InputvideoPath, OutputPath)

elif(UserChoice == 8):
    InputvideoPath = input("Enter video Path :")
    OutputPath = "D:\GIT\TTS\output"    
    Makeit9_16(InputvideoPath, OutputPath)
    
elif(UserChoice == 9): 
    HiberFlg = 0
    HiberFlg=int(input("Do you wish to Hibernate on Completion : 1-yes"))

    InputvideoPath=[]
    n=int(input("Number of elements in array:"))
    for i in range(0,n):
       l=(input())
       InputvideoPath.append(l)
    print(InputvideoPath)
    inPutaudioPath = []   
    for file in glob.glob("D:\GIT\TTS\Audio\*.mp3"):
        inPutaudioPath.append(file)
    # inPutaudioPath.append("D:\\GIT\\TTS\\NightLetmeSlowdown.mp3")
    # inPutaudioPath.append("D:\\GIT\\TTS\\BilliEllish.mp3")
    # inPutaudioPath.append("D:\\GIT\\TTS\\BoyWithUkeToxic.mp3")
    # inPutaudioPath.append("D:\\GIT\\TTS\\canwekissforever.mp3")
    # inPutaudioPath.append("D:\\GIT\\TTS\\Cradles.mp3")
    # inPutaudioPath.append("D:\\GIT\\TTS\\DuncanLaurence.mp3")
    # inPutaudioPath.append("D:\\GIT\\TTS\\Hymns.mp3")
    # inPutaudioPath.append("D:\\GIT\\TTS\\IamRider.mp3")
    # inPutaudioPath.append("D:\\GIT\\TTS\\IndustryBaby.mp3")
    # inPutaudioPath.append("D:\\GIT\\TTS\\letmedownSlowVer.mp3")
    # inPutaudioPath.append("D:\\GIT\\TTS\\LetmeDownWithTamilSOng.mp3")
    # inPutaudioPath.append("D:\\GIT\\TTS\\MiddleofNight.mp3")
    # inPutaudioPath.append("D:\\GIT\\TTS\\NightLetmeSlowdown.mp3")
    # inPutaudioPath.append("D:\\GIT\\TTS\\OneDance.mp3")
    # inPutaudioPath.append("D:\\GIT\\TTS\\Panda.mp3")
    # inPutaudioPath.append("D:\\GIT\\TTS\\Petta.mp3")
    # inPutaudioPath.append("D:\\GIT\\TTS\\SigmaRule.mp3")
    # inPutaudioPath.append("D:\\GIT\\TTS\\Stereo.mp3")
    # inPutaudioPath.append("D:\\GIT\\TTS\\SugarBrownies.mp3")
    # inPutaudioPath.append("D:\\GIT\\TTS\\unstoppablesia.mp3")
    # inPutaudioPath.append("D:\\GIT\\TTS\\xxxtentacion.mp3")
    # inPutaudioPath.append("D:\\GIT\\TTS\\nolie.mp3")
    
    print(inPutaudioPath)
    print(len(inPutaudioPath))
    print((randrange((int(len(inPutaudioPath))))))
    
    for i in range(0,n):
        OutputPath = "D:\GIT\TTS\output"    
        OutputFilePath = Makeit9_16(InputvideoPath[i], OutputPath)
        OutputFolderPath1 = SplitVideo(OutputFilePath, OutputPath)
        #OutputFolderPath1 = "D:\\GIT\\TTS\\output\\Out9_16_supe"
        res = []
        # Iterate directory
        for path in os.listdir(OutputFolderPath1):
            # check if current path is a file
            if os.path.isfile(os.path.join(OutputFolderPath1, path)):
                res.append(OutputFolderPath1 + "\\" + path)
        print("Files Path ")
        print(res)
        for j in range(int(len(res))):
            mergeAudioVideo(inPutaudioPath[(randrange((int(len(inPutaudioPath)))))], res[j], OutputFolderPath1 + "\\OutputAudioMerged")
            
    if(HiberFlg == 1):
        print("Hibernating")
        os.system("shutdown.exe /h")


# OutputMP3FilePath = "D:\\GIT\\TTS\\output\\trymusic.mp3"
# GetTTSOutput("Hello,    I'm Computer", OutputMP3FilePath, Lang ='en')
# Getmusicduration(OutputMP3FilePath)