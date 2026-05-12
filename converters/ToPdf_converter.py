 

from PIL import Image
from core.base_converter import BaseConverter

class ToPdfConverter(BaseConverter):
    """
    Concrete Strategy for PDF conversion.
    Refactored to handle color mode compatibility, a key requirement for PDFs.
    """

    def convert(self, input_path: str, output_path: str):
        
        with Image.open(input_path) as img:
            # PDFs do not support transparency (RGBA) or palette (P) modes well.
            # We must convert to RGB to ensure a successful save.
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            elif img.mode != "RGB":
                img = img.convert("RGB")
            
            # Save as PDF - Logic extracted and decoupled from the old folder structure.
            img.save(output_path, "PDF")
            print(f"Successfully created PDF: {output_path}")