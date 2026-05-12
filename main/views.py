from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from core.converter_factory import ConverterFactory
import os

def universal_converter(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        target_format = request.POST.get('target_format')

        # Normalize docx_to_pdf → target is 'pdf'
        if target_format == 'docx_to_pdf':
            target_format = 'pdf'

        source_format = uploaded_file.name.split('.')[-1].lower()

        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        input_path = fs.path(filename)

        output_filename = f"converted_{filename.split('.')[0]}.{target_format}"
        output_path = os.path.join(fs.location, output_filename)

        try:
            converter = ConverterFactory.get_converter(source_format, target_format)
            converter.convert(input_path, output_path)
            return render(request, 'success.html', {'download_url': fs.url(output_filename)})

        except Exception as e:
            return render(request, 'error.html', {'message': str(e)})

    initial_target = request.GET.get('target', 'pdf')
    return render(request, 'convert.html', {'initial_target': initial_target})

def home_view(request):
    return render(request, 'home.html')