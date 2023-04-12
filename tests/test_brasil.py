from localizedpydantic.models.brazil import CPF
import pytest

def test_valid_cpf():
    cpf = CPF(cpf="12345678909")
    assert cpf.cpf == "123.456.789-09"

def test_invalid_cpf():
    with pytest.raises(ValueError):
        CPF(cpf="12345678910")