# PDF OCR & Extraction Tool

This project provides a two-step workflow for splitting a large PDF document into individual pages and performing high-quality OCR/structure extraction using IBM's Docling and EasyOCR.

## Features
- **PDF Splitting**: Automatically splits a large PDF into individual page files for easier processing.
- **Advanced OCR**: Uses Docling to extract text and document structure (headings, tables, etc.) into Markdown format.
- **Vietnamese Support**: Configured to handle both Vietnamese and English text accurately.
- **OOP Structure**: Clean, reusable Object-Oriented code in `OCRLLM.py`.

## Project Structure
- `test_pypdf.py`: The script used to split the source PDF into individual pages.
- `OCRLLM.py`: The main OCR engine that processes the split pages and generates a combined output.
- `pages/`: (Generated) Directory containing the split PDF pages.
- `result.txt`: (Generated) The final combined Markdown extraction.
- `requirements.txt`: List of Python dependencies.

## Installation

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd OCR
   ```

2. **Install dependencies**:
   Make sure you have Python 3.10+ installed. Then run:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Step 1: Split the PDF
Open `test_pypdf.py` and update the path to your source PDF file. Then run:
```bash
python test_pypdf.py
```
This will create a `pages/` folder containing each page as a separate PDF.

### Step 2: Perform OCR
Run the main processor to extract text from all pages in the `pages/` folder:
```bash
python OCRLLM.py
```
Wait for the process to complete. The final result will be saved in `result.txt`.

## Configuration
You can modify the OCR settings in `OCRLLM.py` within the `OCR` class constructor:
```python
ocr_options = EasyOcrOptions()
ocr_options.lang = ["vi", "en"] # Add or remove languages here
```

## License
MIT
