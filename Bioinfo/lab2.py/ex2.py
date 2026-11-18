import matplotlib.pyplot as plt
import math
import random


def calculate_temperature(c, g, a, t):
    length = c + g + a + t
    gc_percentage = (c + g) / length * 100

    return (
        81.5
        + 16.6 * math.log10(0.05)
        + 0.41 * gc_percentage
        - 600 / length
    )


gc_values = []
temperatures = []

for i in range(9):
    c = random.randint(1, 15)
    g = random.randint(0, 10)
    a = random.randint(1, 10)
    t = random.randint(1, 10)

    gc_values.append((c + g) / 2)
    temperatures.append(calculate_temperature(c, g, a, t))

plt.plot(gc_values, temperatures, marker="o")
plt.xlabel("Average G and C count")
plt.ylabel("Melting temperature")
plt.title("DNA Melting Temperature")
plt.show()