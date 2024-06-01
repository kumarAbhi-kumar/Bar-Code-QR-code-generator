import barcode
from barcode.writer import ImageWriter

# Creating a data field for the barcode
data = "917870583406895"  # Example data, typically my mobile number

# Choosing the barcode format (EAN13 is a common format for product barcodes)
# Note: The EAN format that I used here must have 12 digits
barcode_format = barcode.get_barcode_class('ean13')

# Creating the barcode object
my_barcode = barcode_format(data, writer=ImageWriter())

# Saving the barcode as an image file
my_barcode.save("custom_barcode")

print("Barcode generated and saved as custom_barcode.png")