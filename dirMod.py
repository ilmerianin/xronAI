# 04.10.22 отработка поиска папок на новом телефоне и создание базы для дальнейшей работы
# доработанная dir выводит содержи'/data/data/com.termux/',мое процедуры в столбик
# сортирует (очищает/перемещает) файлы по списку задач
# вывод списка папок с вложееиями и поиск папки по имени


import os
import sys
import shutil
import pickle
import json

findfraza = 'teleg' #фраза поиска в listdir
pathT= '/data/data/com.termux/'
fileName = 'taskDirMod.txt' #сервисный файл с задачами,переменная  пока не порключена  определение происходит по умолчанию в процндуре
#/data/data/com.termux/files/

# List очистки и копирования файлов для sortiFiles: этот используется для поиска на диске нового телефона данных папок
''' формат списка задач['/data/data/com.termux/files/home/WhatsApp/Media/WhatsApp Video/Sent/',
    '0',"." ,0],
inPath = "папка источник" для поиска                       outPath = 'папка получатель'                      xxx = '.mp4' # расширение файлов                  coDel = 0    # 0-del 1-copy+del 2- copy
'''
inOutPathes = list([
    ['Telegram Documents', '0', '.mp4',0],
    ['Telegram Documents', '0', '.MP4',0],
    ['Telegram Documents', '0', '.mp3',0],
    ['Telegram Documents', '0', '.jpeg',0],
    ['Telegram Documents', '0', '.jpg',0],
    ['Telegram Documents', '/data/data/com.termux/files/home/storage/shared/documents/pdf/',  '.pdf', 1],
    ['Telegram Documents', '0','.webp', 0],
    ['Telegram Documents', '0','.png', 0],
   ['Telegram Video',  '0', '.mp4',0],
   ['Telegram Video',  '0',  '.w',0],
   ['Yandex','0',    '.jpg',0],
  ['Telegram Video', '0', '.m',0],
  ['Telegram Images','0', '.jpg',0],
  ['Telegram Video', '0', '.M',0],                  ['Telegram Video', '0', '.mov',0]])

# путь для вывода дерева папок listDir
# и поиска имен 
pathx ='/data/data/com.termux/files/'
# OPPO: /data/data/com.termux/files/home/storage/shared/Android/media/org.telegram.messenger/Telegram
#'/storage/375D-13F3/DCIM/'

#'/data/data/com.termux/files/'
# /data/data/com.termux/files/usr/lib/python3.10/'

proc=pickle   # место опрееления имени метода для листа методов dirprint

def dirprint(proc):  # доработанная dir выводит содержимое апроцедуры в столбик
    dirlist=dir(proc)
    print('dir(%s):' % proc)

    for idproc in dirlist:
        print(idproc)
    return

# вывод папок и файлов на всю глубину
def listDir(pathx,fileVis=0):
    ''' путь к папке
        1- выводить файлы в папках 0- не выводить
        !!! внутри костыль для поиска по названию папки потом допилю красоту!!!
	в глобальной переменной findfraza фраза для поиска
    '''
    try: # какаято папка вызывала ошибку прикидываясь файлом
    	listpath = os.listdir(pathx)
    except Exception:
        print('error os.listdir:',pathx)
        return

    #print('listpath:', listpath)

    listPathDir =[] # накопитель списка папок в данной ветке/папке

    for filename in listpath:
        if os.path.isfile(pathx+filename):
            if fileVis== 1 : # вывод файлов на печать если нужно
                print(filename)
        else:
            if os.path.isdir(pathx+filename):
                listPathDir.append(pathx+filename+'/') # сборка путей к папкам

    for dirPath in listPathDir: #перебор папок 
       # listDir(dirPath)
       if findfraza in dirPath: #поиск папки по имени
          print(dirPath)

       listDir(dirPath,0) #перезагрузка процедуры для вывода вложенных папок

    return

def sortFiles(inPath, outPath, xxx, coDel):
    '''
    сортировка файлов в папках:
    папка просмотра (источник)
    папка перемещения
    расширение тип- файлов '.mp4'
    copy delete 0 - delete
                1 - copy+delete
                2 - copy'''
    listfiles = os.listdir(inPath)

    for namefile in listfiles:
        if xxx in namefile:
            if coDel == 1 or coDel ==2: 
                print('copy:',namefile,'>',outPath)
                shutil.copy(inPath+namefile, outPath)# копируем файл

            if coDel <= 1:
                print('delete:',inPath+namefile)
                os.remove(inPath+namefile)#удаление файла
    return

def printtask(inPath,outPath,xxxx,coDel):
    ''' вывод задачи'''
    print('inPath:',inPath) 

    print("outPath:",outPath)

    print("xxxx:",xxxx)  

    print("coDel:",coDel)

    return

def printlist(listX):
    ''' вывод списка задач для sortFiles()'''
    for i in listX:
          
        printtask(*i)
        
    return

# поиск папки и возврат полного пути
def createPath(inPath, pathx):
    ''' название папки, путь 
        
        в переменной inPath фраза для поиска
    '''
    try: # была проблема с ошибкой папки.файла
        listpath = os.listdir(pathx)
    except Exception:
        #print(' ')
        #print('error os.listdir:',pathx)
        return False

    #print('listpath:', listpath)

    listPathDir =[]

    for filename in listpath:
        if os.path.isfile(pathx+filename):
            pass
        else:
            if os.path.isdir(pathx+filename):
                listPathDir.append(pathx+filename+
'/')

    for dirPath in listPathDir: #перебор папок
       # listDir(dirPath)
       if inPath in dirPath: #поиск папки по имени
          #print('первое нахождение:', dirPath)

          return dirPath

       fulPath = createPath(inPath, dirPath) #перезагрузка процедуры для вывода вложенных папок
       
       if fulPath != False: # если найден путь
           #print('нашли:',fulPath)
           return fulPath
    
    return False

def choisePath(): #------------------------------
    '''выбор пути  посредством поиска
       возвращает выбранный путь  '''

    while True:
        findFraza = str(input('Введите [-x](отмена) или  фразу для поиска\n:'))
        if '-x' in findFraza or '-X' in findFraza: 
            return False #

        patches =  findPath(findFraza)
        i = 0
        for pat in patches:
            print(i,' ',pat)
            i +=1
        while True:
            antwort = str(input('Введите номер пути или [n]\n:'))
            if 'n' in antwort or 'N' in antwort:
                print('n - return False')
                break
            try:
                num = int(antwort)
            except Exception:
                print('ошибка num = int(antwort) - return False')
                continue

            if num < i :
                print('ваш выбор')
                return patches[num]
    print('Этого не должно быть!')
    return  False

# поиск всех папок и возврат списка полных путей
def findPath(inPath, pathx= '/data/data/com.termux/'):
    ''' название папки, путь 
        
        в переменной inPath фраза для поиска
    '''
    try: # была проблема с ошибкой папки.файла
        listpath = os.listdir(pathx)
    except Exception:
        #print(' ')
        #print('error os.listdir:',pathx)
        return False

    #print('listpath:', listpath)

    listPathDir =[]
    listFindDir =[]

    for filename in listpath:
        if os.path.isfile(pathx+filename):
            pass
        else:
            if os.path.isdir(pathx+filename):
                listPathDir.append(pathx+filename+
'/')

    for dirPath in listPathDir: #перебор папок
       # listDir(dirPath)
        if inPath in dirPath: #поиск папки по имени
             print('нашли:', dirPath)

             listFindDir.append(dirPath)

        fulPath = findPath(inPath, dirPath) #перезагрузка процедуры для вывода вложенных папок
        
        if (isinstance(fulPath, bool)) :
             print('nashol') 
        else:
            if len(fulPath) >=1:
               listFindDir.extend(fulPath)
    
    return listFindDir

# поиск путей для формирования нового списка задач из заготовки
def findNewPath(truName, pathT= '/data/data/com.termux/'):
    ''' a '''

    listTask = []
    for i in truName: # перебор задач для #сортировки файлов

        inPath, outPath, xxxx, coDel = i
        print('Поиск',i)
        inPath = createPath(inPath, pathT)

        if inPath: #если inPath не Fasse
            print('Добавление: ', inPath)
            i[0] = inPath
            listTask.append(i) # добавление в список
    
    printlist(listTask)
    
    return listTask

def sortFilesFromTasks(listTasks):
    ''' сортировка файлов в папках по найденным на данном устройстве путям на вводе 
    список задач   '''

    for i in listTasks: # перебор задач для #сортировки файлов
        inPath, outPath, xxxx, coDel = i
        print('Обработка;',i)

        try:
           sortFiles(inPath, outPath, xxxx, coDel)
        except:
            print('не смог:',inPath)
    

    return

def saveList(listOut, fileName = 'taskDirMod.txt'):    
    '''сохраненеие списка задач '''

    with open(fileName, 'w') as file:
       json.dump(listOut,file)
 
    return

def addTask(taskI, fileName = 'taskDirMod.txt'):
    ''' добавление к файлу задач 1й задачи  '''
    listT = readList(fileName)

    print(listT)

    listT.append(taskI)
    print(listT)
    saveList(listT, fileName)
    return

def readList(fileName = 'taskDirMod.txt'):
    '''чтение списка задач'''
    with open(fileName,'r') as file:
        listIn = json.load(file)
    return listIn

def add_new_task(fileName = 'taskDirMod.txt'):
	'''добавление новых задач в файл задач  '''
	inPath = choisePath() # поиск и выбор целевого пути
	if inPath == False:return False 
	print('выбран путь:',inPath)
	# дальше нужен выбор действия и формирование задачи
	coDel = int(input('введите действие 0-удалить 1-переместить 2-копировать'))
	if coDel == 0:
		outPath ='0'
	elif coDel == 1 or coDel == 2:
		print('выберите путь  для переноса:') #ghj
		outPath = choisePath()
		print('выбран путь для копирования:\n',outPath)
	else: 
		print('выбор не понятен пробуйте заново')
		return False # 125
	xxxx = str(input('какое расширение [.jpg] or [.J] :'))
	# вывести на экран параметры задачи
	printtask(inPath,outPath,xxxx,coDel)
	yeNo = str(input('записываем? y - да '))

	if 'y' in yeNo or 'Y' in yeNo:
		print('добавляю в список')
		return [inPath,outPath,xxxx,coDel]
	
	return False #ret

def main():
    arg = sys.argv

    if len(arg) > 1:
        if '-с' in arg  or '-С' in arg:
            # Создание из шаблона  для нового телефона
            print('FindNewPath')
            
            newlist = findNewPath(inOutPathes) # поиск путей для формирования нового списка задач из заготовки. ! работает
            print('\n newlist:\n', newlist)
            print('сохраняю......')
            saveList(newlist)

            print(type(newlist),len(newlist),'\n Cохраннено:\n',newlist)
            InList = readList()
            print(type(InList),len(InList),'\n прочитанно:\n',InList)

        if '-f' in arg or '-F' in arg:
            # поиск и добавление новых
            print('обработка поиска и добавления новой задачи')
            i = add_new_task()
            if i !=False:
                print('Добавляю задачу') 
                addTask(i)
            #-----------------------------
        if '-s' in arg or '-S' in arg:
            #сортировка
            print('Сортирую согласно задач изфайла:',fileName)
            listTasks = readList()
            sortFilesFromTasks(listTasks) # сортировка файлов в папках по найденным на данном устройстве путям записанным в сервисном файле

        if '-d' in arg:
            print('arg :', arg, len(arg))
            print('модуль :',arg[2])
            dirprint(arg[2]) 
        if '-h' in arg or '-H' in arg:
            print(' -h help\n -c Создание из шаблона  для нового телефона \n -f Поиск и добавление новых \n -h [proc] вывод содержимого pyton модуля \n -s сортировка файлов в папках файл задач:',fileName)
 
   # printlist(inOutPathes) #вывод списка задач

   # dirprint(proc) #вывод списка методов процедуры
   
   # listDir(pathT, 0)     # pathx) # вывод папок и файлов с вложениями 
   # newlist = findNewPath(inOutPathes) # поиск путей для формирования нового списка задач из заготовк работает
  #  print('\n newlist:\n', newlist)

    #sortFilesFromTasks(listTasks) # сортировка файлов в папках по найденным на данном устройстве путя
    
    return

if __name__ =="__main__":
    main()
