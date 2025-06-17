import qrcode

location_data="https://maps.app.goo.gl/jmuNTUdeiAJCcZTS7?g_st=aw "


qr=qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(location_data)
qr.make(fit=True)

img=qr.make_image(back_color="green",fill_color="black")
img.save('location_qr.png')
img.show()

print("QR saved at loaction_qr.png \n scan the QR and follow location")
