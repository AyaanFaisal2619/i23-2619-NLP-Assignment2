import PyPDF2

try:
    reader = PyPDF2.PdfReader('Assignment 2.pdf')
    with open('Assignment2_parsed.txt', 'w', encoding='utf-8') as f:
        for i, page in enumerate(reader.pages):
            f.write(f"--- Page {i+1} ---\n")
            f.write(page.extract_text() + "\n")
except Exception as e:
    print("PyPDF2 failed:", e)
