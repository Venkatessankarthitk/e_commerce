from img2table.ocr import TesseractOCR
from img2table.document import Image

# Instantiation of the image
img = Image(src="/react/ecommerce/abcd.jpeg")


# Table identification
imgage_tables = img.extract_tables()

# Result of table identification
imgage_tables

#output
# [ExtractedTable(title=None, bbox=(10, 8, 745, 314),shape=(6, 3)),
#  ExtractedTable(title=None, bbox=(936, 9, 1129, 111),shape=(2, 2))]
print(imgage_tables)
