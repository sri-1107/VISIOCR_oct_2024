from django.shortcuts import render
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .ocr_service import perform_ocr


from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .ocr_service import perform_ocr

def home(request):
    return render(request, 'OCR_APP/home.html')

def upload_image(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        uploaded_file_url = fs.url(filename)

        extracted_text = perform_ocr(fs.path(filename))

        return render(request, 'OCR_APP/result.html', {
            'uploaded_file_url': uploaded_file_url,
            'extracted_text': extracted_text
        })
    return render(request, 'OCR_APP/upload.html')


