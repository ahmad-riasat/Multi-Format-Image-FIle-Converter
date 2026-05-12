from converters.ToJpeg_converter import ToJpegConverter
from converters.ToPdf_converter import ToPdfConverter
from converters.ToPng_converter import ToPngConverter
from converters.ToPdfFromDocx_converter import ToPdfFromDocxConverter
from converters.ToImageFromPdf_converter import ToImageFromPdfConverter
# As you refactor more files, import them here

class ConverterFactory:
    """
    This Factory class eliminates hard-coding by dynamically 
    selecting the correct conversion strategy.
    """
    
    _registry = {
        # (Input Format, Target Format)
        ('jpg', 'pdf'): ToPdfConverter,
        ('jpeg', 'pdf'): ToPdfConverter,
        ('png', 'pdf'): ToPdfConverter,
        ('png', 'jpeg'): ToJpegConverter,
        ('jpeg', 'png'): ToPngConverter,
        ('docx', 'pdf'): ToPdfFromDocxConverter,
        ('pdf', 'jpeg'): ToImageFromPdfConverter,
        ('pdf', 'jpg'): ToImageFromPdfConverter,
        ('pdf', 'png'): ToImageFromPdfConverter,
    }

    @staticmethod
    def get_converter(source_format,target_format):
        """
        Returns an instance of the required converter.
        Applying the Open/Closed Principle: you can add new formats 
        to the registry without changing this method.
        """
        source=source_format.lower().replace('.', '')
        target= target_format.lower().replace('.', '')
        
        converter_class = ConverterFactory._registry.get((source,target))
        
        if not converter_class:
            raise ValueError(f"Format '{target_format}' is not supported yet.")
            
        return converter_class()
    
    #this will return the converter class, which convert the format