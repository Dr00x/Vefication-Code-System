import smtplib
from random import randint, randrange
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from colorama import Fore, init

init(autoreset=True)

to = str(input('Email para verificação\n>:'))

port = "587"
hostGm = "smtp.gmail.com"
with open('2324235463') as c:
    line = c.read()

    global code
    code = eval(line)



with open('7277777777796667773') as pw:
    lines = pw.read().splitlines()
    
    global a, b
    a = lines[0]
    b = lines[1] 
    

server = smtplib.SMTP(hostGm, port)
server.ehlo()
server.starttls()


server.login(a,b)


body = "Seu codigo de verificação: {code} não feiche a o programa senao o codigo se tornará inútil".format(code=code)
msgEmail = MIMEMultipart()

msgEmail['From'] = a
msgEmail['To'] = to
msgEmail['Subject'] = 'Seu codigo de verificação chegou! {code}'.format(code=code)
msgEmail.attach(MIMEText(body,'plain'))

try:
    server.sendmail(msgEmail['From'],msgEmail['To'], msgEmail.as_string())
except:
    print(Fore.RED + "Um erro ocorreu, verifique o seu email e reinicie o programa [pressione qualquer tecla]")
    input()
    quit()

inpCode = int(input('\nDigite o codigo enviado\n>:'))

if inpCode == code:
    print(Fore.GREEN + "Codigo correto")
    quit()
else:
    print(Fore.RED + "Codigo incorreto")
    quit()

