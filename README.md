# ALBEDO - PDF Generator :page_facing_up:

### Run on localhost (without Docker)
1. install [wkhtmltopdf](https://wkhtmltopdf.org/downloads.html)
2. install required libraries & start uvicorn server
```
pip install -r requirements.txt
uvicorn main:app --reload
```
3. try [http://127.0.0.1:8000/form3?id=6510749999](http://127.0.0.1:8000/form3?id=6510749999)

### Run on localhost (with Docker)
1. build docker image & start container
```
docker build -t albedo .
docker run -dp 8000:8000 albedo
```
2. try [http://127.0.0.1:8000/form3?id=6510749999](http://127.0.0.1:8000/form3?id=6510749999)

### Deploy to fly.io
1. install [flyctl](https://fly.io/docs/hands-on/install-flyctl/)
2. just
```
fly launch
```

### Note
- อันนี้ผม deploy ไว้ ลองเข้าไปดูได้ครับ [Link](https://albedo.fly.dev/form3?id=6510749999)
- จะเห็นปัญหาว่า wkhtmltopdf พอมัน render ใน linux มันจะไม่เหมือน render ใน macos, window (อ้างอิงจากภาพด้านล่าง render ใน macos) ซึ่งปัญหาเท่าที่อ่าน stack overflow มา เป็นเพราะ version ของ wkhtmltopdf ตอนนี้เราใช้ 0.12.6 เขาแนะนำให้อัพเป็น 0.13.*
- ผมมีการปรับชื่อ column ในไฟล์ form3response.csv ใหม่ เพราะเดิมมีชื่อ column ซ้ำ ซึ่งผมจะใช้ชื่อ column ในการดึงข้อมูล ดังนั้นถ้าเอาไฟล์ csv ใหม่มา อย่าลืมปรับชื่อ column ตามด้วยนะครับ
- ถ้าจะทำให้มันดึง google form response มาจาก google sheet เลยก็ทำได้นะครับ ผมสร้าง agent ไว้แล้ว แค่เพิ่ม permission เข้าถึง google sheet ให้มัน (code ผมเก็บไว้อยู่อีกโปรเจคนึง)

### Examples
<img src="https://github.com/zenosaika/albedo/blob/main/form3example.png">