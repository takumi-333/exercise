from enum import Enum

class Gender(Enum):
    Male = 1
    Female = 2

def sum(a, b)->int:
    return a+b


def main():
    gender = Gender.Male
    if gender == Gender.Male:
        print("あなたは男性です")
    else:
        print("あなたは女性です")

if __name__ == "__main__":
    main()