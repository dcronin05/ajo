equations = []


def parse_operators(function):
    eq_index = 0
    for digit in function[:]:
        try:
            int(digit)
            equations[eq_index] += digit
        except IndexError as e:
            equations.append(digit)
        except ValueError as e:
            eq_index += 2
            equations.append(digit)

    return perform_multiplication(equations)


def perform_multiplication(parts):

    for num in range(len(parts)):
        if parts[num] == '*':
            parts[num] = int(parts[num - 1]) * int(parts[num + 1])
            del(parts[num - 1])
            del(parts[num])
            break
    if '*' in parts:
        perform_multiplication(parts)

    return parts
