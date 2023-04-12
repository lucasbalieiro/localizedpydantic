import re

def validate_cpf(cpf: str) -> bool:
    cpf = re.sub('[^0-9]', '', cpf)

    if len(cpf) != 11:
        return False

    if len(set(cpf)) == 1:
        return False

    soma = sum([int(cpf[i]) * (10 - i) for i in range(9)])
    resto = 11 - (soma % 11)
    if resto == 10 or resto == 11:
        resto = 0
    if resto != int(cpf[9]):
        return False

    soma = sum([int(cpf[i]) * (11 - i) for i in range(10)])
    resto = 11 - (soma % 11)
    if resto == 10 or resto == 11:
        resto = 0
    if resto != int(cpf[10]):
        return False

    return True
