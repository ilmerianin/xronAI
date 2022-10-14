# -*- coding: utf-8 -*-
# ffmpeg скачать бинарный файл https://ffbinaries.com/downloads
#  в данной настройке с SD карты из кучи собирает на диске новый видео файл
#               отбирает по времени CreateListFile_SD_Mexico
#  03.06.22     собираент все в подряд  CreateListFile_SD_Rus 
#             сам создает пути которых нет


# video_to_gif(path): Проходит по папке и из файлов .mp4 делает .gif
         #import ffmpeg # для video_to_gif() возможно не установленна версия для  PYNHON 
#        
# add_mp4_in_list - Проходит по папке и из файлов .mp4 делает один с именем outFile = 'первый файл.mp4'
#               NamFileList = 'myListFile.txt' #имя временного файла списка в папке
#               pathMp4 = 'E:/DCIM/100GOPRO/'      #папка источник с .mp4
#               pathout = 'd:/Видео/дляЗагрузки/'  #папка получатель финального .mp4   
NamFileList = 'myListFile.txt' #имя временного файла списка в папке
pathMp4 = 'c:/DCIM/WID/'     # папка с файлами .mp4 для  сборки в один файл     
pathout = 'c:/DCIM/WID/Zagruz/' #  итоговый файл
outFile = 'outSumFile.mp4'



# delFile_fileList(pathNameList): # удаляет файлы из списка содержащегося в файле
#!pip install ffmpeg-python #работает
#import ffmpeg
     

import os
import subprocess  #работа с командной строкой

from pathlib import Path

path = "/storage/emulated/0/DCIM/GoPro-Exports" # путь к папке для преобразования .mp4 делает .gif

def video_to_gif(path):
    ''' # Проходит по папке и из файлов .mp4 делает .gif

        path - путь к папке в которой переделывать из файлов .mp4 делает .gif
    '''
    for file in os.listdir(path):
        if file.endswith((".mp4", ".MP4")):
            file_name = file.split(".")[0]
            gif_file = file_name + ".gif"
            
            stream = ffmpeg.input(f"{path}/{file}")
            stream = ffmpeg.filter(stream, "fps", fps=2)
            stream = ffmpeg.output(stream, f"{path}/{gif_file}")
            ffmpeg.run(stream)
            
        # else:
        #     print("Bad extension in the file!")



def CreateListFile(path, NamFileList, outFile):
    '''
        создаёт файл со списком видео файлов для ffmpeg
        берет все файлы мр4 из папки
        path - путь
        NamFileList = 'myListFile.txt' #имя временного файла списка в папке
        outFile = название файла вывода
    '''
    #pathN: Path = Path(path) # универсальный путь
    
    timelater =0
    
    try:
        flist = open(path + NamFileList, mode='w+')
    except OSError:
        print('Кака я та ошибка с открытием файла:',path + NamFileList )
        
    
    for iterfile in os.listdir(path):
        
        if iterfile.endswith((".mp4", ".MP4")):
                        
            file = path + iterfile
            sizef = os.path.getsize(file)/1000000
            
            if timelater ==0:
                timelater = os.path.getctime(file)
                
            dTime = os.path.getctime(file) - timelater
                                                          
            print(iterfile,':', sizef, 'mb')#, dTime , 'delta time')
            
            if  'outSumFile.mp4' in outFile: #выбор имени конечного файла
                outFile = iterfile
                            
            flist.write('file ' + file +'\n') # запись нужной строки для ffmpeg
            
            timelater = os.path.getctime(file)
            
    flist.close()       
          
    '''
    print('файл:') #------------------------контроль вывод файла
    with open(path + NamFileList, mode='r') as f:
        print(f.read())
        f.seek(0)
        print(f.readline())#------------------------контроль'''

    return outFile

def CreateListFile_SD_Mexico (path, NamFileList, outFile):
    '''
        создаёт файл со списком видео файлов для ffmpeg
         из SD или другого пути( афйлы в папке в навал)
         по определённому алгоритму анализируя время создания файлов заточено под мексику
        path - путь
        outFile = название файла вывода если не выбрано берется имя первого файла
    '''
    
    
    #pathN: Path = Path(path) # универсальный путь
    timelater = 0
    fBig = False
    sizef = 0
    
    try:
        flist = open(path + NamFileList, mode='w+')
    except OSError:
        pass
    
    for iterfile in os.listdir(path):
        
        if iterfile.endswith((".mp4", ".MP4")):
            #fileNameP: Path = Path(file) # универсальный путь
            #print(pathN / fileNameP)
            
            file = path + iterfile
            sizef = os.path.getsize(file)/1000000
            
            if timelater ==0:
                timelater = os.path.getctime(file)
                
            dTime = os.path.getctime(file) - timelater
            
            if fBig == False and dTime < 1800 and dTime > 0: # время между файлами до большого файла
                                                                             
                    if sizef > 400:   # размер большого файла 
                        fBig = True
            else:
                    if dTime > 600 or dTime < 0 : #время между файлами после большого файла
                        
                        print('конец прыжка')
                        flist.close()
                        
                        print('Cодержание списка файлов:') #------------------------контроль вывод файла
                        with open(path + NamFileList, mode='r') as f:
                            print(f.read())
                            f.seek(0)
                            print('Итоговое имя файла:',f.readline())#------------------------контроль
                        input('дальше?')
                        
                        return outFile
                        
                    
                    
            print(iterfile,':', sizef, 'mb', dTime , 'сек.delta time ', round(dTime/60,2) , 'мин')
            if  'outSumFile.mp4' in outFile:
                outFile = iterfile
                            
            flist.write('file ' + file +'\n')
            
            
            timelater = os.path.getctime(file)
    flist.close()       
          
    
    print('файл:') #------------------------контроль вывод файла
    with open(path + NamFileList, mode='r') as f:
        print(f.read())
        f.seek(0)
        print(f.readline())#------------------------контроль
    input('файл лист сформирован дальше?')
    return outFile


def CreateListFile_SD_Rus (path, NamFileList, outFile):
    '''
        создаёт файл со списком .jpg файлов для ffmpeg
         из SD или другого пути( афйлы в папке в навал)
         по определённому алгоритму анализируя время создания файлов заточено под мексику
        path - путь
        outFile = название файла вывода если не выбрано берется имя первого файла
    '''
    
    
    #pathN: Path = Path(path) # универсальный путь
    timelater = 0
    # fBig = False
    sizef = 0
    
    try:
        flist = open(path + NamFileList, mode='w+')
    except OSError:
        pass
    
    for iterfile in os.listdir(path):
        
        if iterfile.endswith((".mp4", ".MP4")):
            #fileNameP: Path = Path(file) # универсальный путь
            #print(pathN / fileNameP)
            
            file = path + iterfile 
            sizef = os.path.getsize(file)/1000000
            
            
            if timelater ==0:
                 timelater = os.path.getctime(file)
                
            dTime = os.path.getctime(file) - timelater
            
            # if fBig == False and dTime < 1400: # время между файлами до большого файла
                                                                             
            #         if sizef > 400:   # размер большого файла 
            #             fBig = True
            # else:
            #         if dTime > 600: #время между файлами после большого файла
                        
            #             print('конец прыжка')
            #             flist.close()
                        
                        # print('Cодержание списка файлов:') #------------------------контроль вывод файла
                        # with open(path + NamFileList, mode='r') as f:
                        #     print(f.read())
                        #     f.seek(0)
                        #     print('Итоговое имя файла:',f.readline())#------------------------контроль
                        # input('дальше?')
                        
                        # return outFile
                        
                    
            
            print(iterfile,':', sizef, 'mb', dTime , 'сек.delta time ', round(dTime/60,2) , 'мин')

            if  'outSumFile.mp4' in outFile:
                outFile = iterfile
                            
            flist.write('file ' + file +'\n')
            
            
            timelater = os.path.getctime(file)
    flist.close()       
          
    
    print('файл:') #------------------------контроль вывод файла
    with open(path + NamFileList, mode='r') as f:
        print(f.read())
        # f.seek(0)
        #print(f.readline())#------------------------контроль

    Yn = str(input('файл лист сформирован дальше N/n EXIT?'))
    if 'n'in Yn or 'N' in Yn:
        exit()

    return outFile
     
def add_mp4_in_list(path, pathout, outInfo = False, outFile = 'outSumFile.mp4'):
    '''
      Проходит по папке и из файлов .mp4 делает один с именем outFile = 'outSumFile.mp4'
      path - путь  к папке
      outInfo = False/True выводить инфо о работе
    '''
    outFile = CreateListFile_SD_Rus(path, NamFileList, outFile)
            
    '''             myListFile.txt:
                    file D:/poligon/VID_20201018_131938.mp4
                    file D:/poligon/VID_20201018_132423.mp4
                    file D:/poligon/VID_20201018_135729.mp4
                    file D:/poligon/VID_20201018_140221.mp4
    
    '''
    args = ['ffmpeg', '-f', 'concat', '-safe', '0', '-i', path + NamFileList,'-vsync','2', '-c', 'copy', pathout + outFile]
    #args = ['ffmpeg', '-f', 'concat', '-safe', '0', '-i', path + NamFileList, pathout + outFile]
    print('args:', args)
    
    p = subprocess.run(args, shell=True,capture_output = True, text = True)

    if outInfo is True:   # вывод информайии от ffmpeg
            print('p.returncode:', p.returncode)
            print('p.stdout:', p.stdout)
            print('len(p.stderr):', len(p.stderr))
            print('p.stderr:', p.stderr)
            print('p.stderr:', p.stderr.split('\n')[-2])
            
    
    if os.path.isfile(pathout + outFile ): # если финальныйфайл существует то 

        delFile_fileList_mod(path + NamFileList, True) # удалить исходные файлы
    
    os.remove(path + NamFileList) # удаление сервисного файла
    
    print(path + NamFileList)
    return



def add_jpg_in_list(path, pathout, outInfo = False, outFile = 'outSumFile.mp4'):
     '''
       Проходит по папке и из файлов .jpg делает один с именем outFile = 'outSumFile.mp4'
       path - путь  к папке
       outInfo = False/True выводить инфо о работе
     '''
     outFile = CreateListFile_SD_jpg(path, NamFileList, outFile)
             
     '''             myListFile.txt:
                     file D:/poligon/VID_20201018_131938.jpg
                     file D:/poligon/VID_20201018_132423.jpg
                     file D:/poligon/VID_20201018_135729.jpg
                     file D:/poligon/VID_20201018_140221.jpg
     
     '''
     # без перекодирования потоков
     args = ['ffmpeg', '-f', 'concat', '-safe', '0', '-i', path + NamFileList, '-c', 'copy', pathout + outFile]
     
     
     print('args:', args)
     
     p = subprocess.run(args, shell=True,capture_output = True, text = True)

     if outInfo is True:   # вывод информайии от ffmpeg
             print('p.returncode:', p.returncode)
             print('p.stdout:', p.stdout)
             print('len(p.stderr):', len(p.stderr))
             print('p.stderr:', p.stderr.split('\n')[-2])
             
     
     if os.path.isfile(pathout + outFile ): # если финальныйфайл существует то 
         if 'y'==str(input('Удалить исходные файлы? y-да')):
                delFile_fileList(path + NamFileList) # удалить исходные файлы
     
     os.remove(path + NamFileList) # удаление сервисного файла
     return 
  

def delFile_fileList(pathNameList):
    '''
    удаляет файлы из списка содержащегося в файле
    '''

    f = open(pathNameList, mode='r')
    for i in f:
    
        print(i[0:-2].split(' ')[-1])
        try:
            os.remove(i[0:-1].split(' ')[-1])
        except:
            print('файл: ', i[0:-1].split(' ')[-1], '-отсутствует')
          
    f.close()
    print('всё удалил')

    return


def delFile_fileList_mod(pathNameList, ascDel = True):
    '''
    C вопросом  удаляет файлы из списка содержащегося в файле
    pathNameList - путь к файлу .txt с листом файлов
    ascDel - True задать вопрос перед удалением
    '''
    if ascDel : # если стоит флаг задаем вопрос
        ascD = str(input('Удалять? y/Y '))
        if 'y' in ascD or 'Y' in ascD :
            delFile_fileList(pathNameList) # файлы удаляем из списка
            #exit()

    else:       # если  вопрос не нужен удаляем без слов
        delFile_fileList(pathNameList)      

    return
 
def isFile(path, strXXX):
    '''
    поиск в папке файлов с расширением или частью имени
    ----------
    path : TYPE str
        путь к папке проверки
    strXXX : TYPE str
        чачть имени расширения которое ищем 

    Returns
    -------
    bool False/True
        
    '''
    strxxx = strXXX.lower()
    strXXX = strXXX.upper()
    
    listFile = os.listdir(path)
    for fileName in listFile:
        if fileName.endswith((strXXX,strxxx)):
            return True
    return False

   
    
def main():
    # video_to_gif(path) # Проходит по папке и из файлов .mp4 делает .gif

    if not os.path.exists(pathMp4):  # если папок для работы нет создать
        print('Создаю пути на диске')
        os.makedirs(pathout)
        if  os.path.exists(pathout):
            print('новые папки созданны: ',pathout)


    print('проверка наличия файлов .mp4  ',pathMp4)
    while  isFile(pathMp4, '.MP4'): # пока есть в папке .mp4
        print('Сборка файла:')
        add_mp4_in_list(pathMp4, pathout, outInfo = True) # Проходит по папке и из файлов .mp4 делает один
        
    #add_jpg_in_list(pathMp4, pathout, True) # Проходит по папке и из файлов .jpg делает один
        
    # delFile_fileList(pathMp4 + NamFileList) #удаляет файлы из списка содержащегося в файле
    
    # ask = str(input('Остальное удалить? y/n: '))
    
    # if 'Y' in ask or 'y' in ask :
    #     for fildel in os.listdir(pathMp4):
    #         if os.path.isfile(pathMp4+fildel): # только файлы!!
    #             os.remove(pathMp4+fildel)
    return

if __name__ == "__main__":
    main()

# возможные строки ffmpeg 

#ffmpeg -i MOV1.mp4 -acodec copy -vcodec copy -vbsf h264_mp4toannexb -f mpegts mov1.ts #Конвертим файлы в MPEG-TS (делается довольно быстро):

    #file D:\\poligon\\VID_20201018_140221.ts 
    #ffmpeg -safe 0 -f concat -i mylist1.txt -c copy D:\\poligon\\outpu2.mp4# работает

    #ffmpeg -i "concat:D:\\poligon\\VID_20201018_140221.ts|D:\\poligon\\VID_20201018_131938.ts" -c copy uutput3.mp4
    
#ffmpeg -f concat -i myListFile.txt -c copy output.mp4 #работает даже с листом .mp4
#ffmpeg -i C:/DCIM/1080PVersion.mp4 -r 60 C:/DCIM/1080PVersion60.mp4 # переформат на 60 кадров
#ffmpeg -i C:/DCIM/1080PVersion.mp4 -r 60 -b:v 30M C:/DCIM/1080PVersion60.mp4 # переформат на 60 кадров и битрейт видео 30М
   
#p = subprocess.run(ffmpeg -i MOV1.mp4 -acodec copy -vcodec copy -vbsf h264_mp4toannexb -f mpegts mov1.ts
