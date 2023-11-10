import random


def create_rand_int(min_value, max_value):
    """
    Function:
    It creates an random integer inbetween 
    the range of two Parameter(min_value, max_value).
    
    Parameter:
    min_value(int): Minimum integer value
    max_value(int): Maximum integer value    
    
    Return:
    Returns one integer number
    
    """
    return random.randint(min_value, max_value)


def create_rand_operator():
    """
    Function:
    It creates an random operator (+, -, *)
    
    Paramter:
    --non--
    
    Return:
    Returns one operator 
    """
    return random.choice(['+', '-', '*'])


def cal_result_numbers(number1, number2, operator):
    """
    Function:
    It calculates the result between two numbers(number1, number2)
    and an operator (+, -, *) 
    
    Paramter:
    number1 (int): First number
    number2 (int): second number
    operator(str): Operator for the calcualtion
    
    Return:
    Returns the result and the calculation as a sting

    """
    calculation = f"{number1} {operator} {number2}"
    
    if operator == '+': 
        result = number1 + number2
        
    elif operator == '-': 
        result = number1 - number2
        
    else: 
        result = number1 * number2
        
    return calculation, result


def math_quiz():
    """
    Function: 
    It connectes three function create_rand_int, 
    create_rand_operator, cal_result_numbers. 
    
    Return: 
    The quiz gives out three random calculation and ask for the answer.
    It returns the reached score after finishing   
    """
    start_score = 0
    number_question = 3 #how many calculation are required

    print("Welcome to the Math Quiz Game!")
    print("""You will be presented with math problems, and you need to provide
    the correct answers.""")

    for _ in range(number_question):
        num1 = create_rand_int(1, 10); 
        num2 = create_rand_int(1, 5); 
        rand_op = create_rand_operator()
        problem, answer = cal_result_numbers(num1, num2, rand_op)
        
        print(f"\nQuestion: {problem}")
        
      
        try: 
            useranswer = input("Your answer: ")
            value_useranswer = int(useranswer)  #Try to convert the useranswer into integer number
            
        except ValueError:
            print("please insert integer number") # Error if the input isnt a number
        

        if value_useranswer == answer:
            print("Correct! You earned a point.")
            start_score += +1
            
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {start_score}/{number_question}") #shows the Score at the end of the game

if __name__ == "__main__":
    math_quiz()
