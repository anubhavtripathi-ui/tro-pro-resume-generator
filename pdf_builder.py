from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
)
from reportlab.lib.styles import getSampleStyleSheet


def create_resume_pdf(
    output_file,
    candidate_name,
    target_role,
    summary,
):
    doc = SimpleDocTemplate(
        output_file,
        pagesize=A4
    )

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            candidate_name,
            styles["Title"]
        )
    )

    story.append(
        Paragraph(
            target_role,
            styles["Heading2"]
        )
    )

    story.append(
        Spacer(1, 12)
    )

    story.append(
        Paragraph(
            summary,
            styles["BodyText"]
        )
    )

    doc.build(story)
