import ollama


response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content": "Explain what a job description is in two sentences."
        }
    ]
)


print(response["message"]["content"])