 



from PIL import Image, ExifTags
from core.base_converter import BaseConverter
import os

class ToJpegConverter(BaseConverter):
    

    def _fix_orientation(self, img):
        """Internal helper to handle EXIF orientation logic (Refactored)"""
        try:
            exif = dict(img._getexif().items()) # get exip data (orientatin detail to properly rotate image )
            for orientation_key, val in ExifTags.TAGS.items():
                if val == 'Orientation' and orientation_key in exif:
                    if exif[orientation_key] == 3: return img.rotate(180, expand=True)
                    if exif[orientation_key] == 6: return img.rotate(270, expand=True)
                    if exif[orientation_key] == 8: return img.rotate(90, expand=True)
        except Exception:
            pass # Orientation data missing
        return img

    def convert(self, input_path: str, output_path: str):

        with Image.open(input_path) as img:
            img = self._fix_orientation(img)
            
            # JPEG requires RGB mode; handle transparency (RGBA)
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            
            # Save using the parameters provided by the Factory, not hard-coded paths
            img.save(output_path, 'JPEG', quality=100)