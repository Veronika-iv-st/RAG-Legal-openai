from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
import os

# Cargar clave API
load_dotenv()
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# Cargar y dividir el PDF
loader = PyPDFLoader("Bienestar Animal.pdf")
pages = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
docs = splitter.split_documents(pages)

# Crear embeddings y vectorstore
embedding = OpenAIEmbeddings()
if os.path.exists("bienestar_index"):
    vectorstore = FAISS.load_local("bienestar_index", embedding, allow_dangerous_deserialization=True)
else:
    vectorstore = FAISS.from_documents(docs, embedding)
    vectorstore.save_local("bienestar_index")

retriever = vectorstore.as_retriever()

# Definir el prompt (¡usa 'context' porque lo usaremos en el input!)
prompt_template = PromptTemplate(
    template="""
Usa unicamente la informacion del texto proporcionado para responder a las preguntas del usuario citando el texto exacto.
Si no encuentras la informacion exacta di solo "no tengo informacion especifica para esta pregunta"
No puedes inventar informacion adicional, solo proporcionar la informacion util para cada consulta extrayendo el texto.

contexto: {context}

Pregunta: {question}
""",
    input_variables=["context", "question"]
)

# Crear el chain actualizado (forma recomendada por LangChain 0.3+)
qa_chain = create_stuff_documents_chain(llm=llm, prompt=prompt_template)

# Ejecución
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
import os

# Cargar clave API
load_dotenv()
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# Cargar y dividir el PDF
loader = PyPDFLoader("Bienestar Animal.pdf")
pages = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
docs = splitter.split_documents(pages)

# Crear embeddings y vectorstore
embedding = OpenAIEmbeddings()
if os.path.exists("bienestar_index"):
    vectorstore = FAISS.load_local("bienestar_index", embedding, allow_dangerous_deserialization=True)
else:
    vectorstore = FAISS.from_documents(docs, embedding)
    vectorstore.save_local("bienestar_index")

retriever = vectorstore.as_retriever()

# Definir el prompt (¡usa 'context' porque lo usaremos en el input!)
prompt_template = PromptTemplate(
    template="""
Usa unicamente la informacion del texto proporcionado para responder a las preguntas del usuario citando el texto exacto.
No puedes inventar informacion adicional, solo proporcionar la informacion util para cada consulta extrayendo el texto.
Proporciona tambien el parrafo que proporciona esta informacion.

contexto: {context}

Pregunta: {question}
""",
    input_variables=["context", "question"]
)

# Crear el chain actualizado (forma recomendada por LangChain 0.3+)
qa_chain = create_stuff_documents_chain(llm=llm, prompt=prompt_template)

# Ejecución
def responder_pregunta(question: str) -> str:
    relevant_docs = retriever.get_relevant_documents(question)
    return qa_chain.invoke({"context": relevant_docs, "question": question})

# Solo se ejecuta si corres este archivo directamente
if __name__ == "__main__":
    while True:
        question = input("¿Qué necesitas saber sobre el bienestar animal? ")
        if question.lower() == "exit":
            break
        result = responder_pregunta(question)
        print("\n📘 Información Legal:\n")
        print(result)