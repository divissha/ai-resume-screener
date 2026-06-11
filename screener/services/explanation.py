def generate_explanation(resume_skills, missing_skills):

    strengths = []
    recommendations = []

    # Strengths
    if "python" in resume_skills:
        strengths.append("Strong Python background")

    if "django" in resume_skills:
        strengths.append("Good Django experience")

    if "react" in resume_skills:
        strengths.append("Familiar with React")

    if "sql" in resume_skills:
        strengths.append("Database knowledge using SQL")

    # Recommendations
    if "aws" in missing_skills:
        recommendations.append(
            "Focus on cloud technologies (AWS)"
        )

    if "docker" in missing_skills:
        recommendations.append(
            "Learn containerization using Docker"
        )

    if "postgresql" in missing_skills:
        recommendations.append(
            "Add PostgreSQL projects to your portfolio"
        )

    if "machine learning" in missing_skills:
        recommendations.append(
            "Build Machine Learning projects to strengthen your profile"
        )

    return {
        "strengths": strengths,
        "missing": missing_skills,
        "recommendations": recommendations,
    }