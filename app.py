import streamlit as st

from rag import retriever
from rag import llm

st.title("🤖 Pegasus IA Assistant")

pregunta = st.text_input(
    "Pregunta sobre la empresa"
)

if st.button("Preguntar"):

    documentos = retriever.invoke(
    pregunta
    )

    contexto = "\n".join(
        [doc.page_content for doc in documentos]
    )

    prompt = f"""
    Responde únicamente usando la información proporcionada.

    Contexto:
    {contexto}

    Pregunta:
    {pregunta}
    """

    respuesta = llm.invoke(prompt)

    texto = respuesta.content[0]["text"]

    st.markdown(texto)
