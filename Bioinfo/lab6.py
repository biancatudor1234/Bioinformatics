import random

def random_dna(n):
    return "".join(random.choices("ATGC", k=n))

def reverse_complement(dna):
    pairs = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join(pairs[x] for x in dna[::-1])

def create_element():
    left = random_dna(12)
    middle = random_dna(15)
    right = reverse_complement(left)

    return left + middle + right
dna = ""
positions = []

number = random.randint(3, 4)

for i in range(number):
    dna += random_dna(random.randint(15, 25))

    start = len(dna)
    dna += create_element()
    end = len(dna) - 1

    positions.append((start, end))

length = random.randint(max(200, len(dna)), 400)
dna += random_dna(length - len(dna))

print("DNA sequence:", dna)
print("Sequence length:", len(dna))

print("\nInserted elements:")

for start, end in positions:
    print("Start:", start, "End:", end)

print("\nDetected elements:")

for i in range(len(dna) - 38):
    left = dna[i:i + 12]
    right = dna[i + 27:i + 39]

    if reverse_complement(left) == right:
        print("Start:", i, "End:", i + 38)