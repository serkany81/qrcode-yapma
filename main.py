import qrcode 
from qrcode import constants


# code = qrcode.make('https://jquery.com/')
# code.save('qrcode1.png')

code = qrcode.QRCode(
    version=1,
    error_correction=constants.ERROR_CORRECT_L,
    box_size=10, border=4
)

code.add_data('https://picsum.photos/')
code.make(fit=True)

image = code.make_image(fill_color="blue",back_color='black')

image.save('qrcode.png')
