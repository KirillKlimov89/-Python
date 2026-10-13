import pytest

from string_utils import StringUtils


@pytest.fixture
def utils():
    return StringUtils()


def test_capitalize_positive(utils):
    assert utils.capitalize("skypro") == "Skypro"


def test_capitalize_empty(utils):
    assert utils.capitalize("") == ""


def test_capitalize_space(utils):
    assert utils.capitalize(" ") == " "


def test_capitalize_none(utils):
    with pytest.raises(AttributeError):
        utils.capitalize(None)


def test_trim_positive(utils):
    assert utils.trim("   skypro") == "skypro"


def test_trim_no_spaces(utils):
    assert utils.trim("Тест") == "Тест"


def test_trim_only_spaces(utils):
    assert utils.trim("   ") == ""


def test_trim_none(utils):
    with pytest.raises(AttributeError):
        utils.trim(None)


def test_contains_true(utils):
    assert utils.contains("SkyPro", "S") is True


def test_contains_false(utils):
    assert utils.contains("SkyPro", "U") is False


def test_contains_digit(utils):
    assert utils.contains("123", "2") is True


def test_contains_empty(utils):
    assert utils.contains("", "a") is False


def test_delete_symbol_single(utils):
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"


def test_delete_symbol_substring(utils):
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"


def test_delete_symbol_not_found(utils):
    assert utils.delete_symbol("SkyPro", "Z") == "SkyPro"


def test_delete_symbol_spaces(utils):
    assert utils.delete_symbol("04 апреля 2023", " ") == "04апреля2023"
