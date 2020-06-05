from PIL import Image
import pytesseract
import docx

mydoc = docx.Document()
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image = Image.open("F:\python\scanne\medhist00039-0105.gif")

image_to_text = pytesseract.image_to_string(image, lang='eng')
print(type(image_to_text))

mydoc.add_paragraph(image_to_text)
mydoc.save("F:/python/scanne/my_written_file.docx")

#print(image_to_text)



