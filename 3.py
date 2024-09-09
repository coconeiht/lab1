class Calculator:
    def add(*args):
        return sum(args)

    def multiply(*args):
        result = 1
        for num in args:
            result *= num
        return result

    def divide(*args):
        result = args[0]
        for num in args[1:]:
            if num == 0:
                return "Cannot divide by zero"
            result /= num
        return result

    def subtract(*args):
        result = args[0]
        for num in args[1:]:
            result -= num
        return result
