import logging


class Calculator:

    def __init__(self):
        self.current_number = 0

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        logger_handler = logging.FileHandler('logging.log')
        logger_handler.setLevel(logging.INFO)

        logger_formatter = logging.Formatter(
            '%(name)s - %(levelname)s - %(message)s')

        logger_handler.setFormatter(logger_formatter)

        self.logger.addHandler(logger_handler)
        self.logger.info('Настройка логгирования окончена!')

    def start(self) -> None:
        """This method start calculator"""
        signs = ["+", "-", "/", "*"]

        while True:
            a, b = map(
                int,
                input("Please enter two number format (a b): ").split(" "))
            s: str = input(
                "Please enter the action sign (action signs +, -, /, *): ")
            result: float = 0
            if s in signs:
                try:
                    match s:
                        case "+":
                            result = self.add(a, b)
                        case "-":
                            result = self.subtract(a, b)
                        case "/":
                            result = self.divided(a, b)
                        case "*":
                            result = self.multiply(a, b)

                    print(f"result = {result}")
                    break
                except ZeroDivisionError:
                    self.logger.error(
                        f"You can't divide by zero! params a = {a}, b = {b}, sing = {s}"
                    )
                    print("You can't divide by zero!")
            else:
                self.logger.error(
                    f"Please enter correct sign! params a = {a}, b = {b}, sing = {s}"
                )
                print("Please enter correct sign!")

    def add(self, a: float, b: float) -> float:
        """This method adding two numbers (a and b)"""
        self.logger.info(f'{a} Add {b}')
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """This method subtract two numbers (a and b)"""
        self.logger.info(f'{a} substract {b}')
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """This method multiply two numbers (a and b)"""
        self.logger.info(f'{a} multiply {b}')
        return a * b

    def divided(self, a: float, b: float) -> float:
        """This method divided a in b if b not equals zero"""
        self.logger.info(f'{a} divided {b}')
        return a / b


def main() -> None:
    """This main method, dot run"""
    calculate = Calculator()
    calculate.start()


if __name__ == "__main__":
    main()
