import matplotlib.pyplot as plt


def nucleotide_frequency(sequence):
    bases = ["C", "G", "A", "T"]
    frequencies = [sequence.count(base) for base in bases]

    plt.bar(bases, frequencies, color="skyblue")
    plt.xlabel("Nucleotides")
    plt.ylabel("Frequency")
    plt.title("DNA Nucleotide Frequency")
    plt.show()


while True:
    dna = input("Enter DNA sequence: ").upper()
    nucleotide_frequency(dna)