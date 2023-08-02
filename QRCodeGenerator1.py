import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1, error_correction=qrcode.ERROR_CORRECT_H,box_size=10,border=5)
qr.add_data("https://github.com/rupalxxii")
qr.make(fit=True)
img=qr.make_image(fill_color= "Orange",back_color="Yellow")
img.save("Github.png")