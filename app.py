import streamlit as st
from PyPDF import PdfReader
from langchain.text_splitter import RecursiveTextSplitter
import os

from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain.vectorstores import FAISS                                # for vector embeddings 
from langchain_google_genai import GoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain           # for question chats and prompts
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv




load_dotenv()

genai.congifure_api_key(os.getenv("GENAI_API_KEY"))


#REad PDF go through pages and extract text.
def get_pdf_text(pdf_docs):
    text = ""
    for pdf_doc in pdf_docs:

        pdf = PdfReader(pdf)

        for page in pdf_reader.pages:
            text += page.extract_text()
    
    return text

def get_text_chunks(text):
    splitter = RecursiveTextSplitter(chunk_size=10000, chunk_overlap=1000) #here we are splitting the text into chunks of 10000 characters with an overlap of 1000 characters
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embeddings-001")
    vector_store = FAISS.from_text(text_chunks, embeddings=embeddings)
    vector_store.save_local("fiass_index")
    return vector_store


def get_conversational_chain():
    prompt_template = '''
    Answer the question as detailed as possible from the provided context, make sure to provide the details and the reasoning behind your answer, if the answer 
    is not present in the context just say "Answer not available in the context", do not provide wrong answers.
    Context: \n {context}? \n
    Question: \n {question}

    Answer:

    '''
    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)

    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

    chain = load_qa_chain(model, chain_type='stuff',prompt=prompt)

    return chain

def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(mode1="models/embedding-0Ø1")

    new_db = FAISS.load_local("faiss_index", embeddings)
    docs = new_db.similarity_search(user_question)

    chain = get_conversational_chain()

    response = chain(
        {"input_documents": docs, "question": user_question},
        return_only_outputs=True)

    print(response)

    st.write("Reply:", response["output_text"])


def main():
    st.set_page_config('Chat with multiple PDF')
    st.header("Chat with multiple PDF using GEMINI")

    user_question = st.text_input("Ask a question based on the PDF:")

    if user_question:
        user_input(user_question)
    
    with st.sidebar:
        st.title("Menu")
        pdf_docs = st.file_uploader("Upload PDF")
        if st.button("Submit and Process PDF"):
            with st.spinner("Processing PDF..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_pdf_text(raw_text)
                get_vector_store(text_chunks)
                st.success("PDF Processed Successfully")

if __name__ == "__main__":
    main()
