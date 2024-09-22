import PyPDF2
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone
import cohere

# Initialize Pinecone with the provided API key
pc = Pinecone(api_key='7de99cc8-1389-4912-9a1b-1f3e3e7ca42c')

# Initialize Cohere API client for generating responses
cohere_client = cohere.Client('SB102vS4TC1TDuUh6br0DTPHU4wzChX4UHREfUar')

def extract_text_from_pdf(uploaded_file):
    # Create a PDF reader object
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:  
            text += page_text
    return text

def upsert_embeddings(doc_text, index):
    embedder = SentenceTransformer('all-MiniLM-L6-v2')
    doc_embeddings = embedder.encode([doc_text])[0].tolist()  
    vector_id = "doc_1"  
    
    # Store the text of the document in metadata
    vectors = [
        {
            'id': vector_id,
            'values': doc_embeddings,
            'metadata': {'text': doc_text}  
        }
    ]
    
    index.upsert(vectors)

def retrieve_relevant_docs(query, index, top_k=3):
    embedder = SentenceTransformer('all-MiniLM-L6-v2')
    query_embedding = embedder.encode([query])[0].tolist()  
    results = index.query(vector=query_embedding, top_k=top_k, include_metadata=True) 

    retrieved_docs = [{'id': match['id'], 'text': match['metadata']['text']} for match in results['matches']]
    return retrieved_docs

def generate_answer(query, context_docs, cohere_client):
    context = " ".join([doc['text'] for doc in context_docs if isinstance(doc['text'], str)])  # Ensure all parts are strings
    prompt = f"Based on the following context, provide a detailed answer:\n\nContext: {context}\n\nQuestion: {query}\nAnswer:"

    response = cohere_client.generate(
        model='command-xlarge',  
        prompt=prompt,
        max_tokens=150
    )
    return response.generations[0].text.strip()
