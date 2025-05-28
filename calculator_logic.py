import math

def safe_eval(expression):
    try:
        return eval(expression, {
            "sin": lambda x: math.sin(math.radians(x)),
            "cos": lambda x: math.cos(math.radians(x)),
            "tan": lambda x: math.tan(math.radians(x)),
            "asin": lambda x: math.degrees(math.asin(x)) if -1 <= x <= 1 else "Error",
            "acos": lambda x: math.degrees(math.acos(x)) if -1 <= x <= 1 else "Error",
            "atan": lambda x: math.degrees(math.atan(x)),
            "sqrt": lambda x: math.sqrt(x) if x >= 0 else "Error",
            "abs": abs,
            "_builtins_": None
        })
    except:
        return "Syntax Error"