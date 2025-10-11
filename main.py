#!/usr/bin/env python3

from pdf2image import convert_from_path
import os
import argparse

def pdf_to_images(
    pdf_path: str,
    output_folder: str | None = None,
    dpi: int = 300,
    image_format: str = "png"
) -> None:
    """
    Convert all pages in a PDF to separate images.

    Args:
        pdf_path (str): Path to the input PDF file.
        output_folder (str | None): Directory to save images.
                                   If None, a folder named `output` will be created next to the PDF.
        dpi (int): Resolution for output images.
        image_format (str): Image format (png, jpeg, etc.)
    """
    # Determine base directory of the input file
    pdf_dir = os.path.dirname(os.path.abspath(pdf_path))

    # Default output directory -> same location as PDF
    if output_folder is None:
        output_folder = os.path.join(pdf_dir, "output")

    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)

    print(f"Converting '{pdf_path}' into images...")
    print(f"Output folder: {output_folder}")

    # Convert PDF pages to images
    pages = convert_from_path(pdf_path, dpi=dpi)

    for i, page in enumerate(pages, start=1):
        image_path = os.path.join(output_folder, f"page_{i}.{image_format}")
        page.save(image_path, image_format.upper())
        print(f"Saved: {image_path}")

    print("Conversion complete!")

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert PDF pages into images."
    )

    parser.add_argument(
        "pdf_path",
        type=str,
        help="Path to the input PDF file."
    )

    parser.add_argument(
        "-o", "--output",
        type=str,
        default=None,
        help="Output folder to save images (default: create 'output' next to the PDF file)"
    )

    parser.add_argument(
        "--dpi",
        type=int,
        default=300,
        help="Resolution for output images (default: 300)"
    )

    parser.add_argument(
        "--format",
        type=str,
        default="png",
        choices=["png", "jpeg", "jpg", "tiff"],
        help="Image format for output (default: png)"
    )

    args = parser.parse_args()

    pdf_to_images(
        pdf_path=args.pdf_path,
        output_folder=args.output,
        dpi=args.dpi,
        image_format=args.format
    )

if __name__ == "__main__":
    main()
