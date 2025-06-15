import qrcode
from datetime import datetime

now=datetime.now()
current_time=now.strftime("Date: %y-%m-%d \n Time: %H:%M:%S")

qr =qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(current_time)
qr.make(fit=True)

img=qr.make_image(fill_color='black',back_color='green')
img.save("datetime_img.png")
img.show()

print("Scan the QR shown here ")
