import os
import csv
import base64
import pandas as pd

from html2pdf import html2pdf

from fastapi import FastAPI
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get('/')
def main():
    return "what is love? baby don't hurt me!"


@app.get('/form3')
def get_form3(id: str = ''):

    if id == '':
        return {'error': 'id is not specified'}
    
    with open('inputs/form3response.csv', 'r') as f:
        csvreader = csv.reader(f)
        header = next(csvreader)
        rows = [row for row in csvreader]

    df = pd.DataFrame(rows, columns=header)
    df = df[df.เลขทะเบียนนักศึกษา == id] # select where id == id

    if df.empty:
        return {'error': 'data not found'}

    df = df.iloc[-1] # get last record of this id
    
    # read and convert TSE logo image to base64
    root = os.path.dirname(os.path.abspath(__file__))
    tse_logo_path = os.path.join(root, 'templates', 'tse_logo.png')
    with open(tse_logo_path, 'rb') as img:
        tse_logo_base64 = base64.b64encode(img.read()).decode()
    
    template_name = 'form3'

    contexts = {
        'id': id, 
        'tse_logo_base64': tse_logo_base64,
        'student': {
            'name': df['ชื่อ-นามสกุล'],
            'id': df['เลขทะเบียนนักศึกษา'],
            'phone': df['เบอร์โทรติดต่อ'],
            'email': df['อีเมล']
        },
        'company': f"{df['ชื่อสถานประกอบการ (ภาษาอังกฤษ)']} ({df['ชื่อสถานประกอบการ (ภาษาไทย)']})",
        'fromdate': df['จะเริ่มต้นฝึกงานตั้งแต่'],
        'todate': df['ถึงเดือน'],
        'job': df['ตำแหน่งงานที่นักศึกษาไปฝึก'],
        'job_description': df['ลักษณะงานที่ไปฝึกงานระยะยาวตามที่นักศึกษาได้ติดต่อสอบถาม'],
        'recipient': {
            'name': df['ชื่อ-นามสกุล (ผู้รับหนังสือขอความอนุเคราะห์)'],
            'role': df['ตำแหน่ง (ผู้รับหนังสือขอความอนุเคราะห์)'],
            'phone': df['เบอร์โทรติดต่อ (ผู้รับหนังสือขอความอนุเคราะห์)'],
            'email': df['อีเมล (ผู้รับหนังสือขอความอนุเคราะห์)']
        },
        'coordinator': {
            'name': df['ชื่อ-นามสกุล (ผู้ประสานงานในการติดต่อและส่งเอกสาร)'],
            'role': df['ตำแหน่ง (ผู้ประสานงานในการติดต่อและส่งเอกสาร)'],
            'phone': df['เบอร์โทรติดต่อ (ผู้ประสานงานในการติดต่อและส่งเอกสาร)'],
            'email': df['อีเมล (ผู้ประสานงานในการติดต่อและส่งเอกสาร)']
        },
        'addr': {
            'no': df['ที่อยู่เลขที่'],
            'alley': df['ซอย'],
            'street': df['ถนน'],
            'subdistrict': df['แขวง/ตำบล'],
            'district': df['เขต/อำเภอ'],
            'province': df['จังหวัด'],
            'postalcode': df['รหัสไปรษณีย์'],
            'phone': df['โทรศัพท์']
        }
    }

    # https://wkhtmltopdf.org/usage/wkhtmltopdf.txt
    options = {
        'page-size': 'A4',
        'orientation':'Portrait',
        'encoding': 'UTF-8',
        'dpi': 300,
    }

    err, pdf = html2pdf(template_name, contexts, options)

    if err:
        return err
    
    headers = {"Content-Disposition": f"inline; filename={id}.pdf"}
    response = Response(pdf, media_type="application/pdf", headers=headers)

    return response
