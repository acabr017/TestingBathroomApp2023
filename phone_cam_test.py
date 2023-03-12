import cv2
import numpy as np
import urllib.request
import pytesseract

url = "https://10.0.0.103:8080"
cp = cv2.VideoCapture(url)

'''
while(True):
    camera, frame = cp.read() 
    if frame is not None:
        cv2.imshow("Frame", frame)
    q = cv2.waitKey(1)
    if q==ord("q"):
        break
cv2.destroyAllWindows()
'''

while(True):
    ret, frame = cp.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU[1])

    text = pytesseract.image_to_string(threshold, lang="eng")

    cv2.imshow("frame", frame)
    print(text)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break