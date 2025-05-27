# 🐾 BienestarIA – Asistente Legal Inteligente con LangChain y OpenAI

Este proyecto es un asistente legal basado en inteligencia artificial que responde preguntas directamente desde un texto legal en PDF.  
Construido con **LangChain 0.3**, **OpenAI GPT-3.5** y **FAISS**, incluye además una interfaz web visual hecha con Flask y HTML.

---

## 🚀 ¿Qué hace esta aplicación?

- 📄 Carga un archivo PDF legal (por defecto: `Bienestar Animal.pdf`)
- 🔍 Divide el texto automáticamente en fragmentos inteligentes ("chunks")
- 🧠 Convierte esos fragmentos en vectores semánticos con `OpenAIEmbeddings`
- 🤖 Usa GPT-3.5 para responder a preguntas usando solo el contenido del documento
- 💬 Permite interactuar desde la terminal **o desde una interfaz web tipo ChatGPT**
- 🔒 No tiene memoria: responde solo a lo que preguntas en ese momento

---

## 🔁 ¿Se puede adaptar para otros textos legales?

¡Sí, muy fácilmente! Este asistente está diseñado para ser reutilizable.

### ✅ ¿Cómo lo modifico?

1. Sustituye el archivo PDF:
Bienestar Animal.pdf → Contrato Laboral.pdf

2. Cambia una línea en `bienestar.py`:
```python
loader = PyPDFLoader("Contrato Laboral.pdf")
Al ejecutar el programa, se generará automáticamente un nuevo vectorstore con el nuevo contenido (contrato_index/ si lo renombras).

🌐 Interfaz Web incluida
Este proyecto incluye una interfaz HTML accesible desde el navegador.
Con solo ejecutar app.py, puedes usar el asistente legal desde una ventana tipo chat sin escribir código:

✅ Entrada de texto con botón

✅ Resultado mostrado en pantalla

❌ No guarda historial ni estados anteriores (sin memoria)

🧪 Cómo ejecutarlo
Clona el repositorio


Activa un entorno virtual y ejecuta:
pip install -r requirements.txt


Crea un archivo .env con tu clave de OpenAI:
OPENAI_API_KEY=tu_clave_aqui


Lanza la interfaz:
python app.py
Abre el navegador en:
http://localhost:5000


🧩 Tecnologías usadas
LangChain 0.3 – Motor de flujo de IA

OpenAI – Modelo de lenguaje

FAISS – Vectorstore local para búsqueda semántica

Flask – Servidor web

HTML – Interfaz simple y accesible

PyPDFLoader – Lector de PDF


📂 Estructura del proyecto

BienestarIA/
├── bienestar.py           # Código base con lógica de IA
├── app.py                 # Servidor Flask con interfaz web
├── Bienestar Animal.pdf   # PDF legal cargado
├── bienestar_index/       # Vectores generados (se crea solo)
├── templates/
│   └── index.html         # Interfaz del chat
├── .env                   # Clave privada (no subir)
├── requirements.txt       # Dependencias
├── .gitignore             # Archivos ignorados por Git
└── README.md              # Este archivo