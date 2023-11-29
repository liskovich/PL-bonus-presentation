# from: https://docs.pydantic.dev/latest/#pydantic-examples

from datetime import datetime
from pydantic import BaseModel, PositiveInt, ValidationError

# define a class for User
# 1. you can provide some default values (e.g. 'John Doe')
# 2. you can allow for several types of data, Pydantic will try to process them (e.g. signup_ts)
class User(BaseModel):
  id: int  
  name: str = 'John Doe'  
  signup_ts: datetime | None  
  tastes: dict[str, PositiveInt]  

external_data = {
  'id': 123,
  'signup_ts': '2023-11-30 12:22',    # this is a string formatted date (converted automatically)
  'tastes': {
      'wine': 9,                      # normal int
      b'cheese': 7,                   # byte (converted automatically)
      'cabbage': '1',                 # string representation of an int (converted automatically)
  },
}

try:
  # here we enable strict validation
  user = User.model_validate(external_data, strict=True)
  print(user.model_dump())
except ValidationError as e:
  print(f"Input validation failed: {e}")

# output:
# Input validation failed: 3 validation errors for User
# signup_ts
#   Input should be a valid datetime [type=datetime_type, input_value='2023-11-30 12:22', input_type=str]
#     For further information visit https://errors.pydantic.dev/2.5/v/datetime_type
# tastes.b'cheese'.[key]
#   Input should be a valid string [type=string_type, input_value=b'cheese', input_type=bytes]
#     For further information visit https://errors.pydantic.dev/2.5/v/string_type
# tastes.cabbage
#   Input should be a valid integer [type=int_type, input_value='1', input_type=str]
#     For further information visit https://errors.pydantic.dev/2.5/v/int_type