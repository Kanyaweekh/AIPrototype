// static/script.js

document.getElementById('prediction-form').addEventListener('submit', async function(e) {
    e.preventDefault(); // ป้องกันการรีโหลดหน้าเว็บ

    // อ้างอิง Element
    const loader = document.getElementById('loader');
    const resultText = document.getElementById('result-text');
    const formData = new FormData(this);

    // แสดง Loader และเคลียร์ผลเก่า
    loader.style.display = 'block';
    resultText.innerHTML = '';

    try {
        // ส่งข้อมูลไปยัง Python API
        const response = await fetch('/api/predict', {
            method: 'POST',
            body: formData
        });
        
        const data = await response.json();

        // หน่วงเวลาเล็กน้อยเพื่อให้เห็น Animation
        setTimeout(() => {
            loader.style.display = 'none';
            if (data.error) {
                resultText.innerHTML = `<span style="color:red">${data.error}</span>`;
            } else {
                resultText.innerHTML = `<div class="prediction-text">${data.class}</div>`;
            }
        }, 500);

    } catch (error) {
        console.error('Error:', error);
        loader.style.display = 'none';
        resultText.innerHTML = '<span style="color:red">An error occurred.</span>';
    }
});