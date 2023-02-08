import socket

porta_servidor = 12345
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_servidor.bind(('', porta_servidor))

print("Servidor Iniciado!")
print('='*30)

acertos = 0
erros = 0

while 1:
    numero_questao, clientAddress = socket_servidor.recvfrom(2048)
    numero_questao = numero_questao.decode("utf-8")
    print("Questao " + numero_questao + " selecionada!")

    if numero_questao == "1":
        questao1 = "VFVVF"
        print("resposta correta: ", questao1)

        resposta, clientAddress = socket_servidor.recvfrom(2048)
        resposta = resposta.decode("utf-8")
        for x, y in zip(resposta, questao1):
            if x.capitalize() == y.capitalize():
                acertos += 1
            else:
                erros += 1

    elif numero_questao == "2":
        questao2 = "VFFV"
        print("resposta correta: ", questao2)

        resposta, clientAddress = socket_servidor.recvfrom(2048)
        resposta = resposta.decode("utf-8")
        for x, y in zip(resposta, questao2):
            if x.capitalize() == y.capitalize():
                acertos += 1
            else:
                erros += 1
    elif numero_questao == "3":
        questao3 = "FFVVV"
        print("resposta correta: ", questao3)

        resposta, clientAddress = socket_servidor.recvfrom(2048)
        resposta = resposta.decode("utf-8")
        for x, y in zip(resposta, questao3):
            if x.capitalize() == y.capitalize():
                acertos += 1
            else:
                erros += 1
    else:
        print("Questao não encontrada!")

    resultado_mensagem = f"{numero_questao};{acertos};{erros}"
    resultado_mensagem = resultado_mensagem.encode("utf-8")
    socket_servidor.sendto(resultado_mensagem, clientAddress)

    acertos = 0
    erros = 0
