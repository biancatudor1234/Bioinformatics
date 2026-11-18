import matplotlib.pyplot as plt
import math
from pathlib import Path


enzymes = {
    "EcoRI": "gaattc",
    "BamHI": "ggatcc",
    "HindIII": "aagctt"
}

ladder = [10000, 8000, 6000, 5000, 4000, 3000,
          2000, 1500, 1000, 500, 250, 100]


def cut_dna(dna, enzyme):
    cuts = [0]

    for i in range(len(dna) - len(enzyme) + 1):
        if dna[i:i + len(enzyme)] == enzyme:
            cuts.append(i + 1)

    cuts.append(len(dna))

    fragments = []

    for i in range(len(cuts) - 1):
        fragments.append(cuts[i + 1] - cuts[i])

    return fragments


def draw_gel(dna, name):
    plt.figure(figsize=(8, 7))
    plt.gca().set_facecolor("black")

    lanes = {"Ladder": ladder}

    for enzyme in enzymes:
        fragments = cut_dna(dna, enzymes[enzyme])
        lanes[enzyme] = fragments
        print(name, enzyme, fragments)

    for i, lane in enumerate(lanes):
        for size in lanes[lane]:
            y = math.log10(size)

            plt.hlines(y, i - 0.3, i + 0.3,
                       colors="white", linewidth=4)

            plt.text(i + 0.35, y, str(size),
                     color="cyan", fontsize=8)

    plt.xticks(range(len(lanes)), list(lanes.keys()))
    plt.yticks([])
    plt.xlim(-0.6, 4)
    plt.title("Gel Electrophoresis - " + name)
    plt.show()


folder = Path(__file__).parent

dna1 = (folder / "rhinovirus_b14.txt").read_text().strip().lower()
dna2 = (folder / "rhinovirus_b3.txt").read_text().strip().lower()

draw_gel(dna1, "Rhinovirus B14")
draw_gel(dna2, "Rhinovirus B3")