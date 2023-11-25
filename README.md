# ALBEDO - PDF Generator :page_facing_up:

### Run on localhost (without Docker)
1. install [wkhtmltopdf](https://wkhtmltopdf.org/downloads.html)
2. install required libraries & start uvicorn server
```
pip install -r requirements.txt
uvicorn main:app --reload
```
3. try [http://127.0.0.1:8000/form3?id=6510749999](http://127.0.0.1:8000/form3?id=6510749999)

### Examples
<img src="https://github.com/zenosaika/albedo/blob/main/form3example.png">