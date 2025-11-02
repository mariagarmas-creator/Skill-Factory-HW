import numpy as np
def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    # The random number to guess
    predict = np.random.randint(1, 100)

    # Range boundaries
    first = 1
    last = 100
    count = 0


    while True:
        # lets always make itguess as half of an available range.
        guess = (first + last) // 2
        count += 1
        # print(f"Try {count}: Guessing {guess}")

        if guess == predict:
            # print(f"Correct! The number was {predict}. Found in {count} tries.")
            break

        # if our predict is bigger, than half of our range,
        #  then our new range is half+1 until last number
        elif guess < predict:
            first = guess + 1
        else:
            last = guess - 1

        if count > 20:
            print("Something went wrong — took too many tries!")
            break

    return count

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
    
print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)