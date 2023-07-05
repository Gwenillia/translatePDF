# translatePDF
Welcome to translatePDF, a project that allows you to translate your PDF files into French.

## Installation
1. First, you'll need to install the required packages. You can find the list of imports in the `translate-pdf.py` file. Here is a quick list of some of the major packages you'll need:

- pypdf
- pdfplumber
- EasyGoogleTranslate (or a similar translation API)

2. Next, place all the PDF files you wish to translate into the PDF folder.

## Usage
1. From the root of the project, run the `unprotect.fish` script. This script will decrypt any encrypted PDF files in the PDF folder and move them into their own directories.

`./unprotect.fish`

2. Now, you're ready to translate the PDFs. Run the `translate-pdf.py` script to begin the translation process.

`python3 translate-pdf.py`

Each page of each PDF file will be translated into French and output as a separate .txt file in the same directory as the original PDF.

## Future Updates
In the future, I plan to update the project with a cleaner, more user-friendly command-line interface. I believe this will enhance user experience and efficiency. So, stay tuned for those updates! I also plan to include ocrmypdf to solve some potential problems :)

