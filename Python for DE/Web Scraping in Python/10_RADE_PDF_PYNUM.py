#we will use pymupdf to extract text from pdf files
import fitz  # PyMuPDF
def read_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text()
        
    doc.close()
    
    return text

if __name__ == "__main__":
    filepath = "test.pdf"
    try:
        content = read_pdf(filepath)
        print("_" * 40)
        print(content)
        print("_" * 40)
    except Exception as e:
        print(f"Failed to read PDF: {e}")
        
    
    
    
