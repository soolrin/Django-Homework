# Дан список чисел. Проверь, образуют ли числа в нём зигза

sequence_1 = [1, 3, 2, 4, 3]
sequence_2 = [1, 2, 3, 4]
sequence_3 = [5, 1, 6, 2, 7]
sequence_4 = [1, 1, 3]


def zigzag_check(sequence):

    if len(sequence) < 3:
        print(f"{sequence} - Нет")
        return

    if sequence[0] == sequence[1]:
        print(f"{sequence} - Нет")
        return

    track = sequence[0] < sequence[1]  # True = UP | False = DOWN

    for i in range(1, len(sequence) - 1):
        if sequence[i] > sequence[i + 1] and track == True:
            track = False
        elif sequence[i] < sequence[i + 1] and track == False:
            track = True
        else:
            print(f"{sequence} - Нет")
            return

    print(f"{sequence} - Да")

zigzag_check(sequence_1)
zigzag_check(sequence_2)
zigzag_check(sequence_3)
zigzag_check(sequence_4)
