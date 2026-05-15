# PDF OCR & Text Extraction Pipeline

A high-performance document extraction tool that leverages IBM's **Docling** for document structure analysis and **Google Gemini (LLM)** for superior text transcription. This pipeline is optimized for complex PDF layouts and supports multiple languages including Vietnamese and English.

## Features
- **Accurate PDF Splitting**: Breaks down large PDF documents into individual pages for efficient batch processing.
- **LLM-Powered OCR**: Uses Google Gemini 1.5 Flash to "read" PDF pages natively, offering better accuracy for multi-column layouts and tables compared to traditional OCR.
- **Local OCR Options**: Includes support for EasyOCR and PaddleOCR for users who prefer local execution.
- **Clean Output**: Automatically converts complex PDF data into structured plain text, removing unnecessary formatting artifacts.

## Project Structure
- `test_pypdf.py`: Splits the source PDF into individual page files.
- `OCRLLM.py`: The primary engine using Google Gemini for text extraction.
- `OCRDoclingEasyOCR.py`: Local OCR engine using the EasyOCR library.
- `OCRDoclingPaddle.py`: Local OCR engine using the PaddleOCR/RapidOCR engine.
- `pages/`: (Generated) Directory containing the split PDF pages.
- `result.txt`: (Generated) The final combined text extraction from all pages.
- `requirements.txt`: Project dependencies list.
- `.env`: (User Created) Stores the Gemini API Key securely.

## Installation

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd OCR
   ```

2. **Install dependencies**:
   Ensure you have Python 3.10 or higher. Install the required packages via pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Key**:
   Create a file named `.env` in the root directory and add your Google Gemini API key:
   ```env
   GEMINI_API_KEY=your_actual_api_key_here
   ```
   *Note: You can get a free key at [Google AI Studio](https://aistudio.google.com/app/apikey).*

## Usage

### Step 1: Prepare the PDF
1. Place your PDF in the project folder.
2. Update the filename in `test_pypdf.py`.
3. Run the splitter:
   ```bash
   python test_pypdf.py
   ```
   This will populate the `pages/` folder with individual PDF pages.

### Step 2: Execute OCR Extraction

#### Primary Method: Google Gemini (LLM)
This is the recommended method for the highest accuracy and best handling of Vietnamese text.
```bash
python OCRLLM.py
```

#### Alternative: Local Engines
If you prefer to run the OCR on your local machine without an internet connection (or for privacy reasons), use the local scripts:
```bash
# For EasyOCR
python OCRDoclingEasyOCR.py

# For PaddleOCR
python OCRDoclingPaddle.py
```

## Configuration
You can customize the behavior of the extraction by editing the scripts:
- **For LLM**: In `OCRLLM.py`, you can modify the `prompt` variable to change how the model interprets the document.
- **For Local OCR**: In the respective scripts, you can update the `lang` list (e.g., `["vi", "en"]`) to support different languages.

## License
MIT
