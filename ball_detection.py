import cv2
import numpy as np
import torch

def detect_ball(frame):
    # Convert frame to HSV color space
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Define the color range for detecting the ball
    lower_color = np.array([60, 50, 50]) # Set the HSV values for your ball color
    upper_color = np.array([75, 255, 255])
    
    # Threshold the HSV image to get only the ball colors
    mask = cv2.inRange(hsv_frame, lower_color, upper_color)
    
    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 50: # min_area to filter out small detections
            # Calculate the center of the contour
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                return (cx, cy) # Return the coordinates of the ball center
    return None

# Load your video file
video_path = 'videos/test3.mp4'
cap = cv2.VideoCapture(video_path)
ret, frame = cap.read()
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # 'yolov5s' is the smallest model



# Check if we got a frame, if not, handle the error (e.g., print an error message)
if not ret:
    print("Failed to capture video")
    cap.release()
    cv2.destroyAllWindows()
    exit()
frame_center = frame.shape[1] / 2
direction_error = 50

while True:
    ret, frame = cap.read()

    # Inference
    results = model(frame)

    # Results
    labels, cord = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]
    n = len(labels)
    for i in range(n):
        row = cord[i]
        if labels[i] == 32:  # The class ID for a sports ball in COCO dataset
            x1, y1, x2, y2 = int(row[0]*frame.shape[1]), int(row[1]*frame.shape[0]), int(row[2]*frame.shape[1]), int(row[3]*frame.shape[0])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break
    
    """ foo
    # If the frame was not retrieved, break from the loop (end of video)
    if not ret:
        break
    
    ball_position = detect_ball(frame)
    
    if ball_position:
        # print(f"Ball detected at: {ball_position}")
        # Here you would add your code to transform coordinates and control the robot
        # Optionally, draw a circle around the detected ball
        cv2.circle(frame, ball_position, 10, (0, 255, 0), -1) # 10 is the radius, (0, 255, 0) is the color (green)

        # Determine if the ball is left or right of the center and print the direction
        # print(ball_position[0], frame_center)
        if ball_position[0] < frame_center - direction_error:
            print("LEFT")
        elif ball_position[0] > frame_center + direction_error:
            print("RIGHT")
        else:
            print("CENTER")

    # Display the frame
    cv2.imshow("Frame", frame)
    
    # Break the loop with the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break """

cap.release()
cv2.destroyAllWindows()
