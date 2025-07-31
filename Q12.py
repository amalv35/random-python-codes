import qrcode
from PIL import Image


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=10,
)

qr.add_data("https://www.linkedin.com/in/amal-v-a108282b6/")
qr.make(fit=True)


qr_img = qr.make_image(fill_color="#808080", back_color="white").convert('RGB')


logo = Image.open("linkedIn.png").convert("RGBA")  # Make sure this file exists

qr_width, qr_height = qr_img.size
logo_size = int(qr_width * 0.25)
logo = logo.resize((logo_size, logo_size), resample=Image.LANCZOS)


alpha = logo.split()[3]
opacity_factor = 0.7  
alpha = alpha.point(lambda p: int(p * opacity_factor))
logo.putalpha(alpha)


qr_img = qr_img.convert("RGBA")

pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
qr_img.paste(logo, pos, mask=logo)

qr_img = qr_img.convert("RGB")
qr_img.save("amal_linkedIn.png")
