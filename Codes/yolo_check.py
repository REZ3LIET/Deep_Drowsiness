import cv2 as cv
from ultralytics import YOLO

#### Image ####
# model = YOLO("yolov8n.pt")
# path = "./Data/Images/Yolo_Check/Desk_1.jpg"
# img = cv.resize(cv.imread(path), (640, 640))
# prediction = model.predict(img, conf=0.5)
# result = prediction[0].plot()
# # cv.imshow("Original", img)
# cv.imshow("Result", result)

# cv.waitKey(0)
# cv.destroyAllWindows()

#### Video ####
model = YOLO("yolov8n.pt")
path = "./Data/Videos/Traffic_1.mp4"
cap = cv.VideoCapture(path)

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    prediction = model.predict(frame, conf=0.5)
    result = prediction[0].plot()

    cv.imshow("Result", result)
    if cv.waitKey(25) & 0xFF == ord("q"):
        break

cap.release()
cv.destroyAllWindows()