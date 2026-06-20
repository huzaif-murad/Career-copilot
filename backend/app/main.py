from services.pdf_extractor import extract_text_from_pdf

pdf_path = "docs/Huzaif_Murad.pdf"
text=extract_text_from_pdf(pdf_path)
print(text)
