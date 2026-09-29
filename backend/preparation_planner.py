from services.llm_service import generate_answer


def generate_preparation_plan(relevant_chunks):

    question = """
Create a practical interview preparation plan based only on
the provided job description context.

Return the result using exactly these sections:

1. Target Role
2. Priority Skills
3. Technical Topics to Study
4. Role-Specific Preparation
5. Interview Preparation
6. Final Preparation Checklist

For Priority Skills:
- List the most important technical and soft skills explicitly
  mentioned in the job description.

For Technical Topics to Study:
- Group related technical topics logically.
- Focus on the technologies, programming languages, frameworks,
  databases, APIs, tools, and technical concepts mentioned in
  the job description.

For Role-Specific Preparation:
- Mention the responsibilities and practical areas the candidate
  should be prepared to discuss.

For Interview Preparation:
- Include preparation areas for technical, role-specific,
  project discussion, and HR interviews.

For Final Preparation Checklist:
- Give concise actionable items the candidate can check before
  the interview.

Important rules:
- Use only information supported by the provided job description.
- Do not invent technologies or requirements.
- Do not assume a specific interview schedule unless it is
  explicitly mentioned.
- Keep the plan practical and concise.
- Prioritize the skills most relevant to the advertised role.
"""

    answer = generate_answer(
        question,
        relevant_chunks
    )

    return answer