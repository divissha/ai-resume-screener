# def match_score(resume_skills, jd_skills):
#     if not jd_skills:
#         return 0

#     matched = set(resume_skills) & set(jd_skills)

#     score = len(matched) / len(jd_skills)
#     return round(score * 100, 2)


# def missing_skills(resume_skills, jd_skills):
#     return list(set(jd_skills) - set(resume_skills))

def match_score(resume_skills, jd_skills):
    if not jd_skills:
        return 0

    matched = set(resume_skills) & set(jd_skills)
    return round(len(matched) / len(jd_skills) * 100, 2)


def missing_skills(resume_skills, jd_skills):
    return list(set(jd_skills) - set(resume_skills))


def missing_skill_percentage(resume_skills, jd_skills):
    if not jd_skills:
        return 0

    missing = set(jd_skills) - set(resume_skills)

    return round((len(missing) / len(jd_skills)) * 100, 2)
