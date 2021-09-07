import smtplib
from random import randint, randrange
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from colorama import Fore, init
#importação das libs

#coloroma init
init(autoreset=True)

to = str(input('Email para verificação\n>:')) #onde sera enviado o email de verificação

port = "587"                #porta usada e host
hostGm = "smtp.gmail.com"

with open('2324235463') as c:      #abrindo o arquivo e pegar o codigo que esta dentro
    line = c.read()                #e usar o codigo para gerar o numero aleatório

    global code
    code = eval(line)



with open('7277777777796667773') as pw:
    lines = pw.read().splitlines()      #abrir o arquivo pegar as informações para login
    
    global a, b
    a = lines[0]
    b = lines[1] 
    

server = smtplib.SMTP(hostGm, port)
server.ehlo()                       #server start
server.starttls()


server.login(a,b) #login

#corpo do email e mime type
body = "Seu codigo de verificação: {code} não feiche a o programa senao o codigo se tornará inútil".format(code=code)
msgEmail = MIMEMultipart()

#informações
msgEmail['From'] = a
msgEmail['To'] = to
msgEmail['Subject'] = 'Seu codigo de verificação chegou! {code}'.format(code=code)
msgEmail.attach(MIMEText(body,'plain'))

#enviar o codigo
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

#dr00x_