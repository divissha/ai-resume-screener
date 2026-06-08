import os
from django.shortcuts import render
from django.conf import settings

from .services.pdf_parser import extract_text
from .services.skills import extract_skills
from .services.matcher import match_score, missing_skills
from .services.ai_engine import semantic_score
from .services.feedback import generate_feedback, skill_advice

from .services.explanation import generate_explanation

from .services.matcher import (
    match_score,
    missing_skills,
    missing_skill_percentage
)


def upload_resume(request):

    

    if request.method == "POST":

        resume = request.FILES['resume']
        jd_text = request.POST['job_description']

        file_path = os.path.join(settings.MEDIA_ROOT, resume.name)

        with open(file_path, "wb+") as f:
            for chunk in resume.chunks():
                f.write(chunk)

        # TEXT
        resume_text = extract_text(file_path)

        # SKILLS
        resume_skills = extract_skills(resume_text)
        jd_skills = extract_skills(jd_text.lower())

        # OLD SCORE (skill-based)
        skill_score = match_score(resume_skills, jd_skills)

        # AI SCORE (semantic)
        ai_score = semantic_score(resume_text, jd_text)

        # FINAL SCORE (blend both)
        final_score = round((skill_score + ai_score) / 2, 2)

        missing = missing_skills(resume_skills, jd_skills)

        explanation = generate_explanation(final_score,missing)

        missing_percent = missing_skill_percentage(resume_skills,jd_skills)

        feedback = generate_feedback(final_score, missing)
        advice = skill_advice(missing)

        if final_score >= 80:
            score_status = "Excellent Match"
        elif final_score >= 60:
            score_status = "Good Match"
        elif final_score >= 40:
            score_status = "Average Match"
        else:
            score_status = "Low Match"

        print("JD TEXT:", jd_text)
        print("JD SKILLS:", jd_skills)
        print("RESUME SKILLS:", resume_skills)
        print("MISSING:", missing)

        return render(request, "screener/result.html", {
            "score": final_score,
            "missing": missing,
            "matched": resume_skills,
            "feedback": feedback,
            "advice": advice,
            "missing_percent": missing_percent,
            "explanation": explanation,
            "score_status": score_status,
        })

    return render(request, "screener/upload.html")






