import json
import ollama


MODEL_NAME = "llama3.2:3b"


def generate_answer(question, relevant_chunks):

    context = "\n\n".join(
        relevant_chunks
    )

    prompt = f"""
You are CareerAgent, an AI job preparation assistant.

Answer the user's question using the provided job description context.

Rules:
- Use the provided context as the primary source.
- Do not invent requirements that are not present in the context.
- If the answer cannot be determined from the context, clearly say that
  the information is not available in the uploaded job description.
- Keep the answer clear and useful for job preparation.

Job Description Context:
{context}

User Question:
{question}
"""

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


def generate_json_answer(
    prompt,
    relevant_chunks
):

    context = "\n\n".join(
        relevant_chunks
    )

    full_prompt = f"""
You are CareerAgent, an AI job preparation assistant.

The provided job description context is the source of truth.

Your task is to extract information from the context
and return ONLY valid JSON.

Important rules:
- Use only information explicitly supported by the context.
- Do not invent information.
- Do not add markdown.
- Do not add explanations outside the JSON.
- If information is not mentioned, use "Not specified"
  for text fields and [] for list fields.
- Keep the extracted information concise.

Job Description Context:
{context}

Task:
{prompt}
"""

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": full_prompt
            }
        ],
        format="json"
    )

    content = response["message"]["content"]

    try:

        return json.loads(content)

    except json.JSONDecodeError:

        raise ValueError(
            "The AI returned an invalid JSON response."
        )