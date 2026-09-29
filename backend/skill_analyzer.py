from services.llm_service import generate_json_answer


def analyze_skills(relevant_chunks):

    prompt = """
Extract the skills from the job description into exactly this
JSON structure:

{
    "programming_languages": [],
    "frameworks_and_libraries": [],
    "databases": [],
    "backend_and_apis": [],
    "tools_and_technologies": [],
    "other_technical_skills": [],
    "soft_skills": []
}

Categorization rules:

programming_languages:
- Programming languages explicitly mentioned.

frameworks_and_libraries:
- Frameworks and libraries explicitly mentioned.

databases:
- Databases, SQL, relational databases, or database technologies
  explicitly mentioned.

backend_and_apis:
- Backend development technologies, REST APIs, HTTP,
  API development, or related backend concepts explicitly mentioned.

tools_and_technologies:
- Development tools, version control tools, platforms,
  or other technologies explicitly mentioned.

other_technical_skills:
- Technical concepts that do not fit the categories above.

soft_skills:
- Communication, teamwork, problem solving, analytical thinking,
  time management, willingness to learn, or other explicitly
  mentioned soft skills.

Important:
- Use only information supported by the job description.
- Do not invent skills.
- Do not duplicate the same skill unnecessarily.
"""

    return generate_json_answer(
        prompt,
        relevant_chunks
    )