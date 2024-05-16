from ultralytics.models.yolo.model import YOLO

# model = YOLO('yolov8n.pt')

model = YOLO('runs/detect/train3/weights/best.pt')

# results = model.predict('dataset/images/train/train_1/four_channel_image546.png')

# for result in results:
#     boxes = result.boxes
#     print(boxes)# Boxes object for bounding box outputs
#     masks = result.masks  # Masks object for segmentation masks outputs
#     keypoints = result.keypoints  # Keypoints object for pose outputs
#     probs = result.probs  # Probs object for classification outputs
#     obb = result.obb  # Oriented boxes object for OBB outputs
#     result.show()  # display to screen
#     result.save(filename='result.png')

results = model.train(data="dataset/data.yaml", epochs=10)
model.val()