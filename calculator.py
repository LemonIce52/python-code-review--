class Calculator:
    def ADD(self, a: float, b: float) -> float:
        """This method adding two numbers (a and b)"""
        return a + b

    def SUBSTRACT(self, a: float, b: float) -> float:
        """This method subtract two numbers (a and b)"""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """This method multiply two numbers (a and b)"""
        return a * b

    def divided(self, a: float, b: float) -> float:
        """This method divided a in b if b not equals zero"""
        return a / b


def main() -> None:
    """This main method, dot run"""
    signs = ["+", "-", "/", "*"]
    calculate = Calculator()

    while True:
        a, b = input("Please enter two number format (a b): ").split(" ")
        s = input("Please enter the action sign (action signs +, -, /, *): ")
        result: int = 0
        if s in signs:
            match s:
                case "+": result = calculate.ADD(a, b)
                case "-": result = calculate.SUBSTRACT(a, b)
                case "/": result = calculate.divided(a, b)
                case "*": result = calculate.multiply(a, b)

            print(f"result = {result}")
        else:
            print("Please enter correct sign!")

if __name__ == "__main__":
    main()