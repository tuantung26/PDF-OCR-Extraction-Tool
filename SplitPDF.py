import os
from pypdf import PdfReader, PdfWriter

reader = PdfReader(r"D:\FPT IS\OCR\Bao cao doanh nghiep BSR 3_2026(1) - Copy.pdf")

os.makedirs("pages", exist_ok=True)

for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    writer.add_page(page)
    output_path = os.path.join("pages", f"page_{i+1}.pdf")
    with open(output_path, "wb") as output:
        writer.write(output)
    
    
