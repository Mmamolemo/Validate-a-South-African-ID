from validate_id.validate_id import (
    length,
    days,
    month,
    check_sum,
    citizenship,
    digits_only,
    validate_sa_id,
)


def test_invalid_length():
    assert length("000919088") == False


def test_correct_length():
    assert length("0009190881087") == True


def test_not_only_digits():
    assert digits_only("000919088108#") == False


def test_digits_only():
    assert digits_only("0009190881087") == True


def test_invalid_day():
    assert days("0002310881087") == False


def test_days():
    assert days("0009190881087") == True


def test_incorrect_month():
    assert month("0013190881087") == False


def test_valid_month():
    assert month("0009190881087") == True


def test_false_citizenship():
    assert citizenship("0009190885087") == False


def test_true_citizenship():
    assert citizenship("0009190881087") == True


def test_invalid_control_digit():
    assert check_sum("0009190881089") == False


def test_valid_control_digit():
    assert check_sum("0009190881087") == True


def test_valid_id():
    assert validate_sa_id("0009190881087") == True


def test_invalid_id():
    assert validate_sa_id("0002310887086") == False
