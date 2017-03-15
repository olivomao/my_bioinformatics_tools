import sys, pdb

'''
extended operations on fasta files
'''

'''
read fasta file and output sequences (seq_name & seq)

copied from refS util

usage: python fasta_ext.py --from_fasta --fa filename

'''
def from_fasta(args):
    filename = args[args.index('--fa')+1]
    pdb.set_trace()

    sequences = {} #[]
    seq = []
    next_name = '_'
    with open(filename) as f:
        for line in f:
            if line[0] == '>':
                #sequences.append((next_name, ''.join(seq)))
                sequences[next_name]=''.join(seq)
                seq = []
                next_name = line.split()[0][1:]
            else:
                seq.append(line.strip().upper())
    #sequences.append((next_name, ''.join(seq)))
    sequences[next_name]=''.join(seq)
    del sequences['_']
    pdb.set_trace()
    return sequences #[1:]

def main():

    return

'''
usage:

#read fasta seq
python fasta_ext.py --from_fasta --fa filename

'''

if __name__ == "__main__":

    args = sys.argv

    if '--from_fasta' in args:
        from_fasta(args)
    else:
        main()