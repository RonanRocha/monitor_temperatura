import serial
from serial.tools import list_ports
import time
import re
from mailersend import MailerSendClient, EmailBuilder
from dotenv import load_dotenv
load_dotenv()


def sendEmail(temperatura, umidade):
    try:
        

        ms = MailerSendClient()

        email = (EmailBuilder()
        .from_email("info@test-86org8e1mqzgew13.mlsender.net", "Projeto Integrador")
        .to_many([{"email": "ronan.rochasouza@gmail.com", "name": "Ronan"}])
        .subject("TEMPERATURA OU UMIDADE CAMARA UMIDA NÃO CONFORME")
        .html(f"TEMPERATURA OU UMIDADE CÂMARA ÚMIDA NÃO CONFORME\n"
              f"TEMPERATURA: {temperatura}\n"
              f"UMIDADE: {umidade}")
        .build())

        response = ms.emails.send(email)

        if response.success:
            print("E-mail enviado")
        else:
            print("Não foi possível enviar e-mail")
    except:
        print("Não foi possível enviar e-mail")


def menu():
    try:
        ports = list(list_ports.comports())
        print('PORTAS SERIAIS DISPONÍVEIS')

        if not ports:
            print("NENHUMA PORTA SERIAL ENCONTRADA.")
            exit()

        for i, port in enumerate(ports, start=1):
            print(f"{i} - {port.device} | {port.description}")

        choosedPort = int(input("\nSELECIONE A PORTA PELO NÚMERO: "))

        if 1 <= choosedPort <= len(ports):
            selectedPort = ports[choosedPort - 1].device
            return selectedPort
    
        print("OPCAO INVALIDA TENTE NOVAMENTE")

    except:
        print("ERRO MENU")


def bootstrap():
    selectedPort = menu()
    # conexao com a porta serial, recebe as informações
    arduino = serial.Serial(selectedPort, 9600)
    #aguarda 2 segundos
    time.sleep(2);
    monitoringCOM(arduino)


def monitoringCOM(arduino):

    temperatura = None
    umidade = None

    #loop infinito para monitoramento
    while True:
        #le o que foi enviado pela porta serial COM , decodifica para utf8, remove espaçõs  em branco do inicio e fim da string
        saidaCom = arduino.readline().decode().strip()
        # regex para recuperar o valor da umidade
        match_umidade = re.search(r"Umidade:\s*([\d.,]+)\s*%", saidaCom)
        # se der match com o padrão converte para float e troca virgula por ponto
        if match_umidade:
            umidade = float(match_umidade.group(1).replace(',', '.'))

        # regex para procura a temperatura
        match_temperatura = re.search(r"Temperatura:\s*([\d.,]+)\s*°C", saidaCom)
        # se der match com o padrão converte para float e troca virgula por ponto
        if match_temperatura:
            temperatura = float(match_temperatura.group(1).replace(',', '.'))

        if temperatura is not None and umidade is not None:
            print(f"Temperatura: {temperatura:.2f} °C")
            print(f"Umidade: {umidade:.2f} %")
            print("----------------------")

            #se a temperatura for maior que 30 graus celsius e a umidade estiver abaixo de 65 notifica o usuario e espera 1 minuto para rodar novamente
            if temperatura > 25.00 or umidade <= 95.00: 
                
                print("notificar por email que a sala não está em condições ideias");
                sendEmail(temperatura, umidade);
                time.sleep(300)
            

            temperatura = None
            umidade = None


bootstrap()






