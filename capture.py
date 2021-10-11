import cv2, time

video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()

    print(check)
    print(frame)

    time.sleep(3)
    cv2.imshow("Capturing", frame)
    cv2.waitKey(0)

video.release()
cv2.destroyAllWindows()