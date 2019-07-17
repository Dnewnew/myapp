from dice import Dice
import pygal

dice_1 = Dice()
dice_2 = Dice()

results = []
for roll_num in range(10000):
    result = dice_1.roll() * dice_2.roll()
    results.append(result)

frequencies = []
multiplications = []
for i in range(1,7):
    for j in range(1,7):
        multiplication = i * j
        multiplications.append(multiplication)
x = sorted(set(multiplications))
frequencies = [results.count(value) for value in x]

hist = pygal.Bar()
hist.title = "Rolling two D6 dice 10000 times"
hist.x_labels = x
hist.x_title = "Results"
hist.y_title = "Frequency of Results"
hist.add('D6*D6', frequencies)
hist.render_to_file('dice_visual_multiplication.svg')