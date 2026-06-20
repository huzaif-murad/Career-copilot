from services.pdf_extractor import extract_text_from_pdf
from services.llm_service import analyze_resume


pdf_path = "docs/Huzaif_Murad.pdf"
text=extract_text_from_pdf(pdf_path)

result=analyze_resume(text)
print(result)