# Part 1: RAG Model for QA Bot
This section outlines the implementation of a Retrieval-Augmented Generation (RAG) model for a Question Answering (QA) bot. The bot retrieves relevant information from documents and generates coherent answers using a vector database (Pinecone) and a generative model (Cohere API).

## Features
Document Retrieval: Retrieve relevant information from a dataset based on user queries.
Coherent Answer Generation: Use the Cohere API to generate answers based on retrieved context.

## Technologies
Python: Programming language for implementation.
Pinecone: Vector database for efficient document storage and retrieval.
Cohere API: NLP model for generating answers.
SentenceTransformers: For embedding document text and user queries.

## Setup Instructions
### Clone the Repository:
git clone https://github.com/Susma261/QA-Bot/tree/main
cd qa-bot

### Create a Virtual Environment
python -m venv venv
source venv/bin/activate  

### Install Dependencies: Ensure requirements.txt is in your repository. Run:
pip install -r requirements.txt

## Usage
Run the Code: Execute the script that implements the RAG model.
Test Queries: Use several test queries to evaluate the model's performance.

## Colab Link: 
https://colab.research.google.com/drive/1oZlIQyVxohm3W37PbTSoa-AJNPefX5ML?usp=sharing

# Part 2: Interactive QA Bot Interface
This section details the development of an interactive interface for the QA bot from Part 1. Users can upload documents and query the bot in real time.

## Features
Document Upload: Users can upload PDF documents for analysis.
Real-Time Question Answering: Users can ask questions and receive immediate answers based on the uploaded document.
Contextual Responses: Display retrieved document segments alongside generated answers.

## Technologies
Streamlit: Framework for building the web interface.
PyPDF2: For extracting text from uploaded PDF documents.

## Setup Instructions
### Clone the Repository
git clone https://github.com/Susma261/QA-Bot/tree/main
cd qa-bot

### Create a Virtual Environment
python -m venv venv
source venv/bin/activate  

### Install Dependencies: Ensure requirements.txt includes all necessary libraries. Run:
pip install -r requirements.txt

### streamlit run app.py
streamlit run app.py

## Docker Instructions
### Build the Docker Image:
docker build -t qa-bot .

### Run the Docker Container:
docker run -p 8501:8501 qa-bot

## Usage
Open your browser and navigate to http://localhost:8501.
Upload a PDF document using the provided file uploader.
After the document is uploaded, view the extracted text.
Enter your question related to the document in the text input field.
Click the submit button to see the generated answer and retrieved segments.

## Conclusion
The development of the RAG-based QA bot and its interactive interface successfully addresses the need for a system that can efficiently retrieve and generate answers from documents. By leveraging Pinecone for storage and Cohere for generation, the bot offers coherent, contextually relevant responses. The interactive interface enhances user experience by allowing document uploads and real-time queries. This project demonstrates the potential of combining retrieval and generation techniques in AI-powered applications.









