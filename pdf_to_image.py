# This small automated script can easily retrieve entire PDF pages and convert them into images. The script uses the popular PyMuPDF module, which is known for its PDF text extraction.

# PDF to Images
# pip install PyMuPDF
import fitz

def pdf_to_images(pdf_file):
    doc = fitz.open(pdf_file)
    for p in doc:
        pix = p.get_pixmap()
        output = f"page{p.number}.png"
        pix.writePNG(output)

pdf_to_images("test.pdf")