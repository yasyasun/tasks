import json


def load_json(file_path):
    """Функуия декодирования JSON-файлов."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def fill_values(report_structure, values):
    """
    Функция  рекурсивно проходит по структуре репорта,
    которая скопирована из тестов, и заполняет значения из values.
    """
    if isinstance(report_structure, dict):
        for key_report, val_report in report_structure.items():
            if key_report == 'id' and isinstance(values, dict):
                for key_values, val_values in values.items():
                    if key_values == 'id' and val_values == val_report:
                        report_structure['value'] = values['value']
                        break
                    elif isinstance(val_values, list):
                        for item in val_values:
                            fill_values(report_structure, item)
            elif isinstance(val_report, list):
                for item in val_report:
                    fill_values(item, values)


def create_report(tests, values):
    """
    Функция создает копию структуры тестов и вызывает функцию заполнения отчета.
    """
    report = tests.copy()
    fill_values(report, values)
    return report


def main(values_file, tests_file, report_file):
    """
    Функция, которая управляет загрузкой данных и созданием отчета.
    """
    values = load_json(values_file)
    tests_structure = load_json(tests_file)
    report = create_report(tests_structure, values)

    with open(report_file, 'w', encoding='utf-8') as file:
        json.dump(report, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main('values.json', 'tests.json', 'report.json')
