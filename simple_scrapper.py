#!/usr/bin/env python3


import requests
import smtplib


# DONE: Recibir parametros (pagina, palabra clave, correo origen, credenciales, correo destino)
# DONE: Descargar la pagina
# DONE: Buscar dentro de la pagina la palabra clave
# TODO: Mandar correo si encontro la palabra si no imprimir en pantalla que no se encontro


def get_web_page(url: str) -> str:
    response = requests.get(url)
    return response.text


def keyword_look_up(web_page: str, keyword: str) -> bool:
    keyword = keyword.lower()
    for word in web_page.split():
        if keyword in word.lower():
            return True
    else:
        return False


def send_email(sender: str, credentials: str, receiver: str) -> bool:
    print("mandando correo men")
    pass


if __name__ == "__main__":

    import argparse
    import datetime

    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", type=str, help="Web page url")
    parser.add_argument("-k", "--keyword", type=str, help="Keyword to look up")
    parser.add_argument("-s", "--sender", type=str, help="Sender email")
    parser.add_argument("-c", "--credentials", type=str, help="Login credentials of sender email")
    parser.add_argument("-r", "--receiver", type=str, help="Receiver email")

    args = parser.parse_args()

    page = get_web_page(args.url)
    is_keyword_here = keyword_look_up(page, args.keyword)

    if is_keyword_here:
        send_email(args.sender, args.credentials, args.receiver)
    else:
        print(datetime.datetime.now().strftime("%d/%m/%y %H:%M.%S") + f" Todavia no hay {args.keyword} :'(")

    #        smtp = smtplib.SMTP('smtp.gmail.com', '587')
    #        smtp.starttls()
    #        smtp.login(os.environ['ORIGEN'], os.environ['MAGNOLIA'])
    #        smtp.sendmail(os.environ['ORIGEN'], os.environ['DESTINO'],
    #                      'Subject: Habemus MAGNOLIA!!!\n'
    #                      'Amor y Chico,\n\n'
    #                      'Ya hay MAGNOLIA revisen la pagina: http://parquestesistan.com/prototipos.html')
    #
