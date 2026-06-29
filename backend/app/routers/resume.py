from fastapi import APIRouter,UploadFile,File,HTTPException
from app.services.pdf_extractor import extract_text_from_pdf
from app.services.llm_service import analyze_resume

router=APIRouter()

@router.post("/resume")
async def upload_resume(file:UploadFile = File(...)) :
   text=extract_text_from_pdf(file.file)
   if not text:
      raise HTTPException(status_code=400,detail="No text found in pdf.")
   result=analyze_resume(text)

   return {
      "result":result
   }

