import spacy
import os
import re

def extract_certifications(text):
    """
    Extract Certifications section.
    """

    pattern = r"(?is)certifications?(.*?)(projects|experience|education|skills|languages|achievements|$)"

    match = re.search(pattern, text)

    if match:
        certification_text = match.group(1).strip()

        certifications = []

        for line in certification_text.split("\n"):
            line = line.strip()

            if line:
                certifications.append(line)

        return certifications

    return []




def extract_languages(text):
    """
    Extract Languages section.
    """

    pattern = r"(?is)languages?(.*?)(projects|experience|education|skills|certifications|achievements|$)"

    match = re.search(pattern, text)

    if match:
        language_text = match.group(1).strip()

        languages = []

        for line in language_text.split("\n"):
            line = line.strip()

            if line:
                languages.append(line)

        return languages

    return []

def extract_projects(text):
    """
    Extract the Projects section from the resume.
    """

    pattern = r"(?is)projects?(.*?)(certifications|experience|education|skills|languages|achievements|$)"

    match = re.search(pattern, text)

    if match:
        project_text = match.group(1).strip()

        projects = []

        for line in project_text.split("\n"):
            line = line.strip()

            if line:
                projects.append(line)

        return projects

    return []

def extract_experience(text):
    """
    Extract the Experience section from the resume.
    """

    pattern = r"(?is)experience(.*?)(education|projects|skills|certifications|languages|$)"

    match = re.search(pattern, text)

    if match:
        experience = match.group(1).strip()

        lines = [
            line.strip()
            for line in experience.split("\n")
            if line.strip()
        ]

        return lines

    return []

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Path to skills.txt
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SKILLS_FILE = os.path.join(BASE_DIR, "data", "skills.txt")


# -----------------------------
# Extract Name
# -----------------------------
def extract_name(text):
    """
    Extract candidate name using spaCy.
    Returns the first PERSON entity found.
    """

    doc = nlp(text)

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text

    return ""


# -----------------------------
# Extract Skills
# -----------------------------
def extract_skills(text):
    """
    Match resume text with skills.txt
    """

    with open(SKILLS_FILE, "r", encoding="utf-8") as file:
        skills = [skill.strip() for skill in file.readlines()]

    resume_lower = text.lower()

    found = []

    for skill in skills:
        if skill.lower() in resume_lower:
            found.append(skill)

    return sorted(list(set(found)))


# -----------------------------
# Extract Education
# -----------------------------
def extract_education(text):

    education_keywords = [
        "B.Tech",
        "Bachelor of Technology",
        "B.E",
        "Bachelor of Engineering",
        "BCA",
        "MCA",
        "B.Sc",
        "M.Sc",
        "MBA",
        "M.Tech",
        "Diploma",
        "PhD",
        "10th",
        "12th"
    ]

    found = []

    for edu in education_keywords:
        if edu.lower() in text.lower():
            found.append(edu)

    return list(set(found))