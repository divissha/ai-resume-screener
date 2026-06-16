import os
from django.shortcuts import render
from django.conf import settings

from .services.pdf_parser import extract_text
from .services.skills import extract_skills
from .services.matcher import match_score, missing_skills
from .services.ai_engine import semantic_score
from .services.feedback import generate_feedback, skill_advice

from .services.explanation import generate_explanation

from django.http import FileResponse
from .services.report import generate_pdf

from .services.role_recommender import recommend_roles
from .services.section_analyzer import analyze_sections
from .services.readability import readability_score, readability_feedback
from .services.project_recommender import recommend_projects
from .models import ResumeAnalysis
from .services.semantic_matcher import semantic_score

from .services.semantic_suggestions import (
    get_semantic_suggestions
)

from .services.matcher import (
    match_score,
    missing_skills,
    missing_skill_percentage
)

from .services.profile_extractor import (
    extract_name,
    extract_email,
    extract_phone,
    extract_github,
    extract_linkedin,
)

from django.contrib.auth.decorators import login_required
from .models import ResumeAnalysis


def upload_resume(request):

    

    if request.method == "POST":
        try:
            
            resume = request.FILES["resume"]
            
            jd_text = request.POST['job_description']

            file_path = os.path.join(settings.MEDIA_ROOT, resume.name)

            with open(file_path, "wb+") as f:
                for chunk in resume.chunks():
                    f.write(chunk)

            print("FILE PATH:", file_path)
            print("FILE EXISTS:", os.path.exists(file_path))

            # TEXT
            resume_text = extract_text(file_path)
            name = extract_name(resume_text)
            email = extract_email(resume_text)
            phone = extract_phone(resume_text)
            github = extract_github(resume_text)
            linkedin = extract_linkedin(resume_text)
            semantic_ats_score = semantic_score(resume_text,jd_text)
            sections = analyze_sections(resume_text)
            readability = readability_score(resume_text,sections)
            readability_message = readability_feedback(readability)


            # SKILLS
            resume_skills = extract_skills(resume_text)
            recommended_roles = recommend_roles(resume_skills)
            jd_skills = extract_skills(jd_text.lower())

            # OLD SCORE (skill-based)
            skill_score = match_score(resume_skills, jd_skills)

            # AI SCORE (semantic)
            ai_score = semantic_ats_score

            # FINAL SCORE (blend both)
            final_score = round((skill_score + ai_score) / 2, 2)

            missing = missing_skills(resume_skills, jd_skills)

            projects = recommend_projects(missing)
            semantic_suggestions = (get_semantic_suggestions(missing))

            explanation = generate_explanation(resume_skills,missing)

            missing_percent = missing_skill_percentage(resume_skills,jd_skills)

            feedback = generate_feedback(final_score, missing)
            advice = skill_advice(missing)

            matched = list(set(resume_skills) & set(jd_skills))

            request.session["score"] = final_score
            request.session["matched"] = matched
            request.session["missing"] = missing
            request.session["explanation"] = explanation

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


            if request.user.is_authenticated:
                 recommended_role = (
                      recommended_roles[0]
                      if recommended_roles
                      else "Not Available")
                 
                 
                 ResumeAnalysis.objects.create(
                     user=request.user,
                     score=final_score,
                     semantic_score=float(semantic_ats_score),recommended_role=recommended_role,matched_skills=", ".join(matched),missing_skills=", ".join(missing),)


                # ResumeAnalysis.objects.create(
                #     user=request.user,
                #     score=final_score,
                #     semantic_score=float(semantic_ats_score),
                #     recommended_role=recommended_roles(
                #         recommended_roles[0]
                #         if recommended_roles
                #         else "Not Available"),
                #     recommended_role=recommended_roles,matched_skills=", ".join(matched),missing_skills=", ".join(missing),)
                

                
            return render(request, "screener/result.html", {
                "score": final_score,
                "missing": missing,
                "matched": resume_skills,
                "feedback": feedback,
                "advice": advice,
                "missing_percent": missing_percent,
                "explanation": explanation,
                "score_status": score_status,
                "explanation": explanation,
                "matched": matched,
                "recommended_roles": recommended_roles,
                "sections": sections,
                "readability": readability,
                "readability_message": readability_message,
                "projects": projects,
                "semantic_suggestions": semantic_suggestions,
                "semantic_score": semantic_ats_score,
                "name": name,
                "email": email,"phone": phone,
                "github": github,
                "linkedin": linkedin,
                # "rankings":scores,
            })

        except Exception as e:
            print("ERROR:", str(e))
            raise

    return render(request, "screener/upload.html")

def download_report(request):

    score = request.session.get("score")

    matched = request.session.get("matched")

    missing = request.session.get("missing")

    explanation = request.session.get("explanation")

    pdf = generate_pdf(
        score,
        matched,
        missing,
        explanation
    )

    return FileResponse(
        pdf,
        as_attachment=True,
        filename="resume_report.pdf"
    )


@login_required
def history(request):

    analyses = ResumeAnalysis.objects.filter(
        user=request.user
    ).order_by("-created_at")

    return render(
        request,
        "screener/history.html",
        {
            "analyses": analyses
        }
    )






