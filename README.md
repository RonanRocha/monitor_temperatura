# Sensor de temperatura

> Descrição curta: software que detecta o Arduino e exibe a temperatura atual e manda para seu email.

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)

## Sobre

Esse software tem como objetivo ler a temperatura via arduino (Apenas testado com arduino uno)

Ao ser aberto, o software:

1. Procura conexao na porta serial 3;
2. Identifica a porta;
3. Lê o sensor de temperatura;
4. Manda a temperatura atual para o email.

## Funcionalidades
- [ ] Detecção do Arduino
- [ ] Leitura da temperatura atual
- [ ] Envio para o email

## Requisitos

### Hardware
- Arduino UNO
- Sensor de temperatura LM35
- Cabo USB
- Jumpers

### Software
- Python
- API mailersend, serial e dotEnv
- Vs code e Arduino UNO

## Configuração

1. Serial na porta 3
2. API key salva do mailersend na ENV


## Instalação

```bash
# Clonar o repositório
git clone https://github.com/RonanRocha/monitor_temperatura.git
cd monitor_temperatura

# Instalar dependências
pip install -r requirements.txt
```

## Como Usar

```bash
git clone https://github.com/RonanRocha/monitor_temperatura.git
cd monitor_temperatura
python monitor.py
```

Saída esperada:

```
Temperatura: XX °C
Umidade: XX.XX %
```

## Exemplos:

<h3>Terminal<h3>

![Tela principal do software (Terminal)](assets/print_softwares/terminal.png)

<h3>Email</h3>

![Tela principal do software (Emial)](assets/print_softwares/email.png)

