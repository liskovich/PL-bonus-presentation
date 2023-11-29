from pydantic import BaseModel, ValidationError

# here we define our input format 
# (both width and height are required and are expected to be ints)
class RectangleInput(BaseModel):
  width: int
  height: int

# updated `calculate_area_safe`
def calculate_area_safe(rectangle: RectangleInput):
  area = rectangle.width * rectangle.height
  return area

try:
  # safe usage with Pydantic validation
  user_width = 5
  user_height = 'b'

  rectangle_data = RectangleInput(width=user_width, height=user_height)
  result = calculate_area_safe(rectangle_data)
  print(f"The area of the rectangle is: {result}")

except ValidationError as e:
  print(f"Input validation failed: {e}")

# output:
# Input validation failed: 1 validation error for RectangleInput
# height
#   value is not a valid integer (type=type_error.integer)