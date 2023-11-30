from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv

from llama_index.program import OpenAIPydanticProgram
from llama_index.extractors import PydanticProgramExtractor
from llama_index.llms import OpenAI

load_dotenv()

# create data models in which we would like to receive dishes
class Dish(BaseModel):
  """Data model for a dish."""
  name: str
  ingredients: List[str]
  price: float
  is_vegetarian: bool = False
  calories: int

class Menu(BaseModel):
  """Data model for a menu."""
  restaurant_name: str
  dishes: List[Dish]

# create the call to LLM
prompt_template_str = """\
Generate an example menu, with restaurant name and a list of 3 dishes. \
The dishes should be from the following cuisine: {cuisine_name}.\
"""
program = OpenAIPydanticProgram.from_defaults(
  output_cls=Menu,
  llm=OpenAI(model="gpt-3.5-turbo"),
  prompt_template_str=prompt_template_str,
  verbose=True,
)

output = program(cuisine_name="Mexican")
print(output)

# output:
# Function call: Menu with args: {
#   "restaurant_name": "Mexican Delight",
#   "dishes": [
#     {
#       "name": "Taco",
#       "ingredients": ["tortilla", "meat", "lettuce", "cheese", "salsa"],
#       "price": 8.99,
#       "is_vegetarian": false,
#       "calories": 350
#     },
#     {
#       "name": "Burrito",
#       "ingredients": ["tortilla", "rice", "beans", "meat", "cheese", "salsa"],
#       "price": 10.99,
#       "is_vegetarian": false,
#       "calories": 500
#     },
#     {
#       "name": "Enchiladas",
#       "ingredients": ["tortilla", "chicken", "cheese", "salsa", "sour cream"],
#       "price": 12.99,
#       "is_vegetarian": false,
#       "calories": 450
#     }
#   ]
# }