\# DNA Sequence Analyzer



A beginner-friendly bioinformatics project built using \*\*Python\*\* and \*\*Biopython\*\* to analyze DNA sequences from FASTA files.



\## Features



\* Reads DNA sequences from a FASTA file

\* Calculates DNA sequence length

\* Counts A, T, G, and C nucleotides

\* Calculates GC content

\* Transcribes DNA into RNA

\* Generates the reverse complement

\* Translates DNA into protein

\* Searches for user-specified DNA motifs

\* Counts motif occurrences

\* Identifies a start codon (ATG)

\* Identifies a stop codon (TGA)

\* Extracts an open reading frame (ORF)

\* Translates the ORF into a protein sequence



\## Technologies Used



\* Python

\* Biopython

\* FASTA format



\## Input



The program reads the DNA sequence from `sample.fasta`.



Example:



```text

>sample\_dna

ATGCGATACGCTTGA

```



\## Example Output



```text

DNA sequence: ATGCGATACGCTTGA

Length: 15

A: 4

T: 4

G: 4

C: 3

GC content: 46.67 %

RNA: AUGCGAUACGCUUGA

Reverse complement: TCAAGCGTATCGCAT

Protein: MRYA\*

GCT positions: \[9]

Number of occurrences: 1

Start codon position: 0

Stop codon position: 12

ORF: ATGCGATACGCTTGA

ORF protein: MRYA\*

```



\## Purpose



This project was created as a beginner bioinformatics project to practice Python programming and basic DNA sequence analysis using Biopython.



