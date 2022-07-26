import math
import os

def createSubtitle(mp3Length, text_array, OutputPath, i):
    print("Testing mp3Length",mp3Length)
    temp_string = OutputPath+"\\Output_"+str(i)+".srt"
    print(temp_string)
    f= open(temp_string ,"w+")
    microseconds = 500
    seconds = 0
    minutes = 0
    hours = 0
    offset_btwsubtitletxt = 1
    for j in range(int(len(text_array))):
        temp_string = str(i)
        f.write(str(j+1) + "\n")
        
        temp_string = str(hours) + ":" + str(minutes) + ":" + str(seconds) + "," + str(microseconds) + " --> "
        
        whole_second = math.floor(mp3Length[j])        
        print("Testing mp3Length[i]",mp3Length[i])
        frac = mp3Length[j] - whole_second      
        frac = frac*100
        whole_mircosecond = math.floor(frac)
        microseconds = microseconds + (whole_mircosecond*10)
        seconds = seconds + whole_second
        print("Testing Seconds",seconds)
        
        if(microseconds>999):
            microseconds = 0
            seconds = seconds +1
        if(seconds>59):
            seconds = 0
            minutes = minutes + 1
        if(minutes>59):
            minutes=0
            hours = hours +1

        temp_string = temp_string + str(hours) + ":" + str(minutes) + ":" + str(seconds) + "," + str(microseconds)
        f.write(temp_string + "\n")

        f.write(text_array[j])
        f.write("\n")


def mergeSubtitle(inputVideo, inputSubtitle, OutputPath, i):
    temp_string = "ffmpeg -y -i " + inputVideo + " -filter_complex "
    temp_string = temp_string + "\"subtitles=" + "output_" + str(i) + ".srt" + ":force_style='Alignment=10,BackColour=&H80000000,BorderStyle=3,Fontsize=10'\" " 
    temp_string = temp_string + OutputPath + "\output_" + str(i) +".mp4"
    print(temp_string)
    os.chdir(OutputPath)
    os.system(temp_string)
    #box.mp4 -filter_complex "subtitles=subtitle_trail.srt:force_style='Alignment=10,BackColour=&H80000000,BorderStyle=4,Fontsize=11'" output2.mp4
    #os.system("some_command < input_file | another_command > output_file")  
    #ffmpeg -i box.mp4 -filter_complex "subtitles=subtitle_trail.srt:force_style='Alignment=10,BackColour=&H80000000,BorderStyle=4,Fontsize=11'" output2.mp4