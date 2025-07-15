import PyPDF2

class PDFExtractor:
    """
    A utility class for extracting text from PDF files.
    """

    @staticmethod
    def extract_text(file) -> str:
        """
        Extracts text from all pages of a PDF.

        Args:
            file: A file-like object containing the PDF.

        Returns:
            str: Extracted text from the PDF.
        """
        try:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""

            for page in pdf_reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

            return text.strip()

        except Exception as error:
            raise RuntimeError(f"Error extracting PDF text: {error}")
