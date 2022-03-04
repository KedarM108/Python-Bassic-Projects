import qrcode
import cv2

img= qrcode.make("Kedar Mule")
img.save("qr_code.jpg")

d=cv2.QRCodeDetector()
val, points, straight_qrcode = d.detectAndDecode(cv2.imread("qr_code.jpg"))
print(val)