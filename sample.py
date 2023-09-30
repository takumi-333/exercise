from enum import Enum

class Gender(Enum):
    Male = 1
    Female = 2

def sum(a, b)->int:
    return a+b

# def culCalorie(weight, height, old):
#     calorie = ((0.0481 * weight + 0.0234 * height - 0.0138 * old - 0.4235) * 1000 ) / 4186
#     return calorie

def main():
    weight = input("体重を入力してください")
    height = input("身長を入力してください")
    old = input("年齢を入力してください")

    print("身長 = " + str(height) + "cm")
    
    gender = Gender.Male
    if gender == Gender.Male:
        print("あなたは男性です")
    else:
        print("あなたは女性です")

if __name__ == "__main__":
    main()