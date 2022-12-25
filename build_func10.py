def main(x, y):
    """Integer type variables 'x' and 'y' are given. Return the value of the expression in README.md file.
    https://github.com/codeschool43/Build_in_function_homework#build_func10

    Args:
        x (int): integer
        y (int): integer
        
    Returns:
        int: the value of the expression
    """
    answer = 3*pow(y, 1/2)+pow(x, 2/3)
    answer = round(answer, 2)
    return answer
x = 2
y = 4
print(main(x, y))