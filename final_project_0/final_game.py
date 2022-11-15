"""Игра угадай число.
Компьютер сам загадывает и угадывает число
"""

import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """  
    
    min = 1
    max = 101
    count: int = 0
    number = np.random.randint(min, max) # Загаданное число
    
    while True:
        count += 1
        predict_number = int((max+min) / 2) # Предполагаемое число
        
        if predict_number > number:
            max = predict_number
            
        elif predict_number < number:
            min = predict_number
            
        else:
            break #конец игры выход из цикла
        
    return count
   
    
def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []  # создали список для сохранения количества попыток
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    
score_game(random_predict)