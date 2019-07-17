import matplotlib.pyplot as plt

# input_values = [1,2,3,4,5]
# squares = [1, 4, 9, 16, 25]
# plt.plot(input_values, squares, linewidth=5)
# plt.title('Square Numbers', fontsize=24)
# plt.xlabel('Value', fontsize=14)
# plt.ylabel('Square of Value', fontsize=14)
# plt.tick_params(axis='both', labelsize=14)
# plt.show()

# 15-1
x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]
#plt.scatter(x_values, y_values, c=(0, 0, 1), edgecolors='none', s=40)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Set3, edgecolor='none', s=40)
plt.axis([0, 5100, 0, 130000000000])
plt.show()