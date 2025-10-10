class Calculator:

    def add(self, a: float, b: float) -> float:
        """This method adding two numbers (a and b)"""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """This method subtract two numbers (a and b)"""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """This method multiply two numbers (a and b)"""
        return a * b

    def divided(self, a: float, b: float) -> float:
        """This method divided a in b if b not equals zero"""
        if b == 0:
            return 0
        else:
            return a / b


def main() -> None:
    """This main method, dot run"""
    signs = ["+", "-", "/", "*"]
    calculate = Calculator()

    while True:
        a, b = map(int, input("Please enter two number format (a b): ").split(" "))
        s: str = input("Please enter the action sign (action signs +, -, /, *): ")
        result: float = 0
        if s in signs:
            match s:
                case "+": result = calculate.add(a, b)
                case "-": result = calculate.subtract(a, b)
                case "/": result = calculate.divided(a, b)
                case "*": result = calculate.multiply(a, b)

            print(f"result = {result}")
            break
        else:
            print("Please enter correct sign!")

if __name__ == "__main__":
    main()