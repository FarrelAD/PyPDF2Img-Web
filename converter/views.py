from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse, Http404
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
import os
import zipfile
import tempfile
import shutil
from .pdf_converter import convert_pdf_to_images

def home(request):
    """Display the main upload page."""
    return render(request, 'converter/home.html')

def convert_pdf(request):
    """Handle PDF upload and conversion."""
    if request.method == 'POST':
        try:
            # Get uploaded file
            pdf_file = request.FILES.get('pdf_file')
            if not pdf_file:
                return JsonResponse({'error': 'No PDF file uploaded'}, status=400)
            
            # Get conversion parameters
            dpi = int(request.POST.get('dpi', 300))
            image_format = request.POST.get('format', 'png')
            
            # Validate file type
            if not pdf_file.name.lower().endswith('.pdf'):
                return JsonResponse({'error': 'Please upload a PDF file'}, status=400)
            
            # Create temporary directory for processing
            with tempfile.TemporaryDirectory() as temp_dir:
                # Save uploaded PDF temporarily
                pdf_path = os.path.join(temp_dir, pdf_file.name)
                with open(pdf_path, 'wb') as f:
                    for chunk in pdf_file.chunks():
                        f.write(chunk)
                
                # Convert PDF to images
                output_folder = os.path.join(temp_dir, 'output')
                convert_pdf_to_images(pdf_path, output_folder, dpi, image_format)
                
                # Create zip file with all images
                zip_filename = f"{os.path.splitext(pdf_file.name)[0]}_images.zip"
                zip_path = os.path.join(temp_dir, zip_filename)
                
                with zipfile.ZipFile(zip_path, 'w') as zipf:
                    for root, dirs, files in os.walk(output_folder):
                        for file in files:
                            file_path = os.path.join(root, file)
                            arcname = os.path.relpath(file_path, output_folder)
                            zipf.write(file_path, arcname)
                
                # Save zip file to media directory
                media_folder = os.path.join(settings.MEDIA_ROOT, 'converted')
                os.makedirs(media_folder, exist_ok=True)
                
                final_zip_path = os.path.join(media_folder, zip_filename)
                shutil.copy2(zip_path, final_zip_path)
                
                # Count number of images created
                image_count = len([f for f in os.listdir(output_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff'))])
                
                return JsonResponse({
                    'success': True,
                    'message': f'Successfully converted {image_count} pages to {image_format.upper()} images',
                    'download_url': f'/download/{zip_filename}/',
                    'image_count': image_count
                })
                
        except Exception as e:
            return JsonResponse({'error': f'Conversion failed: {str(e)}'}, status=500)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def download_images(request, folder_name):
    """Download the converted images as a zip file."""
    try:
        zip_path = os.path.join(settings.MEDIA_ROOT, 'converted', folder_name)
        
        if not os.path.exists(zip_path):
            raise Http404("File not found")
        
        with open(zip_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/zip')
            response['Content-Disposition'] = f'attachment; filename="{folder_name}"'
            return response
            
    except Exception as e:
        raise Http404("File not found")
