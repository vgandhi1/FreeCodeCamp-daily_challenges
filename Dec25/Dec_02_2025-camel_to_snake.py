def to_snake(camel):
    # Fix 1: Handle empty string to prevent crash
    if not camel:
        return ""
        
    # Fix 2: Lowercase the first letter to handle "PascalCase" inputs
    snake = [camel[0].lower()]
    
    # Unused variable 'split_index' removed
    
    for char in camel[1:]:
        if char.isupper():
            snake.append("_")
            snake.append(char.lower())
        else:
            snake.append(char)
            
    return "".join(snake)

# Tests
print(to_snake("helloWorld"))      # hello_world
print(to_snake("myVariableName"))  # my_variable_name
print(to_snake("PascalCase"))      # pascal_case (Fixed!)
print(to_snake(""))                # (Returns empty string instead of crashing)
