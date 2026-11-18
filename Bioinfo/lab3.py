from collections import Counter
from pathlib import Path
import matplotlib.pyplot as plt
import os
from google import genai
from dotenv import load_dotenv


genetic_code = {
    "uuu": "Phe", "uuc": "Phe",
    "uua": "Leu", "uug": "Leu",
    "cuu": "Leu", "cuc": "Leu",
    "cua": "Leu", "cug": "Leu",
    "auu": "Ile", "auc": "Ile",
    "aua": "Ile", "aug": "Met",
    "guu": "Val", "guc": "Val",
    "gua": "Val", "gug": "Val",
    "ucu": "Ser", "ucc": "Ser",
    "uca": "Ser", "ucg": "Ser",
    "ccu": "Pro", "ccc": "Pro",
    "cca": "Pro", "ccg": "Pro",
    "acu": "Thr", "acc": "Thr",
    "aca": "Thr", "acg": "Thr",
    "gcu": "Ala", "gcc": "Ala",
    "gca": "Ala", "gcg": "Ala",
    "uau": "Tyr", "uac": "Tyr",
    "uaa": "Stop", "uag": "Stop",
    "cau": "His", "cac": "His",
    "caa": "Gln", "cag": "Gln",
    "aau": "Asn", "aac": "Asn",
    "aaa": "Lys", "aag": "Lys",
    "gau": "Asp", "gac": "Asp",
    "gaa": "Glu", "gag": "Glu",
    "ugu": "Cys", "ugc": "Cys",
    "uga": "Stop", "ugg": "Trp",
    "cgu": "Arg", "cgc": "Arg",
    "cga": "Arg", "cgg": "Arg",
    "agu": "Ser", "agc": "Ser",
    "aga": "Arg", "agg": "Arg",
    "ggu": "Gly", "ggc": "Gly",
    "gga": "Gly", "ggg": "Gly"
}


def translate_codon(codon):
    codon = codon.lower().replace("t", "u")
    return genetic_code.get(codon)


genome = Path(__file__).with_name(
    "rhinovirus_b14.txt"
).read_text().strip()

frequency = Counter()

for i in range(len(genome) - 2):
    codon = genome[i:i + 3]
    amino = translate_codon(codon)

    if amino is not None:
        frequency[amino] += 1

top_amino = dict(frequency.most_common(10))

print("Most frequent amino acids:")
print(top_amino)

plt.bar(top_amino.keys(), top_amino.values(),
        color="orange")
plt.xlabel("Amino acids")
plt.ylabel("Frequency")
plt.title("Amino Acid Distribution")
plt.show()

prompt = (
    "Identify foods containing these amino acids "
    "and explain their dietary importance: "
    + ", ".join(top_amino.keys())
)

print(prompt)

load_dotenv()
api_key = os.getenv("API_KEY")

if api_key:
    client = genai.Client(api_key=api_key)

    response = client.interactions.create(
        model="gemini-3.8-flash",
        input=prompt
    )

    print(response.output_text)
else:
    print("No API key provided.")