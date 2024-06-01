import qrcode

# Custom data for the QR-Code
data = {
    "Name": "Kumar Abhishek",
    "Email": "fabiamkumar@gmail.com",
    "Phone": "+91-7870583406",
    "Pincode": "816109"
}

# Converting the dictionary to a string representation
data_str = "\n".join([f"{key}: {value}" for key, value in data.items()])

# Creating a QR code object
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Adding the data to the QR code
qr.add_data(data_str)
qr.make(fit=True)

# Creating an image out of the QR code instance
img = qr.make_image(fill_color="black", back_color="white")

# Saving the image
img.save("custom_qr_code.png")