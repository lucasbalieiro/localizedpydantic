# LocalizedPydantic - UNDER CONSTRUCTION

LocalizedPydantic is a Python library for validating localized data, such as Brazilian CEPs and CPFs. The library is designed to be extensible, so that other developers can contribute validation rules for their own countries.

## Installation

Install with pip:

```bash 
    pip install localizedpydantic
```

## Usage

Here's an example of how to use LocalizedPydantic to validate a Brazilian CEP:

```python
from localizedpydantic.validators.brazil import CPF
from pydantic import ValidationError

try:
    cpf = CPF(cpf='123.456.789-00')
    print(cpf.cpf)  # '123.456.789-00'
except ValidationError as e:
    print(e)

try:
    cpf = CPF(cpf='12345678900')
    print(cpf.cpf)  # raises ValidationError
except ValidationError as e:
    print(e)

```

## Contributing
Contributions are welcome! To contribute, please submit a pull request.

## License
LocalizedPydantic is licensed under the MIT license