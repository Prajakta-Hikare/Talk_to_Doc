from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders import TextLoader
from langchain.document_loaders import Docx2txtLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from huggingface_hub import notebook_login
import torch
import transformers
from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers import pipeline
from langchain import HuggingFacePipeline
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
import os
import sys

documents = []

for file in os.listdir("docs"):
    if file.endswith(".pdf"):
        pdf_path = "./docs/" + file
        loader = PyPDFLoader(pdf_path)
        documents.extend(loader.load())
    elif file.endswith('.docx') or file.endswith('.doc'):
        doc_path = "./docs/" + file
        loader = Docx2txtLoader(doc_path)
        documents.extend(loader.load())
    elif file.endswith('.txt'):
        text_path = "./docs/" + file
        loader = TextLoader(text_path)
        documents.extend(loader.load())

document_splitter = CharacterTextSplitter(separator='\n', chunk_size=500, chunk_overlap=100)

document_chunks = document_splitter.split_documents(documents)

embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

vector_db = Chroma.from_documents(document_chunks, embedding=embeddings, persist_directory='./data')
vector_db.persist()

'''notebook_login()'''
auth_token = "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"

tokenizer = AutoTokenizer.from_pretrained("NousResearch/Llama-2-7b-chat-hf",
                                          use_auth_token=auth_token,)

model = AutoModelForCausalLM.from_pretrained("NousResearch/Llama-2-7b-chat-hf",
                                             device_map='auto',
                                             torch_dtype=torch.float16,
                                             use_auth_token=auth_token,
                                             #load_in_8bit=True,
                                             load_in_4bit=True
                                             )

pipe = pipeline("text-generation",
                model=model,
                tokenizer=tokenizer,
                torch_dtype=torch.bfloat16,
                device_map='auto',
                max_new_tokens=512,
                min_new_tokens=-1,
                top_k=30
                )
