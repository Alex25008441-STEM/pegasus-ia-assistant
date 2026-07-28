# pegasus-ia-assistant

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

## Ejemplos de preguntas

- ¿De qué trata el onboarding?
- ¿Qué actividades incluye el onboarding?
- ¿Cuál es el objetivo del plan 30/60/90?
- ¿Qué responsabilidades tiene un nuevo desarrollador?

## Ejemplo de respuesta

Pregunta:

¿Qué actividades incluye el onboarding?

Respuesta:

El onboarding es un proceso de integración diseñado para acelerar la adaptación de los nuevos colaboradores mediante capacitaciones, seguimiento y objetivos definidos para los primeros meses.

## Autor

Alejandro González
Challenge Alura Agente IA
Oracle Next Education
