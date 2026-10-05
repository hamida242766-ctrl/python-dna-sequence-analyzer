# DNA Sequence Analyzer
# A beginner bioinformatics project using Python and Biopython

from Bio.Seq import Seq
from Bio import SeqIO


record = SeqIO.read("sample.fasta", "fasta")
dna = record.seq

print("DNA sequence:", dna)
print("Length:", len(dna))

print("A:", dna.count("A"))
print("T:", dna.count("T"))
print("G:", dna.count("G"))
print("C:", dna.count("C"))

gc = (dna.count("G") + dna.count("C")) / len(dna) * 100
print("GC content:", round(gc,2), "%")

print("RNA:", dna.transcribe())
print("Reverse complement:", dna.reverse_complement())
print("Protein:", dna.translate())

motif = input("Enter a DNA motif to search for: ").upper()
print("motif positions:", [i for i in range(len(dna)) if dna.startswith(motif, i)])
print("Number of occurrences:", dna.count(motif))

start = dna.find("ATG")
print("Start codon position:", start)

stop = dna.find("TGA", start)
print("Stop codon position:", stop)

orf = dna[start:stop + 3]
print("ORF:", orf)


print("ORF protein:", orf.translate())


