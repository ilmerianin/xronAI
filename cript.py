import os
import sys

pathCript = '/data/data/com.termux/files/home/storage/shared/dcim/krip/'  

def main():
    arg_v = sys.argv
    #print('begin prog')
    #print('sys.argv:',arg_v,' len:',len(arg_v))

    #проверка на наличие папки
    if os.path.isdir(pathCript):
        
        print('paer  found: ', pathCript)
        
        if len(arg_v) > 1:
            if arg_v[1]=='1': #если 1 значит криптовать
                print('криптую')
                criptfiles(pathCript)

            if arg_v[1] == '0':
                print('декриптую')
                decriptfiles(pathCript)
        else:
            print('this app crypto files arguments(1- to cript 0- to descript')
        return
    #если нет создать
    else:
        print('Dont find paper!')
        print('Create new paper: ', pathCript)
        os.mkdir(pathCript)
        return

    print('this app cripto files arguments (1- to cript 0- to descript')
    

    return

def decriptfiles(pathCript):
    ''' вернуть обратно расширение'''
    
    listFiles = os.listdir(pathCript)   

    print(len(listFiles))

    for file in listFiles:
               # recrusive find paper
        if os.path.isdir(pathCript + file):
            decriptfiles(pathCript + file + '/')

               #выбрать только зашифрованные файлы
        if file.endswith(('.xxx', '.XXX')):

            if os.path.isfile(pathCript + file):
        
                newFileName = file.split('.')[0][0:-3] +'.'+ file.split('.')[0][-3:] 
                print('decrypt file:', newFileName)
                os.rename(pathCript + file, pathCript + newFileName)
            else:
                print('no find ile')

def criptfiles(pathCript):
    ''' типо шифрование перенести расширение за точку.и сделать .xxx '''

    listFiles = os.listdir(pathCript)

    for file in listFiles:
        print('file name:', file)
                # go to recrusive paper
        if os.path.isdir(pathCript + file):
            criptfiles(pathCript + file + '/')

                #исключить уже зашифрованные файлы       
        if '.xxx' not  in file:
            if os.path.isfile(pathCript + file):

                #print('find file: ',file)
                #print('new name file:', file. split('.')[0], '+ ', 'xxx')
                newFileName = file.split('.')[0] + file.split('.')[1] + '.xxx'
                print('crypt is:', newFileName)
                os.rename(pathCript + file, pathCript + newFileName)
            else:
                print('no find ile')
     
    return



if __name__ == '__main__':
    main()
