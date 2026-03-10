# Install Miniconda (Linux) 

อธิบายขั้นตอนการติดตั้ง **Miniconda บนระบบ Linux** ซึ่งใช้สำหรับจัดการ Python environment และ package สำหรับงานพัฒนาและรัน Server

🔗 **Link** [Miniconda Official Documentation](https://www.anaconda.com/docs/getting-started/miniconda/install#linux-2)

---

## 📥 1. การติดตั้งและตั้งค่า Miniconda

### 1.1 Download & Install Miniconda
ให้รันคำสั่งต่อไปนี้ **ทีละบรรทัด** เพื่อดาวน์โหลดและติดตั้ง Miniconda (สำหรับ Linux – x86_64)

```bash
mkdir -p ~/miniconda3
wget [https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh](https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh) -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh
```
### 1.2 Activate Miniconda
หลังจากติดตั้งเสร็จแล้ว ให้ปิดแล้วเปิด Terminal ใหม่ หรือใช้คำสั่งด้านล่างเพื่อ refresh environment
```bash
source ~/miniconda3/bin/activate
```
### 1.3 Initialize Conda
ตั้งค่า conda ให้สามารถใช้งานได้กับทุก shell
```bash
conda init --all
```
  📌 ข้อสังเกต: หากการตั้งค่าทุกอย่างสมบูรณ์แบบ คุณจะพบคำนำหน้าว่า (base) ปรากฏขึ้นในบรรทัดคำสั่งเสมอ ซึ่งเป็นการยืนยันว่าระบบพร้อมใช้งาน
## 🧑‍💻 2. Python Command Line (VS Code Integration)
Python environment นี้ใช้สำหรับเขียนและรันโปรแกรมบน Server
* เปิด VS Code ผ่าน Command Line
```bash
code
```
* เปิดหรือสร้างไฟล์ใน VS Code
```bash
code <file_name>
```
## 🖥️ 3. การใช้งาน Screen Session
`screen` ใช้สำหรับรันโปรแกรมบน Server แบบต่อเนื่อง
### 3.1 การจัดการ Screen เบื้องต้น
* สร้าง Screen ใหม่
```bash
screen -S <screen_name>
```
* กลับเข้า Screen ที่มีอยู่
```bash
screen -R
```
### 3.2 คำสั่งลัดควบคุม Screen (Shortcuts)
* `Ctrl + A + D` → ออกจาก session ปัจจุบัน โดยระบบจะยังคงประมวลผลอยู่เบื้องหลัง
* `Ctrl + A + K + Y` → ออกจากและลบ session
* `Ctrl + A + [` → Freeze หน้าจอ (สามารถเลื่อนดูได้)
* `q + Enter` → การออกจากสถานะระงับหน้าจอชั่วคราว
* `Ctrl + C` → การยุติโปรแกรมที่กำลังประมวลผลอยู่ในปัจจุบัน
### 3.3 การลบ Screen ที่ชื่อซ้ำ
หากมี Screen ชื่อซ้ำกัน ให้ทำตามขั้นตอนดังนี้
  ตรวจสอบ Screen ที่มีอยู่ทั้งหมด: สามารถกด `Tab` หลังคำสั่งเพื่อดูรายการ screen ที่มีทั้งหมดได้
```bash
screen -R <screen_name>
```
* ขั้นตอนที่ 1 เข้าไปยัง screen ด้วย ID
```bash
screen -R id.<screen_name>
```
* ขั้นตอนที่ 2 ลบ screen
```bash
Ctrl + A + K + Y
```
