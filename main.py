from pprint import pprint
from itertools import permutations
import sys
import fasta_parser
import alignment

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    sys.exit("Usage: " + sys.argv[0] + " [fasta_filename]")

reads   = []
names   = []

with open(filename) as fp:
    for (name, seq) in fasta_parser.read_fasta(fp):
        names.append(name)
        reads.append(seq)

perms = permutations(reads, 2)

for perm in perms:
    print("Sequence1")
    print("Name: " + names[reads.index(perm[0])])
    print("Sequence: " + perm[0])
    print("Sequence2")
    print("Name: " + names[reads.index(perm[1])])
    print("Sequence: " + perm[1])
    [X, Y, M] = alignment.distance_matrix(perm[0], perm[1])
    [str1, str2] = alignment.backtrace(perm[0], perm[1], X, Y, M)
    print("-=Alignment=-")
    print(str1)
    print(str2)
    print("\n")
