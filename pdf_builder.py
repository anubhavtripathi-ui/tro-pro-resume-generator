def create_resume_pdf(
    output_file,
    candidate_name,
    target_role,
    summary,
):
    with open(output_file, "w") as f:
        f.write(candidate_name)
