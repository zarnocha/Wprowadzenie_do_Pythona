import sys


def stretch_number(number: str):
    result_sentence = ""

    for index, digit in enumerate(number):
        power_of_digit = 10 ** (len(number) - index - 1)
        result_sentence += f"{power_of_digit} * {digit}"
        
        if index + 1 != len(number):
            result_sentence += " + "
    
    return result_sentence
    
    
def main():
    sys.stdout.write("Wprowadź liczbę całkowitą: ")
    sys.stdout.flush()
    
    number = sys.stdin.readline().strip()
    stretched_number = stretch_number(number)
    
    sys.stdout.write(f"Podaną liczbę ({number}) można zapisać jako: {stretched_number}")
    sys.stdout.flush()


if __name__ == "__main__":
    main()