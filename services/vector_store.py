import faiss
import numpy as np


def create_faiss_index(embeddings):

    embeddings = np.array(
        embeddings
    ).astype("float32")

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(
        dimension
    )

    index.add(embeddings)

    return index


def search_faiss(
    index,
    query_embedding,
    chunks,
    top_k=3
):

    query_embedding = np.array(
        [query_embedding]
    ).astype("float32")

    distances, indices = index.search(
        query_embedding,
        top_k
    )

    results = []

    for index_position in indices[0]:

        if index_position < len(chunks):

            results.append(
                chunks[index_position]
            )

    return results