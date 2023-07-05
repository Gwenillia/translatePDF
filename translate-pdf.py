import os
from pypdf import PdfReader
import pdfplumber
from easygoogletranslate import EasyGoogleTranslate
import textwrap

# Directory containing the PDF files
pdf_directory = './PDF'

# Get a list of PDF files in the directory
pdf_files = [file for file in os.listdir(pdf_directory) if file.endswith('.pdf')]

# translator = Translator(to_lang='fr')
translator = EasyGoogleTranslate(
    source_language='en',
    target_language='fr'
)

# Iterate over each PDF file
for pdf_file in pdf_files:
    # Create a folder with the name of the PDF file
    folder_name = os.path.splitext(pdf_file)[0]
    folder_path = os.path.join(pdf_directory, folder_name)
    os.makedirs(folder_path, exist_ok=True)

    # Move the PDF file into the folder
    source_path = os.path.join(pdf_directory, pdf_file)
    destination_path = os.path.join(folder_path, pdf_file)
    os.rename(source_path, destination_path)

    # Open the PDF file
    with open(destination_path, 'rb') as f:
        pdf = PdfReader(f)
        num_pages = len(pdf.pages)

    # Iterate over all pages
    for page_num in range(num_pages):
        page = pdf.pages[page_num]

        # Convert page to a file-like object and extract text
        with pdfplumber.open(destination_path) as pdf_file:
            pdf_page = pdf_file.pages[page_num]
            txt = pdf_page.extract_text()

        # Split the text into chunks
        chunks = textwrap.wrap(txt, width=4999, break_long_words=False)

        translated_text = ""
        for chunk in chunks:
            translated_chunk = translator.translate(chunk)
            translated_text += translated_chunk

        # Save the translated text to a new file
        output_filename = f'fr_page{page_num + 1}.txt'
        output_path = os.path.join(folder_path, output_filename)
        with open(output_path, 'w') as f2:
            f2.write(translated_text)

