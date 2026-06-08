from datetime import datetime


def generate_resume_data(
    candidate_name,
    target_role,
    summary,
    skills,
    experience,
    certifications,
    education,
):
    return {
        "candidate_name": candidate_name,
        "target_role": target_role,
        "summary": summary,
        "skills": skills,
        "experience": experience,
        "certifications": certifications,
        "education": education,
        "generated_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
