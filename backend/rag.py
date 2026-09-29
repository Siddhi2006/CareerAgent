import faiss
import numpy as np

from services.embeddings import create_embeddings
from services.vector_store import create_faiss_index, search_faiss


current_index = None
current_chunks = []


def build_vector_store(chunks):

    global current_index
    global current_chunks

    embeddings = create_embeddings(chunks)

    current_index = create_faiss_index(
        embeddings
    )

    current_chunks = chunks

    return {
        "chunk_count": len(chunks),
        "embedding_dimension": embeddings.shape[1],
        "vector_count": current_index.ntotal
    }


def retrieve_relevant_chunks(
    question,
    top_k=3
):

    if current_index is None:
        raise ValueError(
            "No document has been uploaded yet."
        )

    question_embedding = create_embeddings(
        [question]
    )[0]

    results = search_faiss(
        current_index,
        question_embedding,
        current_chunks,
        top_k
    )

    return results


def retrieve_multiple_queries(
    queries,
    top_k_per_query=3,
    max_chunks=12
):

    if current_index is None:
        raise ValueError(
            "No document has been uploaded yet."
        )

    collected_chunks = []

    for query in queries:

        results = retrieve_relevant_chunks(
            query,
            top_k=top_k_per_query
        )

        for chunk in results:

            if chunk not in collected_chunks:

                collected_chunks.append(chunk)

    return collected_chunks[:max_chunks]