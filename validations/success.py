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
  # a convenient way to pass the entire object at once
  user = User(**external_data)
  print(user.model_dump())
except ValidationError as e:
  print(f"Input validation failed: {e}")

# output:
# {
#   'id': 123, 
#   'name': 'John Doe', 
#   'signup_ts': datetime.datetime(2023, 11, 30, 12, 22), 
#   'tastes': {'wine': 9, 'cheese': 7, 'cabbage': 1}
# }