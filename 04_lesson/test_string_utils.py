import pytest
from string_utils import StringUtils


@pytest.mark.parametrize(
    "input_data,expected_output",
    [
        ("skypro", "Skypro"),          # Базовый случай
        ("", ""),                      # Пустой ввод
        ("small", "Small"),            # Маленькая строка
        ("123abc", "123abc"),          # Числовые значения
        ("@skypRo", "@SkypRo"),        # Спецсимволы
    ],
)
def test_capitalize(input_data, expected_output):
    utils = StringUtils()
    output = utils.capitalize(input_data)
    assert output == expected_output, f"Ошибка при обработке {input_data}"


@pytest.mark.parametrize(
    "input_data,expected_output",
    [
        ("   skypro", "skypro"),       # Основной сценарий
        ("", ""),                      # Пустая строка
        ("  small", "small"),          # Несколько пробелов
        ("   SkyPro  ", "SkyPro  "),   # Сохранение пробелов справа
        ("  @skypRo", "@skypRo"),      # Символы кроме пробелов
    ],
)
def test_trim(input_data, expected_output):
    utils = StringUtils()
    output = utils.trim(input_data)
    assert output == expected_output, f"Ошибка при обработке {input_data}"


@pytest.mark.parametrize(
    "input_data,symbol,expected_output",
    [
        ("SkyPro", "S", True),         # Обычный случай
        ("SkyPro", "Z", False),        # Отсутствующий символ
        ("SkyPro", "s", False),        # Учет регистров
        ("", "", False),               # Пустые аргументы
        ("SkyPro", "#", False),        # Спецсимволы
    ],
)
def test_contains(input_data, symbol, expected_output):
    utils = StringUtils()
    output = utils.contains(input_data, symbol)
    assert output == (
        expected_output,
        f"Ошибка при проверке наличия символа '{symbol}' в '{input_data}'")


@pytest.mark.parametrize(
    "input_data,symbol,expected_output",
    [
        ("SkyPro", "P", "Skyro"),      # Основная проверка
        ("SkyPro", "o", "SkyPr"),      # Несколько символов
        ("SkyPro", "Pro", "Sky"),      # Удаление подстроки
        ("SkyPro", "X", "SkyPro"),     # Символ отсутствует
        ("SkyPro", "p", "SkyPro"),     # Чувствительность к регистру
    ],
)
def test_delete_symbol(input_data, symbol, expected_output):
    utils = StringUtils()
    output = utils.delete_symbol(input_data, symbol)
    assert output == (
        expected_output,
        f"Ошибка при удалении символа '{symbol}' из '{input_data}'")
