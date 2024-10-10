import sys


def circular_array_path(size_array, length_interval):
    """Функция выводит путь по круговому массиву."""
    received_path = []
    current_position = 1
    while current_position not in received_path:
        received_path.append(current_position)
        current_position = (current_position + length_interval - 1) % size_array
        if current_position == 0:
            current_position = size_array
    return received_path


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование: python task1.py n m")
        sys.exit(1)

    n = int(sys.argv[1])
    m = int(sys.argv[2])

    path = circular_array_path(n, m)
    for i in path:
        print(i, end='')
