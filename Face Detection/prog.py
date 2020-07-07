import cv2 as cv

original_image = cv.imread("image.jpg")
grayscale_image = cv.cvtColor(original_image, cv.COLOR_BGR2GRAY)
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
detected_faces = face_cascade.detectMultiScale(grayscale_image, 1.3)

for (column, row, width, height) in detected_faces:
    cv.rectangle(original_image, (column, row), (column + width, row + height), (0,255,0), 2)

small_image = cv.resize(original_image, (0,0), fx=0.3, fy=0.3)
cv.imshow("Image", small_image)
cv.waitKey(0)
cv.destroyAllWindows()