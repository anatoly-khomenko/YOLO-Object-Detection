import cv2

video = cv2.VideoCapture(0)
video.set(cv2.CAP_PROP_FRAME_WIDTH,416)
video.set(cv2.CAP_PROP_FRAME_HEIGHT,416)

while True:
    check, frame = video.read()
    print(frame.dtype)
    cv2.imshow('Video window', frame)

    # press 'q' on keyboard to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
