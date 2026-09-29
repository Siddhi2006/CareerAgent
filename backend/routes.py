from flask import Blueprint, request, jsonify
import traceback

from services.document_processor import extract_text_from_pdf
from services.text_chunker import split_text_into_chunks
from services.llm_service import generate_answer

from backend.rag import (
    build_vector_store,
    retrieve_relevant_chunks,
    retrieve_multiple_queries
)

from backend.jd_analyzer import analyze_job_description
from backend.skill_analyzer import analyze_skills
from backend.interview_agent import generate_interview_questions
from backend.preparation_planner import generate_preparation_plan


api = Blueprint("api", __name__)


@api.route("/api/health", methods=["GET"])
def health():

    return jsonify({
        "status": "success",
        "message": "CareerAgent Flask API is running!"
    })


@api.route("/api/upload", methods=["POST"])
def upload_document():

    if "file" not in request.files:

        return jsonify({
            "status": "error",
            "message": "No file was uploaded."
        }), 400

    file = request.files["file"]

    if file.filename == "":

        return jsonify({
            "status": "error",
            "message": "No file was selected."
        }), 400

    if not file.filename.lower().endswith(".pdf"):

        return jsonify({
            "status": "error",
            "message": "Only PDF files are supported."
        }), 400

    try:

        extracted_text = extract_text_from_pdf(file)

        if not extracted_text.strip():

            return jsonify({
                "status": "error",
                "message": "No readable text was found in the PDF."
            }), 400

        chunks = split_text_into_chunks(
            extracted_text
        )

        if not chunks:

            return jsonify({
                "status": "error",
                "message": "No text chunks could be created."
            }), 400

        vector_info = build_vector_store(
            chunks
        )

        return jsonify({
            "status": "success",
            "filename": file.filename,
            "message": "PDF processed successfully.",
            "text_length": len(extracted_text),
            "chunk_count": vector_info["chunk_count"],
            "embedding_dimension": vector_info["embedding_dimension"],
            "vector_count": vector_info["vector_count"]
        })

    except Exception as e:

        print("ERROR IN /api/upload:")
        traceback.print_exc()

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


@api.route("/api/search", methods=["POST"])
def search_document():

    data = request.get_json(
        silent=True
    )

    if not data:

        return jsonify({
            "status": "error",
            "message": "No JSON data was provided."
        }), 400

    question = data.get(
        "question",
        ""
    ).strip()

    if not question:

        return jsonify({
            "status": "error",
            "message": "Please provide a question."
        }), 400

    try:

        relevant_chunks = retrieve_relevant_chunks(
            question,
            top_k=3
        )

        answer = generate_answer(
            question,
            relevant_chunks
        )

        return jsonify({
            "status": "success",
            "question": question,
            "answer": answer,
            "result_count": len(relevant_chunks),
            "relevant_chunks": relevant_chunks
        })

    except ValueError as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400

    except Exception as e:

        print("ERROR IN /api/search:")
        traceback.print_exc()

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


@api.route("/api/analyze-jd", methods=["POST"])
def analyze_jd():

    try:

        relevant_chunks = retrieve_multiple_queries(
            [
                "job title and role",
                "experience required",
                "education required",
                "key responsibilities",
                "technical skills",
                "tools and technologies",
                "qualifications",
                "soft skills",
                "other requirements"
            ],
            top_k_per_query=3,
            max_chunks=12
        )

        analysis = analyze_job_description(
            relevant_chunks
        )

        return jsonify({
            "status": "success",
            "analysis": analysis,
            "result_count": len(relevant_chunks)
        })

    except ValueError as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400

    except Exception as e:

        print("ERROR IN /api/analyze-jd:")
        traceback.print_exc()

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@api.route("/api/analyze-skills", methods=["POST"])
def analyze_skills_api():

    try:

        relevant_chunks = retrieve_multiple_queries(
            [
                "programming languages",
                "frameworks and libraries",
                "databases and SQL",
                "backend and APIs",
                "tools and technologies",
                "technical skills",
                "soft skills"
            ],
            top_k_per_query=3,
            max_chunks=12
        )

        skills = analyze_skills(
            relevant_chunks
        )

        return jsonify({
            "status": "success",
            "skills": skills,
            "result_count": len(relevant_chunks)
        })

    except ValueError as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400

    except Exception as e:

        print("ERROR IN /api/analyze-skills:")
        traceback.print_exc()

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


@api.route("/api/generate-interview", methods=["POST"])
def generate_interview():

    try:

        relevant_chunks = retrieve_multiple_queries(
            [
                "technical skills programming languages",
                "frameworks databases APIs tools",
                "job responsibilities",
                "role requirements",
                "experience qualifications",
                "soft skills"
            ],
            top_k_per_query=3,
            max_chunks=12
        )

        interview_questions = generate_interview_questions(
            relevant_chunks
        )

        return jsonify({
            "status": "success",
            "interview_questions": interview_questions,
            "result_count": len(relevant_chunks)
        })

    except ValueError as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400

    except Exception as e:

        print("ERROR IN /api/generate-interview:")
        traceback.print_exc()

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


@api.route("/api/generate-preparation", methods=["POST"])
def generate_preparation():

    try:

        relevant_chunks = retrieve_multiple_queries(
            [
                "job title and experience",
                "education and qualifications",
                "technical skills",
                "programming languages frameworks",
                "databases APIs tools",
                "responsibilities",
                "soft skills",
                "other requirements"
            ],
            top_k_per_query=3,
            max_chunks=12
        )

        preparation_plan = generate_preparation_plan(
            relevant_chunks
        )

        return jsonify({
            "status": "success",
            "preparation_plan": preparation_plan,
            "result_count": len(relevant_chunks)
        })

    except ValueError as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400

    except Exception as e:

        print("ERROR IN /api/generate-preparation:")
        traceback.print_exc()

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500