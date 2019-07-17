from dice import Dice
import pygal

dice_1 = Dice()
dice_2 = Dice()
dice_3 = Dice()

results = []
for roll_num in range(10000):
    result = dice_1.roll() + dice_2.roll() + dice_3.roll()
    results.append(result)

#frequencies = []
max_result = dice_1.num_sides + dice_2.num_sides + dice_3.num_sides
frequencies = [results.count(value) for value in range(3, max_result+1)]
# for value in range(2, max_result+1):
#     frequency = results.count(value)
#     frequencies.append(frequency)

hist = pygal.Bar()
hist.title = "Rolling three D6 dice 10000 times"
hist.x_labels = [x for x in range(3, max_result+1)]
#hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Results"
hist.y_title = "Frequency of Results"
hist.add('D6+D6+D6', frequencies)
#hist.render()
hist.render_to_file('dice_visual.svg')
