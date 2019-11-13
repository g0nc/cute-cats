#Setando Bibliotecas

import requests
import json
import urllib.request
###########FIM BIBLIOTECAS###############
#COMENTARIOS INUTEIS#

#Id reference set
#{'id': 5, 'name': 'boxes'}
#{'id': 15, 'name': 'clothes'}
#{'id': 1, 'name': 'hats'}
#{'id': 14, 'name': 'sinks'}
#{'id': 2, 'name': 'space'}
#{'id': 4, 'name': 'sunglasses'}
#{'id': 7, 'name': 'ties'}

#CAT APY KEY=2a20fc5a-9387-418f-bbd3-0a18a91eab2c
##########FIM COMENTARIOS INUTEIS##################

#CODIGO#

def pesquisar(opcao, quantidade):
    
    for n in range(quantidade):

        headers = {'x-api-key': '2a20fc5a-9387-418f-bbd3-0a18a91eab2c', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
        req = requests.get("https://api.thecatapi.com/v1/images/search?category_ids="+str(opcao))
        load = json.loads(req.text)
        for itens in load:
            image_name = itens['id']+".jpg"
            image_url = itens['url']
            print("O nome do arquivo eh: "+str(image_name)+" e o URL para acessar eh: "+str(image_url))
            with open(image_name, 'wb') as handle:
                response = requests.get(image_url, stream=True)
                if not response.ok:
                    print(response)

                for block in response.iter_content(1024):
                    if not block:
                        break
                    handle.write(block)
            print("Imagem Salva Com Sucesso!!!!")



def banner():
    print("I'am your cat script, i`m here to download your cat images with u choose")
    print(",_     _,")
    print("|\\___//|")
    print("|=6   6=|")
    print("\=._Y_.=/")
    print(" )  `  (    ,")
    print("/       \  ((")
    print("|        |   ))")
    print("/| |   | |\_//")
    print("\| |._.| |/-`")
    print(" '"'   '"' ")
      

    print("""SELECT YOUR OPTION: \n\n [1] - GATOS COM CHAPEUS \n [2] - GATOS NO ESPACO(UNIVERSO) \n [4] - GATOS COM OCULOS DE SOL \n [5] - GATOS DENTRO DE CAIXAS \n [7] - GATOS COM GRAVATAS \n [14] - GATOS WITH SINKS \n [15] - GATOS COM ROUPA""")
    opcao = input("Digite a opcao aqui: ")
    quantidade = int(input("Quantas fotos voce quer?: "))
    if(opcao == "1"):
        opcao_result = True
    elif(opcao == "2"):
        opcao_result = True
    elif(opcao == "4"):
        opcoa_result = True
    elif(opcao == "5"):
        opcao_result = True    
    elif(opcao == "7"):
        opcao_result = True
    elif(opcao == "14"):
        opcao_result = True
    elif(opcao == "15"):
        opcao_result = True
    else:
        print("Opcao Incorreta, tente novamente com uma das opcoes listadas no menu acima!!!")

    if(opcao_result==True):
        pesquisar(opcao, quantidade)



#FIM CODIGO#

banner()
