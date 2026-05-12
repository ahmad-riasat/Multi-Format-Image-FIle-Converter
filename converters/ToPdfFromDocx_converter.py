# converters/ToPdfFromDocx_converter.py
from core.base_converter import BaseConverter
import aspose.words as aw

class ToPdfFromDocxConverter(BaseConverter):
    """
    Concrete Strategy to convert Word Documents (.docx) to PDF.
    """
    def convert(self, input_path: str, output_path: str):
        try:
            # Load the Word document
            doc = aw.Document(input_path)
            # Save as PDF
            doc.save(output_path)
        except Exception as e:
            raise Exception(f"Word to PDF conversion failed: {str(e)}")