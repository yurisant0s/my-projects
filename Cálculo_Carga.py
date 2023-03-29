
for i in range(4):
    caminhao = int(input('Informe o número do caminhão desejado de 1 a 4: '))
    cod = int(input('Informe de 1 a 5 o código do estado de origem da carga do caminhão: '))
    peso = int(input('Informe o peso da carga do caminhão em toneladas: '))
    carga = int(input('Informe o código de carga entre 10 e 40: '))
    conversao = peso * 1000
    if carga==10<20:
      preco_carga = 100 * conversao
    elif carga==21<30:
      preco_carga = 250 * conversao
    elif carga == 30<40:
      preco_carga = 340 * conversao
    if cod == 1:
     percent = 0.35 * preco_carga
     imposto = percent + preco_carga
    elif cod == 2:
        percent = 0.25 * preco_carga
        imposto = percent + preco_carga
    elif cod == 3:
        percent = 0.15 * preco_carga
        imposto = percent + preco_carga
    elif cod == 4:
        percent = 0.05 * preco_carga
        imposto = percent + preco_carga
    elif cod == 5:
        percent = 0 * preco_carga
        imposto = percent + preco_carga
    print('O caminhão de número {} irá transportar um total de {}Kg, e o preço da carga será de R${:.2f}'.format(caminhao, conversao, imposto))






















