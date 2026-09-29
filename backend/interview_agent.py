from services.llm_service import generate_answer


def generate_interview_questions(relevant_chunks):

    question = """
Generate interview questions strictly from the provided job description context.

The job description is the source of truth.

Return the result using exactly these sections:

1. Technical Questions

Easy
- Generate 5 questions.

Medium
- Generate 5 questions.

Hard
- Generate 5 questions.

2. Role-Specific Questions
- Generate 5 questions.

3. HR Questions
- Generate 5 questions.

Important rules:

- Use only technologies, skills, responsibilities, tools,
  qualifications, and requirements explicitly mentioned in
  the provided job description context.
- Do not introduce technologies, frameworks, tools, or concepts
  that are not supported by the context.
- For example, if OAuth, AOP, Docker, AWS, React, or another
  technology is not mentioned in the context, do not create
  questions specifically about it.
- Technical questions should test understanding of the
  technologies and skills actually mentioned in the JD.
- Role-specific questions should be based on the responsibilities
  and work described in the JD.
- HR questions should be relevant to the advertised role and
  its requirements.
- Avoid duplicate questions.
- Do not provide answers.
- Keep questions clear and interview-ready.
"""

    answer = generate_answer(
        question,
        relevant_chunks
    )

    return answer