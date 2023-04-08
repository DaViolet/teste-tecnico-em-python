from datetime import datetime
import holidays
#pip install holidays --para instalar o módulo holidays


def pergunta1():
    permanenciaUsuario = "S"
    totalGeral = 0.00
    contador = 0

    while (permanenciaUsuario != "N"):
        ano = float(input("Insira o ano de lançamento do veículo."))
        print(ano)

        valorOriginal = float(input("Insira o valor inicial do veículo."))

        if (int(ano) <= 2000):
            totalGeral += ((valorOriginal) * 0.88)
            contador = contador + 1
        else:
            totalGeral += ((valorOriginal) * 0.93)

        print(f"A contagem de carros de ano 2000 é de {contador}.")
        print(f"O total da compra é de R${totalGeral:.2f}.")
        permanenciaUsuario = input("Caso deseje encerrar a aplicação, digite 'N'. Para prosseguir, basta teclar ENTER.")
        print("Aplicação encerrada com sucesso.")


def pergunta2():
    while True:
        codigo_aluno = int(input("Insira o código do aluno. Caso queira encerrar a aplicação, digite 0."))
        if codigo_aluno == 0:
            break
        nota_1 = float(input("Insira a primeira nota: "))
        nota_2 = float(input("Insira a segunda nota: "))
        nota_3 = float(input("Insira a terceira nota: "))

        maior_nota = max(nota_1, nota_2, nota_3)
        media_simples = (4 * maior_nota + 3 * (nota_1 + nota_2 + nota_3 - maior_nota)) / 9

        print(f"Notas do Aluno {codigo_aluno}: {nota_1}, {nota_2}, {nota_3} => Média: {media_simples:.2f} ({'APROVADO' if media_simples >= 6 else 'REPROVADO'})")


def pergunta3():
    print("A) a = 1, b = 2, c = 3")
    print("Não é possível formar um triângulo")
    print("B) a = 3, b = 4, c = 5")
    print("Triângulo Escaleno")
    print("C) a = 2, b = 2, c = 4")
    print("Não é possível formar um triângulo")
    print("D) a = 4, b = 4, c = 4")
    print("Triângulo Equilátero")
    print("E) a = 5, b = 3, c = 3")  
    print("Triângulo Isósceles")


def pergunta4():

    data_vencimento_str = input("Insira a data de vencimento original: (DD/MM/YYYY): ")
    data_vencimento_date = datetime.strptime(data_vencimento_str, "%d/%m/%Y").date()

    verifica_feriado = (verificaFeriado(data_vencimento_str))
    verifica_final_de_semana = verificaFinalDeSemana(data_vencimento_date)
    proximo_dia_util = verificaProximoDiaUtil(data_vencimento_date)

    data_pagamento_str = input("Insira a data de pagamento (DD/MM/YYYY): ")
    data_pagamento_date = datetime.strptime(data_pagamento_str, "%d/%m/%Y").date()

    valor_boleto = float(input("Insira o valor do boleto: "))
    dias_atrasados = (data_pagamento_date - data_vencimento_date).days
    juros = 0.03 * dias_atrasados
    multa = 2.00
    valor_total = 0

    if (verifica_feriado is True and dias_atrasados > 1):
        valor_total = valor_boleto + juros + multa
    elif (verifica_feriado is True or verifica_final_de_semana is True and (proximo_dia_util - dias_atrasados) == 0):
        juros = 0
        multa = 0
        valor_total = valor_boleto + juros + multa
    elif (verifica_feriado is True or verifica_final_de_semana is True and (proximo_dia_util - dias_atrasados) < 0):
        juros = 0.03 * (dias_atrasados+1)
        valor_total = valor_boleto + juros + multa
    elif (verifica_feriado is True and (proximo_dia_util - dias_atrasados) == 0):
        juros = 0
        valor_total = valor_boleto + juros + multa
    elif (verifica_feriado is True and proximo_dia_util == 2 and dias_atrasados == 3):
        juros = 0
        multa = 0
        valor_total = valor_boleto + juros + multa
    elif (dias_atrasados < 0):
        juros = 0
        multa = 0
        valor_total = valor_boleto + juros + multa
    elif (proximo_dia_util - dias_atrasados) == -1:
        valor_total = valor_boleto + juros + multa
    else:
        juros = 0
        multa = 0
        valor_total = valor_boleto + juros + multa

    print(f"Total: {valor_total}")


def verificaFeriado(date):
    feriados = holidays.Brazil()
    feriados_collection = []

    for feriado in feriados['2023-01-01': '2023-12-31'] :
        feriados_collection.append(feriado)

    feriados_collection_formatado = [f.strftime('%d/%m/%Y') for f in feriados_collection]
    #adicionando o dia do trabalhador
    feriados_collection_formatado.append('01/05/2023') 
    #lista de feriados gerada: ['01/01/2023', '21/02/2023', '22/02/2023', '07/04/2023', '09/04/2023', '21/04/2023', '01/05/2023', '08/06/2023', '07/09/2023', '12/10/2023', '02/11/2023', '15/11/2023', '25/12/2023', '01/05/2023']  

    if feriados_collection_formatado.count(date) > 0:
        return True
    else:
        return False


def verificaFinalDeSemana(date):
    if (date.weekday() == 5 or date.weekday() == 6):
        return True
    else:
        return False


def verificaProximoDiaUtil(date):
    if (date.weekday() == 5):
        return 2
    elif (date.weekday() == 6):
        return 1
    else:
        return 0

#Chamada dos algoritmos:
#pergunta1()
#pergunta2() 
#pergunta3()
#pergunta4()