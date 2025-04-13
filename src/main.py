import qrcode


def generate_qr(input):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1,
    )
    qr.add_data(input)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrcode.png")
    print("QR code saved as 'qrcode.png'")

if __name__ == "__main__":

    data = input("Enter the data:")
    print(f"Data: {data}")

    if not data:
        print("Empty data... Generating empty data QR")

    generate_qr(data)
