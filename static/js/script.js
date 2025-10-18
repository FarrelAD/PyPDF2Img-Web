document.addEventListener('DOMContentLoaded', function() {
    const fileUploadArea = document.getElementById('fileUploadArea');
    const pdfFileInput = document.getElementById('pdfFile');
    const pdfForm = document.getElementById('pdfForm');
    const convertBtn = document.getElementById('convertBtn');
    const progressSection = document.getElementById('progressSection');
    const resultSection = document.getElementById('resultSection');
    const errorSection = document.getElementById('errorSection');
    const progressFill = document.getElementById('progressFill');
    const progressText = document.getElementById('progressText');
    const resultText = document.getElementById('resultText');
    const errorText = document.getElementById('errorText');
    const downloadLink = document.getElementById('downloadLink');

    // File upload area interactions
    fileUploadArea.addEventListener('click', () => pdfFileInput.click());
    
    fileUploadArea.addEventListener('dragover', (e) => {
        e.preventDefault();
        fileUploadArea.classList.add('dragover');
    });
    
    fileUploadArea.addEventListener('dragleave', () => {
        fileUploadArea.classList.remove('dragover');
    });
    
    fileUploadArea.addEventListener('drop', (e) => {
        e.preventDefault();
        fileUploadArea.classList.remove('dragover');
        
        const files = e.dataTransfer.files;
        if (files.length > 0) {
            pdfFileInput.files = files;
            updateFileInfo(files[0]);
        }
    });

    // File input change
    pdfFileInput.addEventListener('change', (e) => {
        if (e.target.files.length > 0) {
            updateFileInfo(e.target.files[0]);
        }
    });

    // Form submission
    pdfForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        if (!pdfFileInput.files.length) {
            showError('Please select a PDF file');
            return;
        }

        const formData = new FormData(pdfForm);
        
        // Show progress
        showProgress();
        hideResults();
        hideError();
        
        // Disable convert button
        convertBtn.disabled = true;
        convertBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Converting...';

        try {
            const response = await fetch('/convert/', {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                }
            });

            const data = await response.json();

            if (data.success) {
                showSuccess(data.message, data.download_url, data.image_count);
            } else {
                showError(data.error || 'Conversion failed');
            }
        } catch (error) {
            showError('Network error: ' + error.message);
        } finally {
            // Re-enable convert button
            convertBtn.disabled = false;
            convertBtn.innerHTML = '<i class="fas fa-magic"></i> Convert to Images';
            hideProgress();
        }
    });

    function updateFileInfo(file) {
        // Remove existing file info
        const existingInfo = fileUploadArea.querySelector('.file-info');
        if (existingInfo) {
            existingInfo.remove();
        }

        // Create file info display
        const fileInfo = document.createElement('div');
        fileInfo.className = 'file-info';
        fileInfo.innerHTML = `
            <h4><i class="fas fa-file-pdf"></i> ${file.name}</h4>
            <p>Size: ${formatFileSize(file.size)} | Type: ${file.type || 'PDF'}</p>
        `;
        
        fileUploadArea.appendChild(fileInfo);
    }

    function formatFileSize(bytes) {
        if (bytes === 0) return '0 Bytes';
        const k = 1024;
        const sizes = ['Bytes', 'KB', 'MB', 'GB'];
        const i = Math.floor(Math.log(bytes) / Math.log(k));
        return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
    }

    function showProgress() {
        progressSection.style.display = 'block';
        progressFill.style.width = '100%';
        progressText.textContent = 'Converting PDF to images...';
    }

    function hideProgress() {
        progressSection.style.display = 'none';
        progressFill.style.width = '0%';
    }

    function showSuccess(message, downloadUrl, imageCount) {
        resultText.textContent = message;
        downloadLink.href = downloadUrl;
        downloadLink.download = downloadUrl.split('/').pop();
        resultSection.style.display = 'block';
        hideError();
    }

    function showError(message) {
        errorText.textContent = message;
        errorSection.style.display = 'block';
        hideResults();
    }

    function hideResults() {
        resultSection.style.display = 'none';
    }

    function hideError() {
        errorSection.style.display = 'none';
    }

    // Reset form when new file is selected
    pdfFileInput.addEventListener('change', () => {
        hideResults();
        hideError();
    });
});
