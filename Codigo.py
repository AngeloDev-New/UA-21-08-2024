#Importando pandas e matplot para carregar o doc e lidar com os graficos
import pandas as pd
import matplotlib.pyplot as plt 
#o codigo buscara o documento dentro da pasta raiz...descomente a linha abaixo para ler apartir do git hub
DADOS = pd.read_excel("https://github.com/AngeloDev-New/UA-21-08-2024/raw/main/65561consumo.xlsx",sheet_name='consumo_resolução')

try:
    print(DADOS["Tempo"])
except:
    DADOS = pd.read_excel("65561consumo.xlsx",sheet_name='consumo_resolução')
    #Caso o documento excel n estiver na raiz e a linha 5 nao for descomentada o programa nao encontrara o arquivo de leitura
#print(type(dados["Data"][0]))

plt.figure(figsize=(10,6))

def media(listaValores):
    total = 0
    for valor in listaValores:
        total += valor
    return str(total/len(listaValores))
def quadrado_Ddiferencas(valores):
    quadrados = []
    for valor in valores:
        quadrados.append(valor*valor)
    return quadrados

def desvio_padrao(listaValores):
    #retirada a diferenca entre a media e a real
    mediaInterna = media(listaValores)
    diferencas_Dmedias = []
    for valor in listaValores:
        diferencas_Dmedias.append(float(valor)-float(mediaInterna))
    quadrado_Ddiferencas = (diferencas_Dmedias)
    #feita a media das diferencas
    mediaDquadrados = float(media(quadrado_Ddiferencas))
    #Raiz da media do quadrado das diferencas
    return str(mediaDquadrados**0.5)

def Amplitude(listaValores):
    maior = 0
    menor = 0
    for valor in listaValores:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
    return str(maior - menor)

def TAtivo(listaValores):
    minutos = 0
    for valor in listaValores:
        if valor != 0:
            minutos += 1 
    
    return str(int(minutos/60))+ " horas,"+str(minutos%60)+" minutos"
# Qual grupo de aparelhos apresenta maior média de consumo energético?
def questionA():
    dadosQTA = DADOS.copy()
    plt.plot(dadosQTA["Tempo"],dadosQTA["Grupo1"],marker="o",linestyle="dotted",label="Media Grupo1: "+media(dadosQTA["Grupo1"]))
    plt.plot(dadosQTA["Tempo"],dadosQTA["Grupo2"],marker="o",linestyle="dotted",label="Media Grupo2: "+media(dadosQTA["Grupo2"]))
    plt.plot(dadosQTA["Tempo"],dadosQTA["Grupo3"],marker="o",linestyle="dotted",label="Media Grupo3: "+media(dadosQTA["Grupo3"]))
    plt.title("Media de Consumo de cada grupo")
    plt.xlabel("Hora")
    plt.ylabel("Consumo")
    plt.grid(True)
    plt.legend()
    plt.show()
    
# Qual grupo apresenta maior coeficiente de variação?
# coeficiente de variacao e o (desvio_padrao/mediaConjunto)*100 gera uma porcentagen
def questionB():
    dadosQTB = DADOS.copy()
    plt.plot(dadosQTB["Tempo"],dadosQTB["Grupo1"],marker="o",linestyle="dotted",label="Desvio padrao Grupo1: "+desvio_padrao(dadosQTB["Grupo1"]))
    plt.plot(dadosQTB["Tempo"],dadosQTB["Grupo2"],marker="o",linestyle="dotted",label="Desvio padrao Grupo2: "+desvio_padrao(dadosQTB["Grupo2"]))
    plt.plot(dadosQTB["Tempo"],dadosQTB["Grupo3"],marker="o",linestyle="dotted",label="Desvio padrao Grupo3: "+desvio_padrao(dadosQTB["Grupo3"]))
    plt.title("Desvio padrao de cada grupo")
    plt.xlabel("Hora")
    plt.ylabel("Consumo")
    plt.grid(True)
    plt.legend()
    plt.show()
# Qual grupo apresenta maior amplitude de energia?
def questionC():
    dadosQTC = DADOS.copy()
    plt.plot(dadosQTC["Tempo"],dadosQTC["Grupo1"],marker="o",linestyle="dotted",label="Amplitude Grupo1: "+Amplitude(dadosQTC["Grupo1"]))
    plt.plot(dadosQTC["Tempo"],dadosQTC["Grupo2"],marker="o",linestyle="dotted",label="Amplitude Grupo2: "+Amplitude(dadosQTC["Grupo2"]))
    plt.plot(dadosQTC["Tempo"],dadosQTC["Grupo3"],marker="o",linestyle="dotted",label="Amplitude Grupo3: "+Amplitude(dadosQTC["Grupo3"]))
    plt.title("Amplitude de cada grupo")
    plt.xlabel("Hora")
    plt.ylabel("Consumo")
    plt.grid(True)
    plt.legend()
    plt.show()
#  Qual grupo permanece mais tempo desligado, ou seja, sem consumir energia? Como você chegou a essa conclusão?
def questionD():
    dadosQTD = DADOS.copy()
    plt.plot(dadosQTD["Tempo"],dadosQTD["Grupo1"],marker="o",linestyle="dotted",label="Tempo Ativo Grupo1: "+TAtivo(dadosQTD["Grupo1"]))
    plt.plot(dadosQTD["Tempo"],dadosQTD["Grupo2"],marker="o",linestyle="dotted",label="Tempo Ativo Grupo2: "+TAtivo(dadosQTD["Grupo2"]))
    plt.plot(dadosQTD["Tempo"],dadosQTD["Grupo3"],marker="o",linestyle="dotted",label="Tempo Ativo Grupo3: "+TAtivo(dadosQTD["Grupo3"]))
    plt.title("Tempo ativo de cada grupo")
    plt.xlabel("Hora")
    plt.ylabel("Consumo")
    plt.grid(True)
    plt.legend()
    plt.show()

questionA()
questionB()
questionC()
questionD()
