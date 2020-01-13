ateNove = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
ateDezenove= ["onze", "doze", "treze", "catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
dezenas = ["dez", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
centenas = [["cem", "cento"], "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"]
milhares = ["mil"]

def handleTens(numDezena, numUnidade):
    text = ""
    if numDezena > 0 and numDezena == 1:
        if numUnidade == 0:
            text += dezenas[numDezena-1]
        else:
            text += ateDezenove[numUnidade-1]

    elif numDezena > 1:
        if numUnidade == 0:
            text += dezenas[numDezena-1]
        else:
            text += dezenas[numDezena-1] + ' e ' +  ateNove[numUnidade]

    elif numUnidade > 0:
        text += ateNove[numUnidade]

    return text

def translate(number):
    """Recebe um número (int) entre -9999 e 9999 e retorna seu valor por extenso"""
    prefix = ""
    extenso = ""

    if number == 0:
        return ateNove[0]

    if number < 0:
        prefix = 'menos '
        number = abs(number)

    numStr              = str(number)
    numberFormatted     = numStr.zfill(5);
    numDezenaMilhar     = int(numberFormatted[0])
    numUnidadeMilhar    = int(numberFormatted[1])
    numCentena          = int(numberFormatted[2])
    numDezena           = int(numberFormatted[3])
    numUnidade          = int(numberFormatted[4])

    # XX000 tratando dezena de milhar e unidade de milhar
    extenso += handleTens(numDezenaMilhar, numUnidadeMilhar)

    # adiciona 'mil' após definir as unidades
    extenso += ' ' + milhares[0] if extenso != "" else ""

    # adiciona o 'e' caso o a escrita por extenso já fora iniciada e ainda tenha dígitos para traduzir
    extenso += ' e ' if extenso != "" and numCentena > 0 else ""

    # 00X00 tratando a centena
    if numCentena > 0 and numCentena == 1:
        if numDezena == 0 and numUnidade == 0:
            extenso += centenas[0][0]
        else:
            extenso += centenas[0][1]

    elif numCentena > 1:
        extenso += centenas[numCentena-1]

    # adiciona o 'e' caso o a escrita por extenso já fora iniciada e ainda tenha dígitos para traduzir
    extenso += ' e ' if extenso != "" and (numDezena > 0 or numUnidade) > 0 else ""

    #000XX tratando a dezena e unidade
    extenso += handleTens(numDezena, numUnidade)

    return prefix + extenso
