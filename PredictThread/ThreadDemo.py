import numpy as np
import cv2
from PredictThread import PredictThread
from AppThread import AppThread

LABELS14 = {
    0: "Swiping Left",
    1: "Swiping Right",
    2: "Pulling Hand In",
    3: "Sliding Two Fingers Left",
    4: "Sliding Two Fingers Right",
    5: "Zooming In With Full Hand",
    6: "Zooming In With Two Fingers",
    7: "Zooming Out With Two Fingers",
    8: "Thumb Up",
    9: "Thumb Down",
    10: "Stop Sign",
    11: "Drumming Fingers",
    12: "No gesture",
    13: "Doing other things",
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
result = 99
prob = 1
prob_2=1
model = PredictThread(batch)
model.start()

action = AppThread(result, prob)
action.start()
while True:
    _, frame = cap.read()
    crop_frame = frame[100:400, 150:500]
    batch = frame_queue(crop_frame, batch)
    res, prob = model.get_prediction_value()
    if prob > 0.7:
        text = LABELS14[res]
        prob_2 = prob
        if res not in (12,13):
            action.resume()
        action.gesture_no = res
        action.prob = prob
    cv2.putText(frame, text + " " + str(prob_2), (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.rectangle(frame, (150, 100), (500, 400), (0, 255, 0), 2)
    cv2.imshow("cam", frame)
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
model.join()
action.join()








