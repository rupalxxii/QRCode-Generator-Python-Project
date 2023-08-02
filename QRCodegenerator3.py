import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1, error_correction=qrcode.ERROR_CORRECT_H,box_size=10,border=5)
qr.add_data(9405043970)
qr.make(fit=True)
img=qr.make_image(fill_color="Blue",back_color="Green")
img.save("Phone.jpg")