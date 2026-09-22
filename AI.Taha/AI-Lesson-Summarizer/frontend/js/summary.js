const loadingDiv = document.getElementById('loading');
const summaryContent = document.getElementById('summaryContent');
const actionsDiv = document.getElementById('actions');

// الحصول على مسار الملف من الـ localStorage (اللي حفظناه في صفحة الرفع)
const filePath = localStorage.getItem('uploadedFilePath');

async function getSummary() {
    if (!filePath) {
        loadingDiv.textContent = "لم يتم العثور على ملف للتلخيص! الرجاء العودة ورفع ملف أولاً.";
        loadingDiv.style.color = "#e74c3c";
        return;
    }

    try {
        const response = await fetch('http://127.0.0.1:5000/summarize', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ file_path: filePath })
        });

        const data = await response.json();

        if (response.ok) {
            loadingDiv.style.display = 'none';
            summaryContent.style.display = 'block';
            actionsDiv.style.display = 'flex';
            
            // عرض الملخص
            summaryContent.textContent = data.summary;
        } else {
            throw new Error(data.error || 'حدث خطأ أثناء التلخيص');
        }
    } catch (error) {
        loadingDiv.textContent = `خطأ: ${error.message}`;
        loadingDiv.style.color = "#e74c3c";
    }
}

// تشغيل الدالة عند تحميل الصفحة
document.addEventListener('DOMContentLoaded', getSummary);
