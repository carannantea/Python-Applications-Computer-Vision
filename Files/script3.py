import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("photo.jpg")

# gray_img = cv2.cvtColor(img.cv2.COLOR_BGR2GRAY)
gray_img = cv2.imread("/Users/anthonycarannante/Desktop/Github_Repos/Python-Applications-Computer-Vision/Files/photo.jpg", 0)

cv2.imshow("Gray",gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()