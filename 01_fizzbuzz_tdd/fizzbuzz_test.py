from fizzbuzz import play


def test_returns_same_number():
  number = 1

  result = play(number)

  assert result == number
