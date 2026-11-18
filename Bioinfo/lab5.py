import random
import math
import matplotlib.pyplot as plt
from pathlib import Path

genome = Path(__file__).with_name(
    "rhinovirus_b14.txt"
).read_text().strip()

fragments = []

for i in range(10):
    start = random.randint(0, 3000)
    length = random.randint(100, 3000)

    fragment = genome[start:start + length]
    fragments.append(fragment)

    print("Fragment", i + 1, "length:", len(fragment))


def calculate_position(fragment, a=20, min_h=4):
    return len(fragment) * a / math.log(min_h)


for fragment in fragments:
    position = calculate_position(fragment)

    plt.axhline(
        y=position,
        color="blue",
        linewidth=2
    )

plt.title("DNA fragment distribution")
plt.ylabel("fragment position")
plt.show()