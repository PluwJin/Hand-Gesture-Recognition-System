import numpy as np
import cv2
import tensorflow as tf
from time import sleep
from threading import Thread,Event,Condition

LABELS14={
    0:"Swiping Left",
    1:"Swiping Right",
    2:"Pulling Hand In",
    3:"Sliding Two Fingers Left",
    4:"Sliding Two Fingers Right",
    5:"Zooming In With Full Hand",
    6:"Zooming In With Two Fingers",
    7:"Zooming Out With Two Fingers",
    8:"Thumb Up",
    9:"Thumb Down",
    10:"Stop Sign",
    11:"Drumming Fingers",
    12:"No gesture",
    13:"Doing other things",
}

class PredictThread(Thread):
    def __init__(self,batch=np.zeros((1, 12, 150, 100, 3))):
        super(PredictThread,self).__init__()
        self.stopFlag = Event()
        self.batch_queue = batch
        self.physical_devices = tf.config.list_physical_devices('GPU')
        tf.config.experimental.set_memory_growth(self.physical_devices[0], True)
        #self.model = tf.keras.models.load_model('C:/Users/Erhan Özdoğan/Desktop/gesture-recognizer/Models/14Class-89/model14class_11.h5') #89
        self.model = tf.keras.models.load_model('C:/Users/Erhan Özdoğan/Desktop/gesture-recognizer/Models/27Class-83/model27class_11 _83.h5') #74
        self.result=12
        self.prob=1
        self.con = Condition()

    def run(self):
        while self.stopFlag.is_set() != True:
            try:
                out_arr = self.model.predict(self.batch_queue, use_multiprocessing=False)
                self.result = np.argmax(out_arr)
                self.prob = np.amax(out_arr)
                sleep(0.07)
            except AttributeError as ex:
                print("hata: ", ex)
    def join(self,timeout=None):
        self.stopFlag.set()
        super(PredictThread,self).join(timeout)
    def get_prediction_value(self):
        return self.result,self.prob

    def isalive(self):
        return self.is_alive()

    def pause(self):
        self.con.acquire()
        self.con.wait()
        self.con.release()

    def resume(self):
        self.con.acquire()
        self.con.notify()
        self.con.release()





