import cv2
from cvzone.HandTrackingModule import HandDetector
import time
import pyautogui  # Using pyautogui for key presses

# Initialize webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Width
cap.set(4, 720)   # Height

time.sleep(2.0)

# Initialize hand detector
detector = HandDetector(maxHands=1, detectionCon=0.5, minTrackCon=0.5)

gesture_cooldown = 0

while True:
    success, img = cap.read()
    if not success:
        print("Failed to grab frame, exiting...")
        break

    hands, img = detector.findHands(img)

    if hands:
        lmList = hands[0]["lmList"]
        fingers = detector.fingersUp(hands[0])
        finger_count = fingers.count(1)
        if gesture_cooldown == 0:
            if finger_count == 1:
                print("Move Left ←")
                pyautogui.press('left')
                gesture_cooldown = 10
            elif finger_count == 2:
                print("Move Right →")
                pyautogui.press('right')
                gesture_cooldown = 10
            elif finger_count == 5:
                print("Jump ↑")
                pyautogui.press('up')
                gesture_cooldown = 10
            elif finger_count == 4:
                print("Slide ↓")
                pyautogui.press('down')
                gesture_cooldown = 10

    if gesture_cooldown > 0:
        gesture_cooldown -= 1

    cv2.imshow("Temple Run Hand Control", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()