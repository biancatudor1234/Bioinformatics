import matplotlib.pyplot as plt


def melting_temperature(sequence):
    bases = ["C", "G", "A", "T"]
    counts = [sequence.count(base) for base in bases]

    c, g, a, t = counts
    temperature = 4 * (g + c) + 2 * (a + t)

    plt.bar(bases, counts, color="lightgreen")
    plt.xlabel("Nucleotides")
    plt.ylabel("Frequency")
    plt.title("DNA Base Distribution")
    plt.show()

    return temperature


while True:
    dna = input("Enter DNA sequence: ").upper()
    result = melting_temperature(dna)
    print("Melting temperature:", result, "°C")