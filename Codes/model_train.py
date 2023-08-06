from ultralytics import YOLO

model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)

# Train the model
model.train(data='./Data/dataset/dataset.yaml', epochs=100, imgsz=250)
