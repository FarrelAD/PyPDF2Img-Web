# PDF to Image Converter - Web Interface

A modern web application that converts PDF files into high-quality images with a beautiful, responsive interface.

## Features

- 🎨 **Modern Web Interface** - Clean, responsive design with drag-and-drop file upload
- 📄 **PDF to Image Conversion** - Convert PDF pages to PNG, JPEG, or TIFF images
- ⚙️ **Customizable Settings** - Choose DPI resolution (150, 300, 600) and image format
- 📦 **Batch Download** - Download all converted images as a single ZIP file
- 🚀 **Fast Processing** - Optimized conversion with progress indicators
- 📱 **Mobile Friendly** - Responsive design that works on all devices

## Requirements

- Python 3.12+
- Django 4.2+
- pdf2image library
- poppler-utils (for PDF processing)

## Installation

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

Or using uv:
```bash
uv sync
```

### 2. Install Poppler (Required for PDF processing)

#### Windows:
- Download poppler binaries from [poppler-windows](https://github.com/oschwartz10612/poppler-windows/releases)
- Extract and add the `bin` folder to your system PATH

#### macOS:
```bash
brew install poppler
```

#### Linux:
```bash
sudo apt-get install poppler-utils
```

### 3. Set Up Django

```bash
# Run migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser
```

## Usage

### Start the Development Server

```bash
python manage.py runserver
```

Open your browser and go to `http://127.0.0.1:8000`

### Using the Web Interface

1. **Upload PDF**: Drag and drop your PDF file or click to browse
2. **Configure Settings**: 
   - Choose DPI resolution (150 for fast, 300 for quality, 600 for ultra-high)
   - Select image format (PNG, JPEG, or TIFF)
3. **Convert**: Click "Convert to Images" button
4. **Download**: Download the ZIP file containing all converted images

### Command Line Usage (Original)

You can still use the original command-line interface:

```bash
python main.py "path/to/your/file.pdf" --dpi 300 --format png --output "output_folder"
```

## Project Structure

```
PyPDF2Img/
├── main.py                 # Original command-line script
├── manage.py              # Django management script
├── pdf2img_web/           # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── converter/             # Main Django app
│   ├── views.py           # Web interface logic
│   ├── pdf_converter.py   # PDF conversion functions
│   └── urls.py
├── templates/             # HTML templates
│   └── converter/
│       └── home.html
├── static/                # Static files
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
├── media/                 # Uploaded files and converted images
└── requirements.txt       # Python dependencies
```

## API Endpoints

- `GET /` - Main upload interface
- `POST /convert/` - Convert PDF to images
- `GET /download/<filename>/` - Download converted images as ZIP

## Configuration

### File Upload Limits
Default maximum file size is 50MB. You can modify this in `pdf2img_web/settings.py`:

```python
FILE_UPLOAD_MAX_MEMORY_SIZE = 50 * 1024 * 1024  # 50MB
```

### Supported Formats
- **Input**: PDF files
- **Output**: PNG, JPEG, TIFF images

## Troubleshooting

### Common Issues

1. **"poppler not found" error**:
   - Make sure poppler-utils is installed and in your PATH
   - On Windows, ensure the poppler bin folder is added to system PATH

2. **File upload errors**:
   - Check file size limits in settings.py
   - Ensure the file is a valid PDF

3. **Conversion fails**:
   - Verify the PDF file is not corrupted
   - Check that poppler is properly installed

## Development

### Running Tests
```bash
python manage.py test
```

### Creating Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

## License

This project is open source and available under the MIT License.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Support

If you encounter any issues or have questions, please open an issue on GitHub.
