#!/usr/bin/env python3

import requests
import smtplib
import os
import datetime

if __name__ == "__main__":
    response = requests.get('http://parquestesistan.com/prototipos.html')
    page_text = response.text
    for word in page_text.split():
        if 'magnolia' in word.lower():
            smtp = smtplib.SMTP('smtp.gmail.com', '587')
            smtp.starttls()
            smtp.login(os.environ['ORIGEN'], os.environ['MAGNOLIA'])
            smtp.sendmail(os.environ['ORIGEN'], os.environ['DESTINO'],
                          'Subject: Habemus MAGNOLIA!!!\n'
                          'Amor y Chico,\n\n'
                          'Ya hay MAGNOLIA revisen la pagina: http://parquestesistan.com/prototipos.html')
            break
    else:
        print(datetime.datetime.now().strftime("%d/%m/%y %H:%M.%S") + " Todavia no hay Magnolia :'(")
