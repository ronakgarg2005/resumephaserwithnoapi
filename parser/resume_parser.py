from parser.pdf_reader import extract_pdf_text
from parser.docx_reader import extract_docx_text
from parser.nlp_parser import extract_projects
from parser.nlp_parser import extract_certifications

from parser.regex_parser import extract_regex_details

from parser.nlp_parser import (
    extract_name,
    extract_skills,
    extract_education,
    extract_experience,
    extract_projects,
    extract_certifications,
    extract_languages
)


def parse_resume(filepath):
    """
    Master Resume Parser
    --------------------
    Reads the resume, extracts text, then extracts
    all structured information.
    """

    extension = filepath.split(".")[-1].lower()

    # -----------------------------
    # Read Resume
    # -----------------------------
    if extension == "pdf":
        resume_text = extract_pdf_text(filepath)

    elif extension == "docx":
        resume_text = extract_docx_text(filepath)

    else:
        raise Exception("Unsupported file format")

    # -----------------------------
    # Regex Extraction
    # -----------------------------
    resume_data = extract_regex_details(resume_text)

    # -----------------------------
    # NLP Extraction
    # -----------------------------
    resume_data["name"] = extract_name(resume_text)

    resume_data["skills"] = extract_skills(resume_text)

    resume_data["education"] = extract_education(resume_text)

    # -----------------------------
    # Placeholders (Next Modules)
    # -----------------------------
    resume_data["experience"] = extract_experience(resume_text)

    resume_data["projects"] = extract_projects(resume_text)

    resume_data["certifications"] = extract_certifications(resume_text)

    resume_data["languages"] = extract_languages(resume_text)

    # -----------------------------
    # Raw Resume Text
    # -----------------------------
    resume_data["resume_text"] = resume_text

    return resume_data, resume_text