def generate_explanation(score, missing_skills):

    if not missing_skills:
        return "Your resume contains all required skills from the job description."

    return (
        f"Your resume is missing {len(missing_skills)} "
        f"important skill(s): {', '.join(missing_skills)}. "
        "Adding these skills could improve your ATS score."
    )