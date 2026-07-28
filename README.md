
# Pegasus IA Assistant

## Descripción

Pegasus IA Assistant es un agente inteligente desarrollado con Python, LangChain, Gemini y Streamlit.

Permite consultar documentación interna de la empresa ficticia Santos Pegasus Soluciones mediante preguntas en lenguaje natural.

El sistema utiliza documentos PDF como fuente de conocimiento para generar respuestas contextualizadas.

---

## Arquitectura

PDFs
↓
PyPDFLoader
↓
Chunking
↓
Embeddings Gemini
↓
FAISS
↓
Retriever
↓
Gemini
↓
Streamlit

---

## Tecnologías Utilizadas

- Python
- Streamlit
- LangChain
- Google Gemini
- FAISS
- PyPDF
- dotenv

---

## Estructura del Proyecto

```text
PegasusIAAssistant
│
├── app.py
├── rag.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── data
    └── onboarding.pdf
```

## Instalación

Crear entorno virtual:

```bash
python -m venv venv
```

Activar entorno virtual:

```bash
venv\Scripts\activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Configurar variable de entorno:

```env
GOOGLE_API_KEY=TU_API_KEY
```

Ejecutar aplicación:

```bash
streamlit run app.py
```

<img width="1327" height="728" alt="image" src="https://github.com/user-attachments/assets/db286528-9306-4d9c-85cb-4a76832cff6b" />

## Ejemplos de preguntas

- ¿De qué trata el onboarding?
- ¿Qué actividades incluye el onboarding?
- ¿Cuál es el objetivo del plan 30/60/90?
- ¿Qué responsabilidades tiene un nuevo desarrollador?
<img width="1247" height="649" alt="image" src="https://github.com/user-attachments/assets/8184c096-7749-4e21-902e-52d1dfdcbd5b" />

## Ejemplo de respuesta

Pregunta:

¿Qué actividades incluye el onboarding?

Respuesta:

El onboarding es un proceso de integración diseñado para acelerar la adaptación de los nuevos colaboradores mediante capacitaciones, seguimiento y objetivos definidos para los primeros meses.
<img width="1259" height="672" alt="image" src="https://github.com/user-attachments/assets/bf3bd5e0-2056-4575-afa9-1dc707b7001c" />

## Autor

Alejandro Gonzalez
Challenge Alura Agente IA
Oracle Next Education
