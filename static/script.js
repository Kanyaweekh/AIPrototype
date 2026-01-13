/* --- Floating Elements --- */
document.addEventListener("DOMContentLoaded", () => {
    const container = document.getElementById('floating-container');
    if (!container) return;
    const icons = ['🌸', '✨', '🎫', '☁️', '🎀'];
    for (let i = 0; i < 20; i++) {
        const el = document.createElement('div');
        el.classList.add('floater');
        el.innerText = icons[Math.floor(Math.random() * icons.length)];
        el.style.left = Math.random() * 100 + 'vw';
        el.style.fontSize = (Math.random() * 20 + 10) + 'px';
        el.style.animationDuration = (Math.random() * 10 + 8) + 's';
        el.style.animationDelay = Math.random() * 5 + 's';
        container.appendChild(el);
    }
});

/* --- Print Logic --- */
document.getElementById('prediction-form').addEventListener('submit', async function(e) {
    e.preventDefault();

    const receipt = document.getElementById('receipt-paper');
    const flowerImage = document.getElementById('flower-image');
    const resultName = document.getElementById('result-name');
    const printTime = document.getElementById('print-time');
    const statusMsg = document.getElementById('status-msg');
    const errorBox = document.getElementById('error-box');

    // 1. Reset
    receipt.classList.remove('printing');
    
    // โชว์ข้อความสถานะ
    statusMsg.style.display = 'block'; 
    statusMsg.innerText = "PROCESSING..."; // กำลังประมวลผล
    
    flowerImage.style.display = 'none';
    errorBox.style.display = 'none';
    flowerImage.removeAttribute('src');

    await new Promise(r => setTimeout(r, 500));

    const formData = new FormData(this);

    try {
        const response = await fetch('/api/predict', { method: 'POST', body: formData });
        const data = await response.json();

        if (data.error) {
            alert(data.error);
            statusMsg.innerText = "ERROR!";
        } else {
            resultName.innerText = data.class;
            
            const now = new Date();
            printTime.innerText = now.toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'});

            const newImageSrc = `/static/images/${data.image_file}?t=${Date.now()}`;

            flowerImage.onload = function() {
                this.style.display = 'block';
                errorBox.style.display = 'none';
            };
            flowerImage.onerror = function() {
                this.style.display = 'none';
                errorBox.style.display = 'block';
            };

            flowerImage.src = newImageSrc;
            
            // 2. เริ่มปริ้น -> สั่งซ่อนข้อความสถานะทันที
            statusMsg.style.display = 'none';
            receipt.classList.add('printing');
        }

    } catch (error) {
        console.error(error);
        statusMsg.innerText = "CONNECTION FAILED";
    }
});