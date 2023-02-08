import socket

nome_servidor = "localhost"
porta_servidor = 12345
socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
numero_questao = input("""Selecione o tema da questao:
1- Matematica
2- Historia
3- Geografia
""")
socket_cliente.sendto(numero_questao.encode(), (nome_servidor, porta_servidor))

if numero_questao == "1":
    print("""Questao de Matematica:
Assinale V para verdadeiro e F para falso.

I- A soma dos quadrados dos catetos de um triângulo é igual ao
quadrado de sua hipotenusa.
II- O quadrado da hipotenusa é igual a diferença dos
quadrados dos catetos.
III - Hipotenusa: é o lado oposto ao ângulo reto, sendo considerado o
maior lado do triângulo retângulo.
IV - Catetos: são os lados do triângulo que formam o ângulo reto. São
classificados em: cateto adjacente e cateto oposto.
V- A trigonometria é a ciência responsável pelas relações
estabelecidas entre os triângulos. Estes são figuras geométricas
espaciais compostas de três lados e três ângulos internos.
""")
elif numero_questao == "2":
    print("""Questao de Historia:
Assinale com V (verdadeiro) ou com F (falso) as seguintes afirmações,
sobre fatos históricos relativos ao fim do Império no Brasil.

I- Em 1870, foi fundado o Partido Republicano no Rio de Janeiro, cujo
manifesto defendia a descentralização política com base no federalismo
e a convocação de uma Assembleia Constituinte para realizar
a mudança de governo.
II- Medida importante para a abolição da escravatura, a chamada Lei do
Ventre Livre, de 1871, contou com amplo apoio dos republicanos e
enfrentou maior resistência dos deputados oriundos das províncias do
norte, ainda fortemente dependentes do trabalho escravo.
III- A reforma eleitoral aprovada em 1881 estabeleceu as eleições
diretas, anulando a proibição do voto dos analfabetos e simplificando
o processo de comprovação de renda para o voto censitário, o que
ampliou o número de eleitores e enfraqueceu o poder político central.
IV- Amparada pela vitória na Guerra do Paraguai, a ascensão política
dos militares, influenciados pelos ideais republicanos e
abolicionistas do positivismo, foi elemento importante para a
derrocada da monarquia no Brasil.
""")
elif numero_questao == "3":
    print("""Questao de Geografia:
        Em relacao a posicao geográfica do Brasil:

I- O território brasileiro está totalmente ao sul da linha do Equador,
portanto, o país pertence somente ao Hemisfério meridional.
II- Os extremos do território do Brasil no sentido leste-oeste são:
Monte Caburaí (Roraima) e Arroio Chuí (Rio Grande do Sul).
III- O Brasil pertence ao Hemisfério ocidental, visto que o país está
situado a oeste do meridiano de Greenwich.
IV- O Trópico de Capricórnio “corta” o território brasileiro
na sua porção sul.
V- Cortado ao norte pela linha do Equador, o Brasil possui 7%
do seu território no Hemisfério setentrional e 93% no
Hemisfério meridional.
""")
else:
    print("Questao Invalida")
    print("Cliente encerrado!")
    exit()

numero_de_opcoes = int(input("Ha quantas opcoes?"))
resposta = input("Qual a resposta de cada opcao?")
socket_cliente.sendto(resposta.encode(), (nome_servidor, porta_servidor))
resultado_mensagem, serverAddress = socket_cliente.recvfrom(2048)
print("Resultado:", resultado_mensagem.decode("utf-8"))
socket_cliente.close()
