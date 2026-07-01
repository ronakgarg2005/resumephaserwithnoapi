from docx import Document

def extract_docx_text(docx_path):
    text = ""

    try:
        doc = Document(docx_path)

        for para in doc.paragraphs:
            text += para.text + "\n"

    except Exception as e:
        print("DOCX Error:", e)

    return text