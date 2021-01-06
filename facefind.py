import cvlib as cv
import cv2
# open webcam
webcam = cv2.VideoCapture(0)
if not webcam.isOpened():
    print("Could not open webcam")
    exit()
# loop through frames
while webcam.isOpened():
    # read frame from webcam
    status, frame = webcam.read()
    if not status:
        print("Could not read frame")
        exit()
    # apply face detection
    face, confidence = cv.detect_face(frame)
    # loop through detected faces
    for idx, f in enumerate(face):
        (startX, startY) = f[0], f[1]
        (endX, endY) = f[2], f[3]

        face_region = frame[startY:endY, startX:endX]

        for faces in face:
            (startX, startY) = faces[0], faces[1]
            (endX, endY) = faces[2], faces[3]
            # draw rectangle over face
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)

    # display output
    cv2.imshow("Real-time face detection", frame)

    # press "Q" to stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release resources
webcam.release()
cv2.destroyAllWindows()
