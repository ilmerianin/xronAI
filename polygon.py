# -*- coding: utf-8 -*-
# https://tproger.ru/translations/opencv-python-guide/
# https://zen.yandex.ru/media/machinelearning/opencv-i-vebkamera-62459b0ffee0152eb3c2440c
#  OpenCV  доквументация https://docs.opencv.org/4.5.5/dd/d43/tutorial_py_video_display.html

#pip install opencv-python
import cv2 as cv # 05/05/22 Successfully installed opencv-python-4.5.5.64
import argparse
import numpy as np
import time
import os

# cv2.imwrite("./экспорт/путь.расширение", image)  #Сохранение изображения

def OpenFile():
    '''открыть файл путь взять из строки аргумента !! доработать пересфлку в def func():
    '''
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="path to input image")
    args = vars(ap.parse_args())

    image = cv.imread(args["image"], cv.IMREAD_GRAYSCALE)
      # image = cv2.imread("./путь/к/изображению.расширение")
      # rgb_image = cv.cvtColor(image, cv2.COLOR_BGR2RGB) #Поменять цветовое пространство на RGB

    cv.imshow("Image", image)
    cv.waitKey(0)

    (h, w) = image.shape[:2]

    # display image properties
    print("width: {} pixels".format(w))
    print("height: {} pixels".format(h))

    cv.imwrite("photos/newimage.png", image)

def OpenVideoPach(pach):
    '''открыть файл путь работает 13.05.22
    используется : faces = Find_cascade_fich(face_cascade,frame) 
    '''
    cap = cv.VideoCapture(pach)
    retr = True

    # Собственно этой командой мы загружаем уже обученные классификаторы cv.data.haarcascades+'haarcascade_frontalface_default.xml'
    face_cascade = cv.CascadeClassifier('C:\AI\haarcascade_frontalface_default.xml') # временно заброшен туда использование этого способа на 3 много не распознает

    while retr:

        retr, frame = cap.read()
        StartTime = time.time()
        faces = Find_cascade_fich(face_cascade,frame) #
        print('Время распознания:', str(time.time()-StartTime))
        
        DravRectangleImage(frame, faces)
        
    return


def viewImage(image, name_of_window = 'name_of_window '):
    ''' вывод в окно с с названием работает 13.05.22'''
    cv.namedWindow(name_of_window, cv.WINDOW_NORMAL) #создать окно с именем
    cv.imshow(name_of_window, image)
    
    cv.waitKey(0) # время ждать
     
    cv.destroyAllWindows()


def CapchureVideo():
    ''' захват видео с камеры  не тестировали
    код отсюда:
     https://zen.yandex.ru/media/machinelearning/opencv-i-vebkamera-62459b0ffee0152eb3c2440c
    '''
    print(' CapchureVideo polygon')
    cap = cv.VideoCapture(0) # инициализирует веб-камеру (цифра указывает её индекс).
            #cap = cv.VideoCapture('vtest.avi')

    while(True):
        ret, frame = cap.read()  # Получить картинку с камеры татус получения картинки в ret. Если ret == True, значит все прошло успешно.

        if ret:
            viewImage(frame, 'NewWindow')
        # if ret:         
        #     cv.imshow('original', frame) # Показать окно с картинкой
        # else : print(ret = False)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()   # освободить камеру
    cv.destroyAllWindows()  # закрыть окна
    return

def Find_cascade_fich(face_cascade, image):
    ''' ищет лица на фото  работает 13.05.22
    face_cascad 
    image frame" 
    return:
        type(faces): <class 'numpy.ndarray'> (x, 4)
    время работы  wait time: 0.15 сек
     https://tproger.ru/translations/opencv-python-guide/'''

   
    # if not face_cascade.empty(): #если нет класификатора
    #     # Собственно этой командой мы загружаем уже обученные классификаторы cv.data.haarcascades+'haarcascade_frontalface_default.xml'
    #     face_cascade = cv.CascadeClassifier('C:\AI\haarcascade_frontalface_default.xml') # временно заброшен туда 

    assert not face_cascade.empty(), 'cv.CascadeClassifier( не нашёл файл haarcascade_frontalface_default.xml) '

    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)  # сделать серым

    faces = face_cascade.detectMultiScale(   #общая функция для распознавания как лиц, так и объектов. Чтобы функция искала именно лица, мы передаём ей соответствующий каскад.
        gray,              # Обрабатываемое изображение в градации серого.
        scaleFactor= 1.1,  # Параметр scaleFactor. Некоторые лица могут быть больше других, поскольку находятся ближе, чем остальные. Этот параметр компенсирует перспективу.
        minNeighbors= 5,   # Алгоритм распознавания использует скользящее окно во время распознавания объектов. Параметр minNeighbors определяет количество объектов вокруг лица. То есть чем больше значение этого параметра, тем больше аналогичных объектов необходимо алгоритму, чтобы он определил текущий объект, как лицо. Слишком маленькое значение увеличит количество ложных срабатываний, а слишком большое сделает алгоритм более требовательным.
        minSize=(10, 10)   # непосредственно размер этих областей
    )

    # faces_detected = "Лиц обнаружено: " + format(len(faces))
    # print(faces_detected, 'type(faces):', type(faces), faces.shape)
     

    return faces

def FindFase(image_path = "c:/"):
    ''' ищет лица на фото работает 13.05.22
    image_path = "./путь/к/фото.расширение" 
    return:
        type(faces): <class 'numpy.ndarray'> (x, 4)
    dhtvz hf,jns wait time: 0.8310215473175049 сек
     https://tproger.ru/translations/opencv-python-guide/'''

                                        # Собственно этой командой мы загружаем уже обученные классификаторы cv.data.haarcascades+'haarcascade_frontalface_default.xml'
    face_cascade = cv.CascadeClassifier('C:\AI\haarcascade_frontalface_default.xml') # временно заброшен туда
        #'C:\\Users\\Язь\\AppData\\Local\\Programs\\Python\\Python38\\lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml') # c:\Users\Язь\AppData\Local\Programs\Python\Python38\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml') #haarcascade_frontalface_alt.xml
    
    # print(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
    # print(cv.CascadeClassifier.empty(face_cascade) )
    # print('проверка', face_cascade.empty())

    assert not face_cascade.empty(), 'cv.CascadeClassifier( не нашёл файл haarcascade_frontalface_default.xml) '

    image = cv.imread(image_path)      # считать файл
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)  # сделать серым

    faces = face_cascade.detectMultiScale(   #общая функция для распознавания как лиц, так и объектов. Чтобы функция искала именно лица, мы передаём ей соответствующий каскад.
        gray,              # Обрабатываемое изображение в градации серого.
        scaleFactor= 1.1,  # Параметр scaleFactor. Некоторые лица могут быть больше других, поскольку находятся ближе, чем остальные. Этот параметр компенсирует перспективу.
        minNeighbors= 5,   # Алгоритм распознавания использует скользящее окно во время распознавания объектов. Параметр minNeighbors определяет количество объектов вокруг лица. То есть чем больше значение этого параметра, тем больше аналогичных объектов необходимо алгоритму, чтобы он определил текущий объект, как лицо. Слишком маленькое значение увеличит количество ложных срабатываний, а слишком большое сделает алгоритм более требовательным.
        minSize=(10, 10)   # непосредственно размер этих областей
    )

    # faces_detected = "Лиц обнаружено: " + format(len(faces))
    # print(faces_detected, 'type(faces):', type(faces), faces.shape)
     

    return faces, image

def DravRectangleImage(image, rectangle_NP):
    ''' рисует картинку и квадраты фич работает 13.05.22
        image: cv.imread
        rectangle_NP :<class 'numpy.ndarray'> (x, 4) 
    return 
        True - 
        Fault - не найдены фичи
    '''
    faces_detected = "Fich find: " + format(len(rectangle_NP))
    if len(rectangle_NP) == 0:
        print('не найдены фичи')
        return 0
    # Рисуем квадраты вокруг лиц
    for (x, y, w, h) in rectangle_NP:
        cv.rectangle(image, (x, y), (x+w, y+h), (255, 255, 0), 2) # отрисовка квадратов

    viewImage(image,faces_detected)
    return 1

def main():
    print(' main polygon')

    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit() # выход из программы
    print('чтото нашел')
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        # Our operations on the frame come here
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # Display the resulting frame
        cv.imshow('frame', gray)
        if cv.waitKey(1) == ord('q'):
            break
    # When everything done, release the capture
    cap.release()
    cv.destroyAllWindows()

    return

def FindFich_dnn_readNetFromCaffe(path):
    ''' распознание с помощью нейросети
    pach - путь к видео
    https://telegra.ph/Python-raspoznavanie-obektov-v-realnom-vremeni-06-11

    https://habr.com/ru/company/intel/blog/333612/      более подробно
    '''
    # construct the argument parse and parse the arguments не пошло
    # ap = argparse.ArgumentParser()
    # ap.add_argument("-p", "--prototxt", required=True, help="path to Caffe 'deploy' prototxt file") #--prototxt : Путь к prototxt Caffe файлу.
    # ap.add_argument("-m", "--model",    required=True, help="path to Caffe pre-trained model")      #--model : Путь к предварительно подготовленной модели.
    # ap.add_argument("-c", "--confidence", type=float, default=0.2, help="minimum probability to filter weak detections") #--confidence : Минимальный порог валидности (сходства) для распознавания объекта (значение по умолчанию - 20%).
    # args = vars(ap.parse_args())
    #
    # net = cv.dnn.readNetFromCaffe(args["prototxt"], args["model"])

    # load our serialized face detector from disk
    print("[INFO] loading face detector...")
    protoPath = os.path.sep.join([args["detector"], "deploy.prototxt"])
    modelPath = os.path.sep.join([args["detector"], "res10_300x300_ssd_iter_140000.caffemodel"])
    net = cv.dnn.readNetFromCaffe(protoPath, modelPath)


        # initialize the list of class labels MobileNet SSD was trained to
    # detect, then generate a set of bounding box colors for each class
    CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
    "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
    "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
    "sofa", "train", "tvmonitor"]
    COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

    

    cap = cv.VideoCapture(path)
    retr = True

    while retr:

        retr, frame = cap.read() #считываем кадр
        StartTime = time.time()
        h,w  = frame.shape[:2]

        blob = cv.dnn.blobFromImage(cv.resize(frame, (300,300)),0.007843, (300, 300), 127.5) #преобразование кадра в blob с модулем dnn
        net.setInput(blob)  #мы устанавливаем blob как входные данные в нашу нейросеть
        pred = net.forward() #передаём эти данные через net (строка 54), которая обнаруживает наши предметы
        
        print('predict: ',type(pred), pred.shape,' Время распознания:', str(time.time()-StartTime))
        retr = False

    return



if __name__ =='__main__':
    
    # 1
    # print('sys.path:', sys.path)
    # CapchureVideo() #захват видео с камеры 

    # 2
    # path = 'C:/Ai/768.jpg'  #  C:/Users/Язь/YandexDisk/Скрин для нета/GOPR1494.MP4_20210517_145240.768.jpg'
    # startTime = time.time()
    # faces, image = FindFase(path)
    # print('wait time:',str(time.time()-startTime))
    # DravRectangleImage(image, faces)

    # 3
    #path = 'D:/DCIM/WhatsApp Video 2021-07-23 at 14.52.17.mp4'  # frame.shape: (480, 848, 3)  C:/Users/Язь/YandexDisk/Скрин для нета/GOPR1494.MP4_20210517_145240.768.jpg'
    # OpenVideoPach(path)

    # 4
    #FindFich_dnn_readNetFromCaffe(path)


    main()
