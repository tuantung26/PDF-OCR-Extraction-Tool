import os
import time
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables (API Key)
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
else:
    print("Error: GEMINI_API_KEY not found in .env file.")

class OCR:
    def __init__(self):
        print("Initializing Gemini OCR Engine...")
        self.model = genai.GenerativeModel('gemini-2.5-flash')

    def ocr_pdf_with_llm(self, pdf_path):
        """Uses Gemini LLM to transcribe the PDF page into plain text."""
        print(f"Gemini is reading: {pdf_path}...")
        
        try:
            # 1. Upload the file to Gemini storage
            uploaded_file = genai.upload_file(path=pdf_path)
            
            # 2. Wait for processing if necessary
            while uploaded_file.state.name == "PROCESSING":
                time.sleep(1)
                uploaded_file = genai.get_file(uploaded_file.name)

            # 3. Request transcription in plain text
            prompt = "Trích xuất toàn bộ nội dung văn bản từ file này. Trả về văn bản thuần túy, chính xác (plain text), không sử dụng định dạng markdown (như **, ###, v.v.)."
            response = self.model.generate_content([uploaded_file, prompt])
            
            # 4. Clean up: Delete file from cloud storage
            genai.delete_file(uploaded_file.name)
            
            return response.text
        except Exception as e:
            print(f"Error processing {pdf_path}: {e}")
            return f"[Error: {e}]"

    def process_folder(self, folder_path: str):
        """Iterates through the folder and combines all results into result.txt."""
        result_text = ""
        
        if not os.path.exists(folder_path):
            print(f"Error: Folder '{folder_path}' does not exist.")
            return

        # Get PDF files and sort them numerically
        pdf_files = [f for f in os.listdir(folder_path) if f.lower().endswith(".pdf")]
        pdf_files.sort(key=lambda x: int(x.split('_')[1].split('.')[0]))

        for filename in pdf_files:
            file_path = os.path.join(folder_path, filename)
            text = self.ocr_pdf_with_llm(file_path)
            result_text += f"--- {filename} ---\n"
            result_text += text + "\n\n"
            
        # Write final output
        with open("result.txt", "w", encoding="utf-8") as file:
            file.write(result_text)
            
        print("\n--- Hoàn thành! Kết quả đã được lưu vào result.txt ---")

if __name__ == "__main__":
    ocr_processor = OCR()
    ocr_processor.process_folder("pages")
