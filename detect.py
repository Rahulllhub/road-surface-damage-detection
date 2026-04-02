from ultralytics import YOLO
import cv2
import argparse
import os


def detect_potholes(image_path):

    print("[INFO] Loading YOLOv8 model...")
    model = YOLO("yolov8n.pt")

    if not os.path.exists(image_path):
        print("Image not found")
        return

    print("[INFO] Running detection...")

    image = cv2.imread(image_path)

    results = model(image, conf=0.1)

    pothole_count = 0

    for result in results:
        for box in result.boxes:

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            pothole_count += 1

            cv2.rectangle(image, (x1, y1), (x2, y2),
                          (0, 0, 255), 2)

            cv2.putText(image,
                        "Pothole",
                        (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        (255, 255, 255),
                        2)

    cv2.putText(image,
                f"Potholes detected: {pothole_count}",
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2)

    cv2.imshow("Detection Result", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--image",
                        required=True,
                        help="Path to input image")

    args = parser.parse_args()

    detect_potholes(args.image)