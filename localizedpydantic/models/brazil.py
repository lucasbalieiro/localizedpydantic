from pydantic import BaseModel, validator
from localizedpydantic.validators.brazil import validate_cpf
class CPF(BaseModel):
    cpf: str

    @validator('cpf')
    def validate_cpf(cls, v):
        if not validate_cpf(v):
            raise ValueError('Invalid CPF')
        return f'{v[:3]}.{v[3:6]}.{v[6:9]}-{v[9:]}'

