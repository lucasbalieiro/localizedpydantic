from pytest import mark, raises
from localizedpydantic.models.brazil import CPF, CNPJ, CEP



@mark.parametrize(
    "cpf, expected_result",
    [
        ("12345678909", "123.456.789-09"),
        ("123.456.789-09", "123.456.789-09"),
        ("123.456.78909", "123.456.789-09"),
        ("123456789-09", "123.456.789-09"),
        ("123 456 789 09", "123.456.789-09"),
        ("123.456.789 09", "123.456.789-09"),
        ("123456789-10", ValueError),
        ("123 456 789 10", ValueError),
        ("123.456.789-10", ValueError),
        ("123.456.789 10", ValueError),
        ("12345678910", ValueError),
    ],
)
def test_cpf(cpf, expected_result):
    if isinstance(expected_result, str):
        cpf_model = CPF(cpf=cpf)
        assert cpf_model.cpf == expected_result
    else:
        with raises(expected_result):
            CPF(cpf=cpf)

#test for cnpj

test_cases = [
    ("11222333000181", "11.222.333/0001-81"),
    ("22.334.558/0001-76", None),
    ("00000000000000", None),
    ("99999999999999", None),
    ("11222333000182", None),
    ("1122233300018", None),
    ("112223330001811", None),
    ("1122233300018a", None),
    ("11.222.333/0001-81 ", "11.222.333/0001-81"),
    ("11.222.333/000181", "11.222.333/0001-81"),
]

@mark.parametrize("cnpj, expected", test_cases)
def test_cnpj(cnpj, expected):
    if expected:
        cnpj_obj = CNPJ(cnpj=cnpj)
        assert cnpj_obj.cnpj == expected
    else:
        with raises(ValueError):
            CNPJ(cnpj=cnpj)


#test for cep

test_cases = [
    ("12345678", "12345-678"),
    ("12345-678", "12345-678"),
    ("12.345-678", "12345-678"),
    ("123456789", None),
    ("1234-5678", "12345-678"),
    ("1234567a", None),
    ("123456", None),
    ("12.345.678 ", "12345-678"),
    ("12345 678", "12345-678"),
    (" 12345-678 ", "12345-678"),
]

@mark.parametrize("cep, expected", test_cases)
def test_cep(cep, expected):
    if expected:
        cep_obj = CEP(cep=cep)
        assert cep_obj.cep == expected
    else:
        with raises(ValueError):
            CEP(cep=cep)
