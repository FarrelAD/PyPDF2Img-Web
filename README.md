# PyPDF2Img 📄🖼️

![GitHub release](https://img.shields.io/github/v/release/FarrelAD/PyPDF2Img)

A simple PDF-to-image converter. This program is actually a **wrapper around the [`pdf2image`](https://pypi.org/project/pdf2image/) library**, with added convenience like automatically converting **all pages** of a PDF without extra setup.  

PyPDF2Img is already packaged as standalone binaries for **Windows, macOS, and Linux**. You can download the releases from the GitHub repository here:  
[https://github.com/FarrelAD/PyPDF2Img/releases](https://github.com/FarrelAD/PyPDF2Img/releases)

---

# Manual Guide 🔎

### 1. See program help

Check all available options and usage:

```bash
pdf2img --help
```
This will show something like:
```bash
usage: pdf2img [-h] [-o OUTPUT] [--dpi DPI] [--format {png,jpeg,jpg,tiff}] pdf_path

Convert PDF pages into images

positional arguments:
  pdf_path              Path to the input PDF file.

optional arguments:
  -h, --help            show this help message and exit
  -o, --output          Output folder to save images (default: same folder as PDF / "output")
  --dpi                 Resolution for output images (default: 300)
  --format {png,jpeg,jpg,tiff}
                        Image format for output (default: png)
```

### 2. Convert a PDF with default options

This will create an `output` folder next to your PDF file and save all pages as PNG images:

```bash
pdf2img example.pdf
```
### 3. Convert a PDF to a custom folder

```bash
pdf2img example.pdf -o my_images
```

All images will be saved in the `my_images` folder.

### 4. Set a custom DPI (resolution)

```bash
pdf2img example.pdf --dpi 150
```

### 5. Change the output image format

```bash
pdf2img example.pdf --format jpeg
```

Supports: `png`, `jpeg`, `jpg`, `tiff`.

## NOTES 📝

- On Windows, the executable is `pdf2img.exe`. On macOS/Linux, it is `pdf2img`.
- Works with multi-page PDFs automatically — no need to loop manually.