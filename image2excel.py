import cv2
import pytesseract
import pandas as pd
img = "/react/ecommerce/abcd.jpeg"
image = cv2.imread(img)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, threshold_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
custom_config = r'--oem 3 --psm 6'
text_data = pytesseract.image_to_string(threshold_image)
rows = text_data.split("\n")
table_data = [row.split("\t") for row in rows]
for row in table_data:
    for i, cell in enumerate(row):
        row[i] = ''.join(char for char in cell if ord(char) < 128)
 
df = pd.DataFrame(table_data)
df = df.applymap(lambda x: x if x.strip() != "" else pd.NA)
output_excel_file = "sheet.xlsx"
df.to_excel(output_excel_file, index=False, header=False)
print(table_data)