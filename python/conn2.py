import cv2
import requests
from cvzone.HandTrackingModule import HandDetector

CAM_IP = "CAM_IP_ADD"

LCD_IP = "LCD_IP_ADD"

cap = cv2.VideoCapture(
    f"http:CAM_IP_ADD:81/stream"
)

print("Opened:", cap.isOpened())

detector = HandDetector(
    maxHands=1,
    detectionCon=0.5
)

last_text = ""

while True:

    success, img = cap.read()

    if not success:
        continue

    img = cv2.flip(img, 1)
    img = cv2.resize(img, None, fx=2, fy=2)

    hands, img = detector.findHands(img, draw=True)
    print(hands)

    text = "No Hand"

    if hands:

        hand = hands[0]

        fingers = detector.fingersUp(hand)

        count = fingers.count(1)

        cv2.putText(
            img,
            f"Fingers: {count}",
            (10,40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,255,0),
            2
        )

        if count == 0:
            text = "FIST"

        elif count == 1:
            text = "ONE"

        elif count == 2:
            text = "TWO"

        elif count == 3:
            text = "THREE"

        elif count == 4:
            text = "FOUR"

        elif count == 5:
            text = "FIVE"

    cv2.putText(
        img,
        text,
        (10,90),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255,0,0),
        2
    )

    # Send to LCD only if the text changed
    if text != last_text:

        try:
            requests.get(
                f"http://{LCD_IP}/display",
                params={"text": text},
                timeout=1
            )

            print("LCD:", text)

            last_text = text

        except Exception as e:
            print("ESP32 Error:", e)

    cv2.imshow("ESP32 Gesture Control", img)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
