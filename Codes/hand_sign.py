import cv2 as cv
from ultralytics import YOLO

#### Image ####
model = YOLO("./models/Hand_Sign_Detector.pt")
img = cv.imread("./Data/Images/Test/Test_A.jpg")
prediction = model.predict(img)
result = prediction[0].plot()
# cv.imshow("Image", img)
cv.imshow("Result", result)
cv.waitKey(0)
cv.destroyAllWindows()

#### Video ####
# model = YOLO("./models/Hand_Sign_Detector.pt")
# cap = cv.VideoCapture(0)

# while cap.isOpened():
#     ret, frame = cap.read()

#     if not ret:
#         break

#     prediction = model.predict(frame, conf=0.5)
#     result = prediction[0].plot()

#     cv.imshow("Result", result)
#     if cv.waitKey(25) & 0xFF == ord("q"):
#         break

# cap.release()
# cv.destroyAllWindows()