# Managing Conda Environment
---

## 1. Installing Conda
เลือกติดตั้งได้ตามความเหมาะสมของงาน Conda สามารถติดตั้งได้จาก 2 แหล่งหลัก

### Miniconda  
ขนาดเล็ก เหมาะสำหรับใช้งานบน Server  
🔗 **Link** https://docs.conda.io/en/latest/miniconda.html

### Anaconda  
มาพร้อมเครื่องมือครบถ้วนและ GUI  
🔗 **Link** https://www.anaconda.com/products/distribution
* คำสั่งตรวจสอบการติดตั้ง
```bash
conda --version
```
## 2. การจัดการ Environment
เมื่อเปิด Terminal ใหม่ ระบบจะเริ่มต้นที่ (base) เสมอ
* สร้าง Environment ใหม่
```bash
conda create --name <ชื่อenv> python=<เวอร์ชัน>
```
* เข้าใช้งาน (Activate)
```bash
conda activate <ชื่อenv>
```
* ออกจาก Environment
```bash
conda deactivate
```
* ลบ Environment
```bash
conda remove --name <ชื่อenv> --all
```
* ดูรายการ Environment ทั้งหมด
```bash
conda env list
```
## 3. การจัดการ Package
> ⚠️ สำคัญมาก: ต้อง Activate เข้า Environment ก่อนติดตั้งทุกครั้ง หากลืมลง Package แล้วไป Import จะทำให้เกิด Error
* ติดตั้ง Package
```bash
conda install <ชื่อแพ็กเกจ>
```
* ดูรายการที่ลงไว้
```bash
conda list
```
## 4. GitHub Command Line
⚙️การตั้งค่าเริ่มต้น 
> ดำเนินการเพียงครั้งเดียวในการใช้งานครั้งแรก
```bash
git config --global user.name "ชื่อผู้ใช้"
git config --global user.email "อีเมล"
```
Clone Repository
```bash
git clone <repository_url>
```

---

Save Code to GitHub

ขั้นตอนเมื่อมีการแก้ไขไฟล์

* 1. ดึงเวอร์ชันล่าสุด
```bash
git pull
```

* 2. เพิ่มไฟล์เที่ต้องการจะอัพขึ้น GitHub
```bash
git add <ชื่อไฟล์>
```

* 3. Commit การเปลี่ยนแปลง
```bash
git commit -m "คำอธิบายตามที่เราต้องการ"
```

* 4. อัพโหลดขึ้น GitHub
```bash
git push
```
!! ลำดับการส่งงานขึ้น GitHub !!

  **✨ จำสั้น ๆ : add → commit → push**

🔍 เช็คสถานะไฟล์ (git status)
- สีแดง: ไฟล์ใหม่ที่ Git ยังไม่เคยมี
- สีเขียว: ไฟล์ที่ Add แล้ว เตรียมพร้อมส่ง
- ไม่ขึ้นอะไร: ทุกอย่างเรียบร้อยดี
## 5. GitHub Token
สร้าง Token ได้ที่

`Profile Github Setting➔ Settings ➔ Developer Settings ➔ Personal access tokens ➔ Generate new token `
> **คำเตือน: Token จะแสดงเพียงครั้งเดียวกรุณาเซฟเก็บไว้ให้ดี ถ้าลืมต้องสร้างใหม่**

