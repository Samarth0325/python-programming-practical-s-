def is_palindrum(s):
    if s == s[::-1]:
        print("Is palindrum")
    else:
        print("Is not palindrum")
is_palindrum("madam")