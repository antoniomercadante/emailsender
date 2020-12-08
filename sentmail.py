import smtplib
import sys
import email.utils
import getpass

mailserver = "smtp.gmail.com"
mailport = "587"
mailuser = ""
try:
    mailpasswd = getpass.getpass('Senha para %s: \n' % mailuser)

    De = input('De? ').strip()
    Para = input('Para? ').strip()
    Paras = Para.split(';')
    Assunto = input('Assunto? ').strip()
    Data = email.utils.formatdate()

    texto = ('From: %s\nTo: %s\nDate: %s\nSubject: %s\n\n' % (De, Para, Data, Assunto))

    print('Escreva a mensagem, fim de linha dado por=[Ctrl+d]')
    while True:
        linha = sys.stdin.readline()
        if not linha: break
        texto += linha

    print('Conectando...')
    server = smtplib.SMTP(mailserver, mailport)
    server.starttls()
    server.login(mailuser, mailpasswd)
    falhou = server.sendmail(De, Paras, texto)
    server.quit()

    if falhou:
        print('Envio Falhou:', falhou)
    else:
        print('Enviado com Sucesso.')

except Exception as er:
    print("Erro %s" %er)

except KeyboardInterrupt:
    print("Saindo")

