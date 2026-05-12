# converters/ToImageFromPdf_converter.py
from core.base_converter import BaseConverter
from pdf2image import convert_from_path
import os

class ToImageFromPdfConverter(BaseConverter):
    """
    Strategy to convert the first page of a PDF into an Image.
    """
    def convert(self, input_path: str, output_path: str):
        try:
            # Convert only the first page for simplicity
            images = convert_from_path(input_path, first_page=1, last_page=1)
            if images:
                # Save the first page as the target format
                images[0].save(output_path)
        except Exception as e:
            raise Exception(f"PDF to Image conversion failed: {str(e)}")