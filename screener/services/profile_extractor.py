import re


def extract_email(text):

    match = re.search(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text
    )

    return match.group() if match else "Not Found"


def extract_phone(text):

    match = re.search(
        r"(\+?\d[\d\s\-]{8,}\d)",
        text
    )

    return match.group() if match else "Not Found"


def extract_linkedin(text):

    match = re.search(
        r"linkedin\.com/in/[A-Za-z0-9_-]+",
        text
    )

    return match.group() if match else "Not Found"


def extract_github(text):

    match = re.search(
        r"github\.com/[A-Za-z0-9_-]+",
        text
    )

    return match.group() if match else "Not Found"


def extract_name(text):

    lines = text.split("\n")

    for line in lines[:5]:

        if len(line.split()) <= 4 and len(line) > 2:

            return line.strip()

    return "Not Found"