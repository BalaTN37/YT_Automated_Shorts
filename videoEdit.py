import os
import os.path
from os import path
import tempfile

def mergeVideo(OutputPath_TxtFilePath, OutputPath):
    temp_string = "ffmpeg -y -safe 0 -f concat -i \"" + OutputPath_TxtFilePath + "\" -c copy \"" + OutputPath + "\MergedVideo.mp4\""
    if(path.exists(OutputPath + "\MergedVideo.mp4")):
        if os.path.exists(OutputPath + "\MergedVideo_old.mp4"):
            os.remove(OutputPath + "\MergedVideo_old.mp4")
        os.rename(OutputPath + "\MergedVideo.mp4", OutputPath + "\MergedVideo_old.mp4")
    os.system(temp_string)
    print(temp_string)
    
def mergeAudioVideo(inPutaudioPath, InputvideoPath, OutputPath):
    if not(path.exists(OutputPath)):
        os.makedirs(OutputPath)
    tail = os.path.basename(InputvideoPath)
    k=0;
    if(path.exists(OutputPath + "\Out_" + str(k) + "_"  + tail)):
        k=k+1
        if(path.exists(OutputPath + "\Out_" + str(k) + "_"  + tail)):
            k=k+1
            if(path.exists(OutputPath + "\Out_" + str(k) + "_"  + tail)):
                k=0;
                os.remove(OutputPath + "\Out_" + str(k) + "_"  + tail)
                OutputPath = OutputPath + "\Out_" + str(k) + "_"  + tail
            else:
                if not os.path.exists(OutputPath):
                    os.makedirs(OutputPath)
                OutputPath = OutputPath + "\Out_" + str(k) + "_"  + tail
        else:
            if not os.path.exists(OutputPath):
                    os.makedirs(OutputPath) 
            OutputPath = OutputPath + "\Out_" + str(k) + "_"  + tail               
    else:
        if not os.path.exists(OutputPath):
            os.makedirs(OutputPath)
        OutputPath = OutputPath + "\Out_" + str(k) + "_"  + tail
        
    temp_string = "ffmpeg -y -i " + InputvideoPath +" -stream_loop -1 -i " + inPutaudioPath 
    temp_string = temp_string + " -map 0:v -map 1:a -c:v copy -shortest " + OutputPath
    os.system(temp_string)
    print(temp_string)
    return OutputPath
    
def ChangePortrait2LandScape(InputvideoPath, OutputPath):
    tail = os.path.basename(InputvideoPath)
    k=0;
    if(path.exists(OutputPath + "\OutPort2Land_" + str(k) + "_"  + tail)):
        k=k+1
        if(path.exists(OutputPath + "\OutPort2Land_" + str(k) + "_"  + tail)):
            k=k+1
            if(path.exists(OutputPath + "\OutPort2Land_" + str(k) + "_"  + tail)):
                k=0;
                os.remove(OutputPath + "\OutPort2Land_" + str(k) + "_"  + tail)
                OutputPath = OutputPath + "\OutPort2Land_" + str(k) + "_"  + tail
            else:
                if not os.path.exists(OutputPath):
                    os.makedirs(OutputPath)
                OutputPath = OutputPath + "\OutPort2Land_" + str(k) + "_"  + tail
        else:
            if not os.path.exists(OutputPath):
                    os.makedirs(OutputPath) 
            OutputPath = OutputPath + "\OutPort2Land_" + str(k) + "_"  + tail               
    else:
        if not os.path.exists(OutputPath):
            os.makedirs(OutputPath)
        OutputPath = OutputPath + "\OutPort2Land_" + str(k) + "_"  + tail
        
    temp_string = "ffmpeg -y -i " + InputvideoPath +" -vf " 
    temp_string = temp_string + "\"transpose=2\" " + OutputPath
    os.system(temp_string)
    print(temp_string)
    
# For the transpose parameter you can pass:

# 0 = 90CounterCLockwise and Vertical Flip (default)
# 1 = 90Clockwise
# 2 = 90CounterClockwise
# 3 = 90Clockwise and Vertical Flip
# Use -vf "transpose=2,transpose=2" for 180 degrees.

def StabilizeVideo(InputvideoPath, OutputPath):
    tail = os.path.basename(InputvideoPath)
    k=0;
    if(path.exists(OutputPath + "\OutStabilize_" + str(k) + "_"  + tail)):
        k=k+1
        if(path.exists(OutputPath + "\OutStabilize_" + str(k) + "_"  + tail)):
            k=k+1
            if(path.exists(OutputPath + "\OutStabilize_" + str(k) + "_"  + tail)):
                k=0;
                os.remove(OutputPath + "\OutStabilize_" + str(k) + "_"  + tail)
                OutputPath = OutputPath + "\OutStabilize_" + str(k) + "_"  + tail
            else:
                if not os.path.exists(OutputPath):
                    os.makedirs(OutputPath)
                OutputPath = OutputPath + "\OutStabilize_" + str(k) + "_"  + tail
        else:
            if not os.path.exists(OutputPath):
                    os.makedirs(OutputPath) 
            OutputPath = OutputPath + "\OutStabilize_" + str(k) + "_"  + tail               
    else:
        if not os.path.exists(OutputPath):
            os.makedirs(OutputPath)
        OutputPath = OutputPath + "\OutStabilize_" + str(k) + "_"  + tail    #https://gist.github.com/hlorand/e5012fa315dcfe358008cf1b4611c7e0    
    
    executiondirectory = os.getcwd()
    print(executiondirectory)
    
    temp_dir = tempfile.TemporaryDirectory()
    print(temp_dir.name)
    os.chdir(temp_dir.name)
    
    temp_string = "ffmpeg -i " + InputvideoPath + " -vf vidstabdetect=shakiness=7 -f null -"
    os.system(temp_string)   
    temp_string = "ffmpeg -i " + InputvideoPath + " -vf vidstabtransform=smoothing=30:zoom=5:input=\"transforms.trf\" " + OutputPath
    os.system(temp_string)  
    os.chdir(executiondirectory)
    temp_dir.cleanup()   
    print(temp_string)
    


def SplitVideo(InputvideoPath, OutputPath):
    tail = os.path.basename(InputvideoPath)
    sep = '.'
    tail = tail.split(sep, 1)[0]
    print(tail)
    OutputPath = OutputPath + "\\" + tail
    if not (path.exists(OutputPath)):
        os.makedirs(OutputPath)    
    
    temp_string = "ffmpeg -y -i " + InputvideoPath
    temp_string = temp_string + " -c copy -map 0 -segment_time 00:00:54 -f segment -reset_timestamps 1 "
    temp_string = temp_string + OutputPath + "\\Out%03d.mp4"
    os.system(temp_string)  
    print(temp_string)
    return OutputPath
   
   
def Makeit9_16(InputvideoPath, OutputPath):
    tail = os.path.basename(InputvideoPath)
    sep = '.'
    tail1 = tail.split(sep, 1)[0]
    print(tail)
    OutputPath = OutputPath + "\\" + "Out9_16_" + tail
    # if not (path.exists(OutputPath)):
        # os.makedirs(OutputPath)
        
    #temp_string = "ffmpeg -i " + InputvideoPath + " -vf \"pad=iw:2*trunc(iw*16/18):(ow-iw)/2:(oh-ih)/2,setsar=1\" -c:a copy "
    #temp_string = temp_string + OutputPath
    temp_string = "ffmpeg -y -i " + InputvideoPath + " -lavfi \"[0:v]scale=iw:2*trunc(iw*16/18),boxblur=luma_radius=min(h\,w)/20:luma_power=1:chroma_radius=min(cw\,ch)/20:chroma_power=1[bg];[bg][0:v]overlay=(W-w)/2:(H-h)/2,setsar=1\" "
    temp_string = temp_string + OutputPath
    #ffmpeg -i D:\Temp\Jul1\BVR_2022_07_01_08_33_53.mp4 -lavfi "[0:v]scale=iw:2*trunc(iw*16/18),boxblur=luma_radius=min(h\,w)/20:luma_power=1:chroma_radius=min(cw\,ch)/20:chroma_power=1[bg];[bg][0:v]overlay=(W-w)/2:(H-h)/2,setsar=1"  D:\GIT\TTS\output\1output.mp4
    #temp_string = "ffmpeg -y -i " + InputvideoPath + " -lavfi \"[0:v]scale=256/81*iw:256/81*ih,boxblur=luma_radius=min(h\,w)/40:luma_power=3:chroma_radius=min(cw\,ch)/40:chroma_power=1[bg];[bg][0:v]overlay=(W-w)/2:(H-h)/2,setsar=1,crop=w=iw*81/256\"  "
    #temp_string = temp_string + OutputPath
    os.system(temp_string) 
    print(temp_string)
    return OutputPath