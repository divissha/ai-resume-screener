def analyze_sections(text):

    text = text.lower()

    sections = {

        "Education": False,
        "Projects": False,
        "Skills": False,
        "Experience": False,
        "Certifications": False

    }

    if "education" in text:
        sections["Education"] = True

    if "project" in text or "projects" in text:
        sections["Projects"] = True

    if "skills" in text:
        sections["Skills"] = True

    if "experience" in text:
        sections["Experience"] = True

    if (
        "certification" in text
        or "certifications" in text
    ):
        sections["Certifications"] = True

    return sections