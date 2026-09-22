const fileInput = document.getElementById('fileInput');
const dropZone = document.getElementById('dropZone');
const uploadBtn = document.getElementById('uploadBtn');
const statusMessage = document.getElementById('statusMessage');

let selectedFile = null;

// عند اختيار ملف
fileInput.addEventListener('change', (e) => {
    if (e.target.files.length > 0) {
        selectedFile = e.target.files[0];
        dropZone.innerHTML = `<p>تم اختيار: <strong style="color:#2c3e50;">${selectedFile.name}</strong></p>`;
    }
});

// عند الضغط على زر الرفع
uploadBtn.addEventListener('click', async () => {
    if (!selectedFile) {
        alert("الرجاء اختيار ملف أولاً");
        return;
    }

    statusMessage.style.color = "#3498db";
    statusMessage.textContent = "جاري رفع الملف... الرجاء الانتظار";

    const formData = new FormData();
    formData.append('file', selectedFile);

    try {
        const response = await fetch('http://127.0.0.1:5000/upload', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();
        
        if (response.ok) {
            statusMessage.style.color = "#27ae60";
            statusMessage.textContent = "تم رفع الملف بنجاح! جاري تحويلك...";
            
            // نحفظ المسار عشان نستخدمه في صفحة الملخص
            localStorage.setItem('uploadedFilePath', data.file_path);
            
            // ننتقل لصفحة الملخص بعد ثانية ونص
            setTimeout(() => {
                window.location.href = 'summary.html';
            }, 1500);
        } else {
            throw new Error(data.error || 'حدث خطأ أثناء الرفع');
        }
    } catch (error) {
        statusMessage.style.color = "#e74c3c";
        statusMessage.textContent = error.message;
    }
});
