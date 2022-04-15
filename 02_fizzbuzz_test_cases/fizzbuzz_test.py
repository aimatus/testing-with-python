from fizzbuzz import play


def test_returns_same_number():
  number = 1

  result = play(number)

  assert result == number

def test_returns_fizz_when_multiple_of_3():
  pass

def test_returns_buzz_when_multiple_of_5():
  pass

def test_returns_fizzbuzz_when_multiple_of_3_and_5():
  pass

def test_returns_error_message_when_number_more_than_100():
  pass

def test_throws_exception_when_playing_with_negative_numbers():
  pass