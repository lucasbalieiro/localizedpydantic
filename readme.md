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
from localizedpydantic import ptbr

class Address(ptbr.Address):
    cep: str

address_data = {"cep": "01001-000"}

address = Address(**address_data)
```

## Contributing
Contributions are welcome! To contribute, please submit a pull request.

## License
LocalizedPydantic is licensed under the MIT license