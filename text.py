import re


def multiply(data: str) -> int:
    pattern = r"*mul\(\d+,\d+\)"  # Literal "mul"  then ( then a number Literal "," then a number then )
    flags = re.MULTILINE
    matches = re.findall(pattern, data, flags)
    numbers = [item.strip("mul(").strip(")").split(",") for item in matches]

    sum = 0
    for x in numbers:
        sum += int(x[0]) * int(x[1])

    return sum


with open("input.txt") as f:
    # Regex pattern
    pattern = r"don't\(\).*?(?=do\(\))"

    # Replace the matched pattern with an empty string
    result = re.sub(
        pattern,
        "",
        f.read(),
        flags=re.DOTALL,
    )
    print(multiply(result))