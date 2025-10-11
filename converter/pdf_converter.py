"""
PDF to Image converter module for web interface.
"""
from pdf2image import convert_from_path
import os

def convert_pdf_to_images(pdf_path, output_folder, dpi=300, image_format="png"):
    """
    Convert all pages in a PDF to separate images.

    Args:
        pdf_path (str): Path to the input PDF file.
        output_folder (str): Directory to save images.
        dpi (int): Resolution for output images.
        image_format (str): Image format (png, jpeg, etc.)
    """
    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Convert PDF pages to images
    pages = convert_from_path(pdf_path, dpi=dpi)

    for i, page in enumerate(pages, start=1):
        image_path = os.path.join(output_folder, f"page_{i}.{image_format}")
        page.save(image_path, image_format.upper())

    return len(pages)
