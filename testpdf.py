import os
import PyPDF2
from PyPDF2.errors import PdfReadError

filepath = 'C:/Niharika/PDF_downloader_automatic/Pdfs_20250523/104_ANNUALREPORT16_17.pdf'

try:
    with open(filepath, "rb") as f:
        pdf = PyPDF2.PdfReader(f)

        # Check for empty PDF (no pages)
        if len(pdf.pages) == 0:
            os.remove(filepath)

except PdfReadError:
    os.remove(filepath)
