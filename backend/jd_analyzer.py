from services.llm_service import generate_json_answer


def analyze_job_description(relevant_chunks):

    prompt = """
Extract the job description information into exactly this JSON structure:

{
    "job_title": "",
    "experience_required": "",
    "education_required": "",
    "key_responsibilities": [],
    "technical_skills": [],
    "tools_and_technologies": [],
    "soft_skills": [],
    "other_requirements": []
}

Field instructions:

job_title:
- Extract the advertised job title.

experience_required:
- Extract the required experience.

education_required:
- Extract required degrees or educational qualifications.

key_responsibilities:
- List the major responsibilities mentioned in the job description.

technical_skills:
- List technical skills explicitly mentioned.

tools_and_technologies:
- List specific technologies, frameworks, databases,
  APIs, development tools, and platforms mentioned.

soft_skills:
- List explicitly mentioned soft skills.

other_requirements:
- List other relevant requirements, qualifications,
  preferred qualifications, or experience.

Do not invent information.
Do not add technologies that are not present in the context.
"""

    return generate_json_answer(
        prompt,
        relevant_chunks
    )