import re
our_text = input("f: ")
def generator_numbers(text: str):
    pattern = re.compile(r'\b\d+(\.\d+)?\b')
    matches = pattern.finditer(text)
    for match in matches:
        number = float(match.group())
        yield number

def sum_profit(text: str):
    total_sum = sum(generator_numbers(text))
    print("Загальний прибуток:", total_sum)


sum_profit(our_text)