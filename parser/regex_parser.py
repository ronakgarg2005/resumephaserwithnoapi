import re


def extract_email(text):
    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return ""
def extract_phone(text):

    pattern = r"(\+91[\s-]?)?[6-9]\d{9}"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return ""
def extract_linkedin(text):

    pattern = r"(https?://)?(www\.)?linkedin\.com/in/[A-Za-z0-9_-]+"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return ""
def extract_github(text):

    pattern = r"(https?://)?(www\.)?github\.com/[A-Za-z0-9_-]+"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return ""
def extract_portfolio(text):

    pattern = r"https?://[^\s]+"

    urls = re.findall(pattern, text)

    ignore = ["linkedin", "github"]

    for url in urls:

        if not any(site in url.lower() for site in ignore):
            return url

    return ""
def extract_regex_details(text):

    return {

        "email": extract_email(text),

        "phone": extract_phone(text),

        "linkedin": extract_linkedin(text),

        "github": extract_github(text),

        "portfolio": extract_portfolio(text)

    }