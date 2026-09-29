# CareerAgent

AI Job Preparation and Document Intelligence Assistant

CareerAgent is an AI-powered job preparation assistant that analyzes job description PDFs, extracts important role requirements, identifies technical and soft skills, answers questions using Retrieval-Augmented Generation (RAG), generates interview questions, and creates a role-specific preparation plan.

## Features

- Upload job descriptions in PDF format
- Extract text from uploaded documents
- Split documents into smaller text chunks
- Generate semantic embeddings using Sentence Transformers
- Store and search document embeddings using FAISS
- Retrieve relevant job description information using RAG
- Analyze job title, experience, education, responsibilities, and requirements
- Identify programming languages, frameworks, databases, APIs, tools, and soft skills
- Generate technical, role-specific, and HR interview questions
- Generate a structured interview preparation plan
- Ask questions about the uploaded job description through an interactive chat interface
- Use a local Ollama LLM without requiring paid OpenAI API credits
- Provide a web-based interface using HTML, CSS, and JavaScript

## Project Architecture

```text
Frontend
HTML + CSS + JavaScript
        |
        | HTTP / REST API
        v
Flask Backend
        |
        +-----------------------------+
        |                             |
        v                             v
PDF Processing                    RAG Pipeline
        |                             |
        v                             v
Text Extraction                Text Embeddings
        |                             |
        v                             v
Text Chunking                     FAISS
                                      |
                                      v
                              Relevant Chunks
                                      |
                                      v
                                Ollama LLM
                                      |
                    +-----------------+-----------------+
                    |                 |                 |
                    v                 v                 v
                JD Analysis      Skill Analysis   Interview /
                                                   Preparation



Technology Stack
Frontend
HTML5
CSS3
JavaScript
Backend
Python
Flask
AI and RAG
LangChain Text Splitters
Sentence Transformers
FAISS
Ollama
Llama 3.2 3B
Document Processing
PyPDF
Supporting Libraries
NumPy
pandas
python-dotenv
How CareerAgent Works
1. Upload Job Description

The user uploads a job description PDF through the CareerAgent web interface.

2. Extract Text

PyPDF extracts readable text from the uploaded PDF.

3. Text Chunking

The extracted text is divided into smaller overlapping chunks using a recursive text splitter.

This allows the system to work with specific sections of the document instead of sending the entire document to the language model.

4. Generate Embeddings

Sentence Transformers converts each text chunk into a numerical vector representation.

CareerAgent uses:

all-MiniLM-L6-v2
5. Store Embeddings

The generated embeddings are stored in a FAISS vector index.

FAISS allows CareerAgent to efficiently search for chunks that are semantically relevant to a user's question.

6. Retrieve Relevant Information

When the user asks a question, the question is converted into an embedding.

CareerAgent searches the FAISS index and retrieves the most relevant job description chunks.

7. Generate AI Response

The retrieved chunks are provided to the local Ollama LLM.

The model generates an answer using the retrieved job description information as context.

This creates the RAG pipeline:

Question
   |
   v
Question Embedding
   |
   v
FAISS Similarity Search
   |
   v
Relevant JD Chunks
   |
   v
Ollama LLM
   |
   v
Grounded Answer
AI Modules
Job Description Analysis

CareerAgent extracts:

Job title
Required experience
Education
Key responsibilities
Technical skills
Tools and technologies
Soft skills
Other requirements

The result is displayed using structured dashboard cards.

Skill Analysis

Skills are categorized into:

Programming Languages
Frameworks and Libraries
Databases
Backend and APIs
Tools and Technologies
Other Technical Skills
Soft Skills
Interview Question Generation

CareerAgent generates:

Easy technical questions
Medium technical questions
Hard technical questions
Role-specific questions
HR questions

The questions are generated using the requirements and technologies identified from the job description.

Preparation Plan

CareerAgent creates a preparation plan containing:

Target role
Priority skills
Technical topics to study
Role-specific preparation
Interview preparation
Final preparation checklist
Project Structure
CareerAgent/
│
├── backend/
│   ├── __init__.py
│   ├── routes.py
│   ├── rag.py
│   ├── jd_analyzer.py
│   ├── skill_analyzer.py
│   ├── interview_agent.py
│   └── preparation_planner.py
│
├── services/
│   ├── document_processor.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── text_chunker.py
│   └── llm_service.py
│
├── frontend/
│   ├── index.html
│   ├── analysis.html
│   ├── chat.html
│   ├── preparation.html
│   │
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       ├── main.js
│       ├── analysis.js
│       ├── chat.js
│       └── preparation.js
│
├── data/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
Installation
1. Clone the Repository
git clone https://github.com/YOUR_USERNAME/CareerAgent.git
cd CareerAgent
2. Create a Virtual Environment

Windows:

python -m venv .venv

Activate it:

.venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
4. Install and Configure Ollama

Install Ollama and make sure it is running.

Pull the required model:

ollama pull llama3.2:3b

Verify the model:

ollama list
5. Run CareerAgent
python app.py

Open the application in your browser:

http://127.0.0.1:5000
Example Workflow
Upload Job Description
        |
        v
Extract PDF Text
        |
        v
Create Text Chunks
        |
        v
Generate Embeddings
        |
        v
Create FAISS Vector Index
        |
        v
Analyze Job Description
        |
        +----> Skill Analysis
        |
        +----> Interview Questions
        |
        +----> Preparation Plan
        |
        +----> RAG Chat
RAG Approach

CareerAgent uses Retrieval-Augmented Generation instead of directly asking the LLM to answer questions without context.

The system first retrieves relevant information from the uploaded job description and then provides that information to the LLM.

This helps the application generate responses based on the uploaded document rather than relying only on the model's general knowledge.

Local AI

CareerAgent uses Ollama with:

llama3.2:3b

The LLM runs locally, so the application does not require a paid OpenAI API key.

This makes the project suitable for local development and demonstration.

Future Improvements

Possible future improvements include:

Persistent document and vector storage
Support for multiple uploaded job descriptions
User authentication
Resume upload and resume-to-JD matching
Skill gap analysis
Personalized study schedules
Interview answer evaluation
Job recommendation based on candidate skills
Cloud deployment
Persistent chat history

Author

Siddhi Shendurkar