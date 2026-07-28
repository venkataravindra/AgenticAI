import chromadb


client = chromadb.Client()

collection = client.create_collection("students")


collection.add(
    ids=["1","2"],
    documents = ["Ravi likes Python","Priya likes Java"]
)

# print(collection._embedding_function)
# print(collection.get(include=["embeddings","documents"]))
# print(collection.get())

#similarity

# result = collection.query(query_texts=["Python developer"],
#                           n_results=2)
# print(result)


collection.add(ids=["3"],
               documents=["Machine Learning with Python"])
#print(collection.get())

collection.delete(ids=["2"])
print(collection.get())
print(collection.count())

client.delete_collection("students")