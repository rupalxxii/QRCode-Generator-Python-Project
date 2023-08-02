import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1, error_correction=qrcode.ERROR_CORRECT_H,box_size=10,border=5)
qr.add_data("https://www.linkedin.com/in/rupal-hiwarkar-2a28a625b/")
qr.make(fit=True)
img=qr.make_image(fill_color="White",back_color="Pink")
img.save("LinkdeIn.jpg")