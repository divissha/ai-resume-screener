def generate_feedback(score, missing_skills):

    if score > 80:
        return "Excellent match! You are highly suitable for this role."

    elif score > 60:
        return "Good match. Strengthen missing skills to improve selection chances."

    elif score > 40:
        return "Moderate match. Focus on core technical skills."

    else:
        return "Low match. Consider building foundational skills first."
    
def skill_advice(missing_skills):
    advice_map = {
        "aws": "Learn AWS for cloud deployment skills",
        "docker": "Learn Docker for containerization",
        "django": "Improve Django for backend development",
        "react": "Learn React for frontend development",
        "sql": "Strengthen SQL for data handling"
    }

    return [advice_map.get(skill, f"Learn {skill}") for skill in missing_skills]