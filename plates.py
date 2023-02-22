import re

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    if not s[:2].isalpha():
        return False
    if s.isalpha():
        return True

    pattern = r'^[A-Z]{1,4}[1-9][0-9]{0,2}$'
    if re.match(pattern, s):
        return True
    else:
        return False

main()
