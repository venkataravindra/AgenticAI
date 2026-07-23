# from transformers import pipeline
# generator = pipeline(
#     "text-generation",
#     model="distilgpt2"
# )
# prompt = "i love walking"
# result = generator(prompt,max_new_tokens=3,num_return_sequences=3)
# for i,output in enumerate(result,1):
#   print(f"Output : {i}")
#   print(f"Result : {output["generated_text"]}")


# from transformers import AutoTokenizer
# tokenizer = AutoTokenizer.from_pretrained("distilgpt2")
# text = "i love hyderabad biryani !"
# tokens = tokenizer.tokenize(text)
# token_ids = tokenizer.encode(text)
# print(f"Original Text {text}")
# print(f"Tokens : {tokens}")
# print(f"Tonen ID'S : {token_ids}")

# from sentence_transformers import SentencesDataset
# from sentence_transformers import SentenceTransformer
# model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
# sentences = ["Hello","How are you"]
# vectors = model.encode(sentences)
# print(vectors)


# from sentence_transformers import SentenceTransformer
# from sklearn.metrics.pairwise import cosine_similarity

# # Load the pre-trained embedding model
# model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# # Documents
# sentences = [
#     "i love biryani",
#     "i love hyderabad biryani"
# ]

# # Convert sentences into embeddings
# vectors = model.encode(sentences)

# # User query
# query = ["i love spicy food"]

# # Convert query into embedding
# test_vector = model.encode(query)

# # Find cosine similarity
# scores = cosine_similarity(vectors, test_vector)[0]

# # Print similarity scores
# for sentence, score in zip(sentences, scores):
#     print(f"{sentence} ---> {score:.3f}")



# from sentence_transformers import SentenceTransformer
# model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
# sentences = ["Machine Learning with Quantum Computing", "Deep Learning", "Natural Language Processing"]
# embeddings = model.encode(sentences)
# for sentence, embedding in zip(sentences,embeddings):
#     print("\nSentence:", sentence)
#     print("Embedding:", embedding)
#     print("Embedding length:", len(embedding)) 



#maximum capacity to accept tokens by llm is called context window
#to train model we use torch library  -- suitable for text
#if we want to train model using  video, website we need to use 