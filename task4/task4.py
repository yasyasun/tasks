import sys


def search_min_moves(nums):
    """
    Функция вычисляет минимальное количество ходов,
    требуемых для приведения всех элементов к одному числу.
    """
    nums.sort()
    median = nums[len(nums) // 2]
    moves = sum(abs(num - median) for num in nums)
    return moves


def main(file_path):
    """
    Функция, которая читает данные из файла и вызывает функцию поиска
    """
    list_numbers = []

    with open(file_path, 'r') as file:
        for number in file:
            list_numbers.append(int(number))

    result = search_min_moves(list_numbers)
    print(result)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Необходимо ввести: python task4.py numbers.txt")
        sys.exit(1)

    numbers_file = sys.argv[1]

    main(numbers_file)
