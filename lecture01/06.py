"""
6. Спортсмен занимается ежедневными пробежками. В первый день его
результат составил a километров. Каждый день спортсмен увеличивал
результат на 10 % относительно предыдущего. Требуется определить номер
дня, на который общий результат спортсмена составить не менее b
километров. Программа должна принимать значения параметров a и b и
выводить одно натуральное число — номер дня.
"""

while True:
    try:
        distance = float(input("Please enter a distance of the first day: "))
        desired_distance = float(input("Please enter a desired distance: "))
        break
    except:
        print("Please user only digits. Float is possible.")
        continue
day = 1
while desired_distance >= distance:
    day += 1
    distance *= 1.1
print(f"You wanted to run {desired_distance}. And now, {day}'s after you've achived the {distance:.2f} km distance")