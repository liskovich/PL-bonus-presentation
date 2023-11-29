# the `calculate_area_safe` without any validation for width and height
def calculate_area(width, height):
  area = width * height
  return area

# unsafe usage without validation
user_width = 5
user_height = 'b'

result = calculate_area(user_width, user_height)
print(f"The area of the rectangle is: {result}")

# output:
# The area of the rectangle is: bbbbb