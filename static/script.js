document.getElementById('prediction-form').addEventListener('submit', async function(e) {
    e.preventDefault();

    const placeholder = document.getElementById('placeholder-state');
    const resultState = document.getElementById('result-state');
    const spinner = document.getElementById('loading-spinner');
    const resultName = document.getElementById('result-name');
    const flowerImage = document.getElementById('flower-image');
    const errorMsg = document.getElementById('error-msg');

    // 1. เริ่มโหลด: ซ่อนทุกอย่าง แสดง Spinner
    placeholder.style.display = 'none';
    resultState.style.display = 'none';
    spinner.style.display = 'block';
    
    // Reset รูปภาพ
    flowerImage.style.display = 'block'; 
    errorMsg.style.display = 'none';

    const formData = new FormData(this);

    try {
        const response = await fetch('/api/predict', {
            method: 'POST',
            body: formData
        });
        const data = await response.json();

        // หน่วงเวลา 0.8 วิ ให้ดูเหมือนคิด
        setTimeout(() => {
            spinner.style.display = 'none';

            if (data.error) {
                alert("Error: " + data.error);
                placeholder.style.display = 'block'; // กลับไปหน้าเริ่ม
            } else {
                // 2. แสดงผล
                resultState.style.display = 'block';
                resultName.innerText = data.class;
                
                // ใส่ Timestamp ต่อท้ายเพื่อแก้ปัญหา Browser จำรูปเดิม (Cache)
                flowerImage.src = `/static/images/${data.image_file}?t=${new Date().getTime()}`;
            }
        }, 800);

    } catch (error) {
        console.error(error);
        spinner.style.display = 'none';
        placeholder.style.display = 'block';
        alert("เกิดข้อผิดพลาดในการเชื่อมต่อ");
    }
});