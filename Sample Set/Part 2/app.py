import streamlit as st
import os
from pinecone import Pinecone
from utils import extract_text_from_pdf, upsert_embeddings, retrieve_relevant_docs, generate_answer, cohere_client

pc = Pinecone(api_key='7de99cc8-1389-4912-9a1b-1f3e3e7ca42c')

# Set the name for the Pinecone index we will use
index_name = "test2" 

# Create the index if it doesn't already exist
if index_name not in pc.list_indexes().names():
    pc.create_index(name=index_name, dimension=384, metric='euclidean')
index = pc.Index(index_name)

# Streamlit App
st.title("Interactive QA Bot")

# File uploader for PDF documents
uploaded_file = st.file_uploader("Upload a PDF document", type=["pdf"])

if uploaded_file is not None:
    doc_text = extract_text_from_pdf(uploaded_file)
    st.write("Extracted Document Text:")
    st.write(doc_text)  

    # Upsert embeddings
    upsert_embeddings(doc_text, index)
    st.success("Document uploaded and embeddings created successfully.")

    query = st.text_input("Ask a question based on the document:")
    
    if query:
        retrieved_docs = retrieve_relevant_docs(query, index)
        if retrieved_docs:
            answer = generate_answer(query, retrieved_docs, cohere_client)

            
            st.write("Retrieved Segments:")
            for doc in retrieved_docs:
                st.write(f"- {doc['text'][:200]}...")  
            
            st.write("Generated Answer:")
            st.write(answer)
        else:
            st.write("No relevant documents found.")
