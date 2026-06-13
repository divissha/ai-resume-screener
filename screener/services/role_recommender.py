ROLE_SKILLS = {

    "Backend Developer": [
        "python",
        "django",
        "sql",
        "mysql",
        "postgresql",
        "git"
    ],

    "Full Stack Developer": [
        "python",
        "django",
        "javascript",
        "react",
        "sql",
        "git"
    ],

    "Machine Learning Engineer": [
        "python",
        "machine learning",
        "tensorflow",
        "pytorch",
        "nlp"
    ],

    "Data Scientist": [
        "python",
        "pandas",
        "numpy",
        "machine learning",
        "sql"
    ]
}
    
def recommend_roles(skills):

    skills = set(skills)

    role_scores = []

    for role, required_skills in ROLE_SKILLS.items():

        matched = len(
            skills.intersection(required_skills)
        )

        total = len(required_skills)

        score = round(
            (matched / total) * 100,
            2
        )

        role_scores.append({
            "role": role,
            "score": score
        })

    role_scores.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return role_scores