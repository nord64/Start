import numpy as np


def game_core_v3(number):
    """ Алгоритм угадывания числа на основе бинарного поиска.
        Функция принимает загаданное число и возвращает число попыток."""

    # Создаем отсортированный список всех допустимых значений.
    # Для случая, когда список передается отдельно, необходимо его предварительно отсортировать.
    lst = [i for i in range(1, 101)]

    """ Неплохо было бы делать проверку на принадлежность загаданного числа к заданному диапазону, например:
        if number not in lst:
            return -1
    """

    count = 0
    first = 0
    last = len(lst) - 1
    while first <= last:
        middle = (first + last) // 2
        count += 1
        if lst[middle] == number:
            break
        elif lst[middle] > number:
            last = middle - 1
        else:
            first = middle + 1

    return count


def score_game(game_core):
    """ Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число """
    count_ls = []
    # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


score_game(game_core_v3)
