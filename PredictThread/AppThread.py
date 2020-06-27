from time import sleep
from threading import Thread,Event,Condition
from  selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class AppThread(Thread):
    def __init__(self,gesture_no=99,prob=0):
        super(AppThread,self).__init__()
        self.stopFlag = Event()
        self.gesture_no = gesture_no
        self.prob = prob
        self.tab_count= 0
        self.con = Condition()

        driver_path = "C:\chromedriver.exe"
        self.driver = webdriver.Chrome(driver_path)
        self.driver.get("http://www.python.org")

    def run(self):
        actions = ActionChains(self.driver)
        zm = 100
        while self.stopFlag.is_set() != True:
            try:
                if self.prob > 0.70 :
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
                    elif self.gesture_no == 2:
                        print(" - görev: sayfa yenileme")
                        self.driver.refresh()
                        sleep(4)

                    # Thumb Down
                    elif self.gesture_no == 9:
                        print(" - görev: aşağı kaydır")
                        actions.send_keys(Keys.PAGE_DOWN).perform()
                        sleep(1)

                    # Thumb Up
                    elif self.gesture_no == 8:
                        print(" - görev: yukarı kaydır")
                        actions.send_keys(Keys.PAGE_UP).perform()
                        sleep(1)

                    # Zoom In With Two Fingers
                    elif self.gesture_no == 6:
                        print(" - görev: yakınlaştır")
                        zm += 5
                        szm = "document.body.style.zoom='" + str(zm) + "%'"
                        self.driver.execute_script(szm)
                        sleep(4)

                    # Zoom Out With Two Finger
                    elif self.gesture_no == 7:
                        print(" - görev: uzaklaştır")
                        zm -= 5
                        szm = "document.body.style.zoom='" + str(zm) + "%'"
                        self.driver.execute_script(szm)
                        sleep(4)

                    # Drumming Fingers
                    elif self.gesture_no == 11:
                        print(" - görev: sekmeyi kapat")
                        self.driver.switch_to.window(self.driver.window_handles[self.tab_count])
                        self.driver.close()
                        if self.tab_count == 0 and len(self.driver.window_handles) != 0:
                            self.driver.switch_to.window(self.driver.window_handles[self.tab_count])
                        elif self.tab_count != 0:
                            self.tab_count -= 1
                            self.driver.switch_to.window(self.driver.window_handles[self.tab_count])
                        sleep(4)

                    # Zoom In With Full Hand
                    elif self.gesture_no == 5:
                        print(" - görev: Yeni Sekme")
                        self.driver.execute_script("window.open('https://www.google.com','_blank');");
                        self.tab_count += 1
                        self.driver.switch_to.window(self.driver.window_handles[self.tab_count])
                        sleep(4)

                    # Sliding Two Fingers Left
                    elif self.gesture_no == 3:
                        print(" - görev: Soldaki Sekmeye Git")
                        if self.tab_count-1 >=0  and self.driver.window_handles[self.tab_count-1] != None:
                            self.tab_count -= 1
                            self.driver.switch_to.window(self.driver.window_handles[self.tab_count])
                            sleep(4)

                    # Sliding Two Fingers Right
                    elif self.gesture_no == 4:
                        print(" - görev: Sağdaki Sekmeye Git")
                        if self.tab_count+1<len(self.driver.window_handles) and self.driver.window_handles[self.tab_count+1] != None:
                            self.tab_count += 1
                            self.driver.switch_to.window(self.driver.window_handles[self.tab_count])
                            sleep(4)

                    #Stop Sign
                    elif self.gesture_no == 10:
                        print(" - görev: tarayıcıyı kapat")
                        self.driver.quit()
                        sleep(4)
                self.pause()
            except AttributeError as ex:
                print("hata: ", ex)

    def join(self,timeout=None):
        self.con.acquire()
        self.stopFlag.set()
        super(AppThread,self).join(timeout)


    def pause(self):
        self.con.acquire()
        self.con.wait()
        self.con.release()

    def resume(self):
        self.con.acquire()
        self.con.notify()
        self.con.release()




