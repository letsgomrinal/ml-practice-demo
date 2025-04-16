from PyPDF2 import PdfReader

def load_pdf_text(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def chunk_text(text, chunk_size=500, overlap=100):
    chunks = []
    start = 0
    while start < len(text):
        chunk = text[start:start+chunk_size]
        chunks.append(chunk)
        start += chunk_size - overlap
    return chunks

if __name__=='__main__':
    text = load_pdf_text("nvdia.pdf")
    print(text)
    chunks = chunk_text(text)
    print(chunks)
