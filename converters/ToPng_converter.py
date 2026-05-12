 

from PIL import Image
import os
from core.base_converter import BaseConverter # Import your new base class

class ToPngConverter(BaseConverter):
    
    
    def convert(self, input_path: str, output_path: str):
        """
        Implementation of the conversion logic.
        """
        # Open the original file (e.g., JPEG or BMP)
        with Image.open(input_path) as img:
            # PNG supports RGBA, so no strict need to convert to RGB 
            # unless specifically required by your project logic.
            img.save(output_path, 'PNG')
            print(f"File saved successfully at {output_path}")