import streamlit as st
import pandas as pd
import PyPDF2
import openai

# Accedemos a la clave de API de OpenAI a través de una variable de entorno
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Función para extraer texto de un PDF
def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfFileReader(file)
    text = ""
    for page in range(pdf_reader.numPages):
        page_obj = pdf_reader.getPage(page)
        text += page_obj.extractText()
    return text

# Función para generar una síntesis utilizando GPT-3
def generate_synthesis(text):
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"Generate a synthesis of the following text: {text}",
        temperature=0.7,
        max_tokens=1024,
        n=1,
        stop=None,
        )
    return response.choices[0].text

# Título de la aplicación
st.title("Síntesis de documentos PDF con GPT-3")

# Instrucciones para subir un archivo PDF
st.write("Para comenzar, sube un archivo PDF que quieras sintetizar:")

# Seleccionar archivo PDF
file = st.file_uploader("Sube tu archivo PDF", type=["pdf"])

# Si se subió un archivo PDF
if file is not None:
    # Extraer texto del PDF
    text = extract_text_from_pdf(file)

    # Mostrar el texto del PDF en la aplicación
    st.write("Este es el texto que se extrajo del PDF:")
    st.write(text)

    # Generar una síntesis del texto utilizando GPT-3
    st.write("Generando una síntesis utilizando GPT-3...")
    synthesis = generate_synthesis(text)

    # Mostrar la síntesis en la aplicación
    st.write("Esta es la síntesis generada por GPT-3:")
    st.write(synthesis)
