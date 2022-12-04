def ultoSultoUstai(word):
    # removing spaces and making them small letters
    new_word= ''.join(e for e in word if e.isalnum()).lower()
    return new_word == new_word[::-1]

print(ultoSultoUstai("Do geese see God?"))