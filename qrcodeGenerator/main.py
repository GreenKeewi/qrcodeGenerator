import qrcode

def generate_qr_code(data, filename="qrcode.png", fill_color="#000000", back_color="#FFFFFF"):
    qr = qrcode.make(data)
    img = qr.convert("RGB")
    img = img.point(lambda p: fill_color if p == 0 else back_color)
    img.save(filename)

# Example usage
link = 'https://github.com/GreenKeewi/qrcodeGenerator'
generate_qr_code(link, fill_color="#1B1F3B", back_color="#A0EEC0")