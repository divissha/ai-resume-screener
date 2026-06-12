from io import BytesIO
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(
    score,
    matched,
    missing,
    explanation
):

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "AI Resume Analysis",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            f"ATS Score: {score}%",
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 10))

    content.append(
        Paragraph(
            "Matched Skills",
            styles["Heading2"]
        )
    )

    for s in matched:
        content.append(
            Paragraph(
                f"• {s}",
                styles["Normal"]
            )
        )

    content.append(
        Paragraph(
            "Missing Skills",
            styles["Heading2"]
        )
    )

    for s in missing:
        content.append(
            Paragraph(
                f"• {s}",
                styles["Normal"]
            )
        )

    doc.build(content)

    buffer.seek(0)

    return buffer