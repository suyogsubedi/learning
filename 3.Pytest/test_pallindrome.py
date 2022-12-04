import pytest
from pallindrome import ultoSultoUstai
@pytest.mark.parametrize("palindrome", [
    "",
    "a",
    "Bob",
    "Never odd or even",
    "Do geese see God?",
])
# yo function lai value chai mathi ko parametrize bata aaucha, tsko first parameter ko naam palindrome cha tei bhayera tala function call ma tei use gareko
def test_is_palindrome(palindrome):
    print("inside test")
    assert ultoSultoUstai(palindrome)
@pytest.mark.parametrize("non_palindrome", [
    "abc",
    "abab",
])
def test_is_not_palindrome(non_palindrome):
    assert not ultoSultoUstai(non_palindrome)

# parametrize use garera , expected result ko value ni afaile manually dine bhaye chai tala ko jsto garne
@pytest.mark.parametrize("maybe_palindrome, expected_result", [
    ("", True),
    ("a", True),
    ("Bob", True),
    ("Never odd or even", True),
    ("Do geese see God?", True),
    ("abc", False),
    ("abab", False),
])
def test_is_palindrome(maybe_palindrome, expected_result):
    assert ultoSultoUstai(maybe_palindrome) == expected_result