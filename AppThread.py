from time import sleep
from threading import Thread,Event
from  selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class AppThread(Thread):
    def __init__(self,gesture_no=99,prob=0):
        super(AppThread,self).__init__()
        self.stopFlag = Event()
        self.gesture_no = gesture_no
        self.prob = prob

        driver_path = "C:\chromedriver.exe"
        self.driver = webdriver.Chrome(driver_path)
        self.driver.get("http://www.python.org")

    def run(self):
        actions = ActionChains(self.driver)
        zm = 100
        while self.stopFlag.is_set() != True:
            print("Gesture: ", self.gesture_no, "Probablity", self.prob)
            try:
                if self.prob > 0.80:
                    #Swiping Left
                    if self.gesture_no == 0:
                        print(" - görev: geri git")
                        self.driver.back()
                        sleep(4)

                    # Swiping Right
                    elif self.gesture_no == 1:
                        print(" - görev: ileri git")
                        self.driver.forward()
                        sleep(4)

                    #Pulling Hand In
                    elif self.gesture_no == 5:
                        print(" - görev: sayfa yenileme")
                        self.driver.refresh()
                        sleep(4)

                    # Thumb Down
                    elif self.gesture_no == 21:
                        print(" - görev: aşağı kaydır")
                        actions.send_keys(Keys.PAGE_DOWN).perform()
                        sleep(2)

                    # Thumb Up
                    elif self.gesture_no == 20:
                        print(" - görev: yukarı kaydır")
                        actions.send_keys(Keys.PAGE_UP).perform()
                        sleep(2)

                    # Zoom In With Full Hand
                    elif self.gesture_no == 16:
                        print(" - görev: yakınlaştır")
                        zm += 5
                        szm = "document.body.style.zoom='" + str(zm) + "%'"
                        self.driver.execute_script(szm)
                        sleep(4)

                    # Zoom Out With Full Hand
                    elif self.gesture_no == 17:
                        print(" - görev: uzaklaştır")
                        zm -= 5
                        szm = "document.body.style.zoom='" + str(zm) + "%'"
                        self.driver.execute_script(szm)
                        sleep(4)

                    # Drumming Fingers
                    elif self.gesture_no == 24:
                        print(" - görev: sekmeyi kapat")
                        self.driver.close()
                        sleep(4)

                    #Pulling Two Fingers in
                    elif self.gesture_no == 11:
                        print(" - görev: tarayıcıyı kapat")
                        self.driver.quit()
                        sleep(4)

                    else:
                        print("Not Recorded Gesture")

            except AttributeError as ex:
                print("hata: ", ex)
    def join(self,timeout=None):
        self.stopFlag.set()
        super(AppThread,self).join(timeout)


