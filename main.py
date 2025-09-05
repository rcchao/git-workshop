from calculator.add import add
from calculator.subtract import subtract
from calculator.multiply import multiply
from calculator.divide import divide
from utils.format import pretty_print

def run_demo():
    x, y = 10, 5
    results = {
        "add": add(x, y),
        "subtract": subtract(x, y),
        "multiply": multiply(x, y),
        "divide": divide(x, y),
    }
    pretty_print(results)

if __name__ == "__main__":
    run_demo()
