import re

def validate_cpf(cpf: str) -> bool:
    cpf = re.sub('[^0-9]', '', cpf)

    if len(cpf) != 11:
        return False

    if len(set(cpf)) == 1:
        return False

    sum1 = sum([int(cpf[i]) * (10 - i) for i in range(9)])
    remainder1 = 11 - (sum1 % 11)
    if remainder1 == 10 or remainder1 == 11:
        remainder1 = 0
    if remainder1 != int(cpf[9]):
        return False

    sum2 = sum([int(cpf[i]) * (11 - i) for i in range(10)])
    remainder2 = 11 - (sum2 % 11)
    if remainder2 == 10 or remainder2 == 11:
        remainder2 = 0
    if remainder2 != int(cpf[10]):
        return False

    return True
