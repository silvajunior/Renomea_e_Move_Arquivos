import time
from datetime import datetime
import os
import binascii

def processarArquivo():
    datahora = datetime.now()
    dht = datahora.strftime("%d%m%Y%H%M%S")
    time.sleep(0.5)
    for nome in os.listdir('./arquivos'):
        dados = str(nome).split(".")
        print(nome)
        if dados[1] == "txt":
            hs = binascii.hexlify(os.urandom(2))
            hs = hs.decode()
            novo_nome = dados[0]+"_"+dht+"_" +hs+".txt"
            print(novo_nome)
            os.rename("./arquivos/"+nome, "./processados/"+novo_nome)
            time.sleep(0.1)
    print("Sem arquivos .txt!")

while True: 
    processarArquivo()
                
                
