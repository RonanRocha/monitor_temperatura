#include <DHT.h>//Inclui a biblioteca DHT Sensor Library 
#define DHTPIN 2//Pino digital 2 conectado ao DHT11 
#define DHTTYPE DHT11//DHT 11 

DHT dht(DHTPIN, DHTTYPE);//Inicializando o objeto dht do tipo DH

void setup() {
  Serial.begin(9600);//Inicializa a comunicação serial 
  dht.begin();//Inicializa o sensor DHT11

}

void loop() {
  delay(2000);//Intervalo de dois segundos entre as medições 
    float h = dht.readHumidity();//lê o valor da umidade e armazena na variável h do tipo float (aceita números com casas decimais) 
    float t = dht.readTemperature();//lê o valor da temperatura e armazena na variável t do tipo float (aceita números com casas decimais) 
    if (isnan(h) || isnan(t)) {//Verifica se a umidade ou temperatura são ou não um número 
      return;//Caso não seja um número retorna 
    } 
    Serial.print("Umidade: ");//Imprime no monitor serial a mensagem "Umidade: " 
    Serial.print(h);//Imprime na serial o valor da umidade 
    Serial.println("%");//Imprime na serial o caractere "%" e salta para a próxima linha 
    Serial.print("Temperatura: ");//Imprime no monitor serial a mensagem "Temperatura: " 
    Serial.print(t);//Imprime na serial o valor da temperatura  
    Serial.println("°C ");//Imprime no monitor serial "ºC" e salta para a próxima linha  

}
