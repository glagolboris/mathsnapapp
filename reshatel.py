from sympy import sympify, solve


def resh(eq):
    sympy_eq = sympify("Eq(" + get_true_eq(eq).replace("=", ",") + ")")
    if solve(sympy_eq):
        result = 'Результат: '
        for el in solve(sympy_eq):
            result += f'{str(el)}; '
        return result

    else:
        return 'Нет корней'


def get_true_eq(eq):
    t = eq.replace(' ', '')
    equ = list(t)

    for el in range(len(equ.copy())):
        if equ[el] == '+':
            equ[el] = ' + '

        if equ[el] == '-':
            equ[el] = ' - '

        if equ[el] == '*':
            equ[el] = ' * '

        if equ[el] == '/':
            equ[el] = ' / '

        if equ[el] == '//':
            equ[el] = ' // '

        if equ[el].isalpha():
            if el > 0:
                if equ[el - 1].isnumeric():
                    equ[el] = f'*{equ[el]}'

    return ''.join(equ)
