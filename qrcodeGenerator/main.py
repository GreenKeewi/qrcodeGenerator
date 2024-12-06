import qrcode

def generate_qr_code(data, fill_color="#000000", back_color="#FFFFFF"):
    qr = qrcode.QRCode(version=1, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save("qrcode.png")

# Example usage
link = 'https://github.com/GreenKeewi/qrcodeGenerator'
generate_qr_code(link, fill_color="#1B1F3B", back_color="#A0EEC0")