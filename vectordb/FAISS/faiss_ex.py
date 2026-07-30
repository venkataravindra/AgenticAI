# import faiss

# print(faiss.__version__)
# import faiss
# dimension = 4
# index = faiss.IndexFlatL2(dimension)
# print(index)


# import numpy as np
# import faiss

# dimension = 4
# index = faiss.IndexFlatL2(dimension)
# data = np.array([
#     [1,2,3,4],
#     [2,3,4,5],
#     [10,11,12,13]
# ],dtype='float32')
# index.add(data)
# print(index.ntotal)
# print(index.reconstruct(0))
# print(index.reconstruct(1))
# print(index.reconstruct(2))

# import numpy as np
# import faiss

# dimension = 4
# index = faiss.IndexFlatL2(dimension)
# data = np.array([
#     [1,2,3,4],
#     [2,3,4,5],
#     [10,11,12,13]
# ],dtype='float32')
# index.add(data)
# new_data = np.array([
#     [50,51,52,53],
#     [100,101,102,103]
# ],dtype='float32')
# index.add(new_data)
# print(index.ntotal)


# import numpy as np
# import faiss

# dimension = 4
# index = faiss.IndexFlatL2(dimension)
# data = np.array([
#     [1,2,3,4],
#     [2,3,4,5],
#     [10,11,12,13]
# ],dtype='float32')
# index.add(data)
# new_data = np.array([
#     [50,51,52,53],
#     [100,101,102,103]
# ],dtype='float32')
# index.add(new_data)
# print(index.ntotal)
# query = np.array([[2,3,4,5]],dtype='float32')
# distance,indexes = index.search(query,2)
# print(distance)
# print(indexes)

# import numpy as np
# import faiss

# dimension = 4

# Create a flat L2 index
# index = faiss.IndexFlatL2(dimension)

# # Wrap it with IndexIDMap to support IDs
# index = faiss.IndexIDMap(index)

# vectors = np.array([
#     [1,2,3,4],
#     [2,3,4,5],
#     [3,4,5,6]
# ], dtype='float32')

# # Add vectors with custom IDs
# ids = np.array([101, 102, 103], dtype='int64')
# index.add_with_ids(vectors, ids)
# print(f"After adding with IDs: {index.ntotal}")

# # Add more vectors with different IDs
# new_vectors = np.array([
#     [4,5,6,7],
#     [5,6,7,8]
# ], dtype='float32')
# new_ids = np.array([104, 105], dtype='int64')
# index.add_with_ids(new_vectors, new_ids)
# print(f"After adding more vectors: {index.ntotal}")


# index.remove_ids(faiss.IDSelectorBatch(np.array([102], dtype='int64')))
# print(f"After removing ID 102: {index.ntotal}")
# faiss.write_index(index, "employees.index")
# loaded_index = faiss.read_index("employees.index")
# print(loaded_index)
# search_vector = np.array([[1,2,3,4]], dtype='float32')
# distances, indices = loaded_index.search(search_vector, k=3)
# print(f"Distances: {distances}")
# print(f"Indices: {indices}")
# print(f"\nTotal vectors in index: {loaded_index.ntotal}")

# faiss.write_index(index,"employees.index")
# index = faiss.read_index("employees.index")

# print(index.ntotal)

import numpy as np
import faiss

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    "Python is easy",
    "Java is object oriented",
    "AI is the future"
]

embeddings = model.encode(documents)
print(embeddings.shape)
dimension = 384
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings, dtype='float32'))
print(index.ntotal)