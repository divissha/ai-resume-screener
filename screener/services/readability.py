# def readability_score(text, sections):

#     score = 50

#     found_sections = sum(
#         sections.values()
#     )

#     score += found_sections * 10

#     if len(text.split()) > 300:
#         score += 10

#     return min(score, 100)

def readability_score(text, sections):

    score = 0

    # Section Analysis (50 marks)

    found_sections = sum(sections.values())

    score += found_sections * 10

    # Resume Length (20 marks)

    word_count = len(text.split())

    if word_count >= 300:
        score += 20

    elif word_count >= 200:
        score += 15

    elif word_count >= 100:
        score += 10

    # Action Verbs (15 marks)

    action_verbs = [
        "developed",
        "built",
        "implemented",
        "created",
        "designed",
        "optimized",
        "deployed",
        "managed"
    ]

    action_count = sum(
        1
        for verb in action_verbs
        if verb in text
    )

    score += min(action_count * 3, 15)

    # Numbers / Achievements (15 marks)

    has_numbers = any(
        char.isdigit()
        for char in text
    )

    if has_numbers:
        score += 15

    return min(score, 100)

def readability_feedback(score):

    if score >= 80:
        return "Excellent ATS readability."

    elif score >= 60:
        return "Good ATS readability."

    elif score >= 40:
        return "Average readability. Improve resume structure."

    return "Poor ATS readability."