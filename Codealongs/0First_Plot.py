import matplotlib.pyplot as plt

numbers = list(range(10))

squares = [number**2 for number in numbers]

print(squares)
print(numbers)

plt.plot(numbers, squares)
plt.title("x^2 for positive integers 0-9")
plt.xlabel("x")
plt.ylabel("y")
plt.show()