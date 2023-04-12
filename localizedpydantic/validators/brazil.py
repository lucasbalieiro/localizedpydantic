import re

def validate_cpf(cpf: str) -> bool:
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

def validate_cnpj(cnpj: str) -> bool:
    cnpj = re.sub(r'\D', '', cnpj)

    if not cnpj.isdigit():
        return False

    if len(cnpj) != 14:
        return False

    invalid_numbers = [str(i) * 14 for i in range(10)]
    if cnpj in invalid_numbers:
        return False

    weight1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    weight2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    cnpj_digit = cnpj[-2:]
    cnpj = cnpj[:-2]

    total1 = sum([int(a) * b for a, b in zip(cnpj, weight1)])
    remainder1 = total1 % 11
    digit1 = str(11 - remainder1) if remainder1 > 1 else '0'

    total2 = sum([int(a) * b for a, b in zip(cnpj + digit1, weight2)])
    remainder2 = total2 % 11
    digit2 = str(11 - remainder2) if remainder2 > 1 else '0'

    return cnpj_digit == digit1 + digit2