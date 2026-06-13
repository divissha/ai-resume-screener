SKILL_RELATIONS = {

    "docker": [
        "Containerization",
        "Kubernetes",
        "CI/CD"
    ],

    "aws": [
        "EC2",
        "S3",
        "Lambda"
    ],

    "postgresql": [
        "Database Design",
        "SQL Optimization",
        "Data Modeling"
    ],

    "machine learning": [
        "TensorFlow",
        "PyTorch",
        "Scikit-Learn"
    ],

    "react": [
        "Redux",
        "REST APIs",
        "Frontend Architecture"
    ],

    "django": [
        "REST Framework",
        "Authentication",
        "Backend Development"
    ]
}

def get_semantic_suggestions(missing_skills):

    suggestions = {}

    for skill in missing_skills:

        if skill.lower() in SKILL_RELATIONS:

            suggestions[skill] = (
                SKILL_RELATIONS[skill.lower()]
            )

    return suggestions