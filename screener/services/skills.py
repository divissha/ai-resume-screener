SKILLS = [
    "python", "django", "flask", "fastapi",
    "sql", "mysql", "postgresql",
    "javascript", "react", "node", "express",
    "aws", "azure", "gcp",
    "docker", "kubernetes",
    "git", "linux",
    "machine learning", "deep learning",
    "nlp", "pandas", "numpy" 
]

# def extract_skills(text):
#     found_skills = []

#     for skill in SKILLS:
#         if skill in text:
#             found_skills.append(skill)

#     return found_skills

def extract_skills(text):
    text = text.lower()
    return [skill for skill in SKILLS if skill in text]