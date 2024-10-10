import math
import sys


def read_circle_data(file_path):
    """Читает данные окружности из файла."""
    with open(file_path, 'r') as file:
        center_x, center_y = map(float, file.readline().strip().split())
        radius = float(file.readline().strip())
    return center_x, center_y, radius


def read_points(file_path):
    """Читает координаты точек из файла."""
    points = []
    with open(file_path, 'r') as file:
        for line in file:
            x, y = map(float, line.strip().split())
            points.append((x, y))
    return points


def determine_position(point, circle):
    """Определяет положение точки относительно окружности."""
    center_x, center_y, radius = circle
    distance = math.sqrt((point[0] - center_x) ** 2 + (point[1] - center_y) ** 2)
    if distance < radius:
        return 1  # Внутри
    elif distance == radius:
        return 0  # На окружности
    else:
        return 2  # Снаружи


def main(circle_file_path, points_file_path):
    """
    Функция, которая управляет считыванием данных и вывода результата.
    """
    circle = read_circle_data(circle_file_path)
    points = read_points(points_file_path)

    results = []
    for point in points:
        position = determine_position(point, circle)
        results.append(position)

    for result in results:
        print(result)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование: python task2.py circle.txt points.txt")
        sys.exit(1)

    circle_file = sys.argv[1]
    points_file = sys.argv[2]

    main(circle_file, points_file)
