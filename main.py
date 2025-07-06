import cv2
import torch

# Load the YOLOv8 model
model = torch.hub.load('ultralytics/yolov8', 'yolov8n', pretrained=True)


def process_frame(frame):
    # Perform object detection
    results = model(frame)

    # Parse the results
    detections = results.pandas().xyxy[0]

    # Example: Filter for lines (you'll need to adapt this for your specific use case)
    line_detections = detections[detections['name'].isin(['line'])]

    # Draw detections on the frame
    for _, row in line_detections.iterrows():
        x1, y1, x2, y2 = int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax'])
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    return frame, line_detections


def control_car(line_detections):
    # Simple logic to control the car
    if len(line_detections) > 0:
        # Example: Adjust steering based on line position
        # (You need to replace this with actual car control logic)
        print("Driving between lines")
    else:
        print("No lines detected, adjust driving")


def main():
    # Open video capture (0 for webcam, replace with video file path if needed)
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Process the frame
        processed_frame, line_detections = process_frame(frame)
        # Display the result
        cv2.imshow('YOLOv8 Line Detection', processed_frame)

        # Control the car
        control_car(line_detections)

        # Break loop on 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

