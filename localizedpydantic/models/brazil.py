import re
from pydantic import BaseModel, validator
from localizedpydantic.validators.brazil import validate_cpf, validate_cnpj, validate_cep
class CPF(BaseModel):
    cpf: str

    @validator('cpf')
    def validate_cpf(cls, v):
        v = re.sub('[^0-9]', '', v) 
        if not validate_cpf(v):
            raise ValueError('Invalid CPF')
        return f'{v[:3]}.{v[3:6]}.{v[6:9]}-{v[9:]}'

class CNPJ(BaseModel):
    cnpj: str

    @validator('cnpj')
    def validate_cnpj(cls, v):
        v = re.sub(r'\D', '', v)
        if not validate_cnpj(v):
            raise ValueError('Invalid CNPJ')
        return f'{v[:2]}.{v[2:5]}.{v[5:8]}/{v[8:12]}-{v[12:]}'
    
class CEP(BaseModel):
    cep: str

    @validator('cep')
    def validate_cep(cls, v):
        v = re.sub('[^0-9]', '', v)
        if not validate_cep(v):
            raise ValueError('Invalid CEP')
        return f'{v[:5]}-{v[5:]}'