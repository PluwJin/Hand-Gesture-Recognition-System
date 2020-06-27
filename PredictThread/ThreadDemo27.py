import numpy as np
import cv2
from PredictThread import PredictThread
import time

LABELS27={
    0:"Swiping Left",
    1:"Swiping Right",
    2:"Swiping Down",
    3:"Swiping Up",
    4:"Pushing Hand Away",
    5:"Pulling Hand In",
    6:"Sliding Two Fingers Left",
    7:"Sliding Two Fingers Right",
    8:"Sliding Two Fingers Down",
    9:"Sliding Two Fingers Up",
    10:"Pushing Two Fingers Away",
    11:"Pulling Two Fingers In",
    12:"Rolling Hand Forward",
    13:"Rolling Hand Backward",
    14:"Turning Hand Clockwise",
    15:"Turning Hand Counterclockwise",
    16:"Zooming In With Full Hand",
    17:"Zooming Out With Full Hand",
    18:"Zooming In With Two Fingers",
    19:"Zooming Out With Two Fingers",
    20:"Thumb Up",
    21:"Thumb Down",
    22:"Shaking Hand",
    23:"Stop Sign",
    24:"Drumming Fingers",
    25:"No gesture",
    26:"Doing other things",
}

gesture = np.zeros((1, 12, 150, 100, 3))


def frame_queue(image, batch_queue):
    for i in range(11):
        batch_queue[0][i] = batch_queue[0][i+1]
    img = cv2.resize(image, (100, 150))
    batch_queue[0][11] = img
    return batch


batch = np.zeros((1, 12, 150, 100, 3))
cap = cv2.VideoCapture(0)
text = "No gesture"
result,res = (25,25)
prob=0
prob_2 =1
model = PredictThread(batch)
model.start()
i=0
while True:
    _, frame = cap.read()
    crop_frame = frame[100:400, 150:500]
    batch = frame_queue(crop_frame, batch)
    res, prob = model.get_prediction_value()
    if prob > 0.6:
        text = LABELS27[res]
        prob_2 = prob

    cv2.putText(frame, text + " " + str(prob_2), (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.rectangle(frame, (150, 100), (500, 400), (0, 255, 0), 2)
    cv2.imshow("cam", frame)
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
model.join()








