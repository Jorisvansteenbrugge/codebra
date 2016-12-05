#!/usr/bin/env python

from sys import argv

def parse_fasta(fasta_file):
    """Returns a dictionary from a fasta file containing the protein IDs (as keys), the protein sequence and the length of this sequence.
    fasta_file = a .fasta file containg one or more protein sequences"""
    sequence_dict = {}
    seq = ''
    for line in fasta_file:
        line = line.strip()
        if not line.startswith(">"):
            seq += line
        if line.startswith(">"):
            if not seq == '':
                sequence_dict[key] = seq
                seq = ''
            line = line.split(' ')
            key = line[0][1:]
    sequence_dict[key] = seq
    return sequence_dict

def match_orthologs(sequence_dict, sequenceID):
    #No_Orthologs_seq = 
    print sequence_dict.keys()
    for ID in sequenceID:
	print ID
	ID = ID.strip()
	if ID == '':
	    continue
	if ID in sequence_dict.keys():
	    del sequence_dict[ID]
	    #print sequence_dict.keys()
	    #print '>' + ID + '\n' + sequence_dict[ID]
    return sequence_dict

def write_fasta(sequence_dict):
    for ID in sequence_dict:
	print '>' + ID + '\n' + sequence_dict[ID]
    return '' 

if __name__ == '__main__':
    sequence_dict = parse_fasta(open(argv[1], 'r'))
    sequenceID = open(argv[2], 'r')
    sequence_dict2 = match_orthologs(sequence_dict, sequenceID)
    print write_fasta(sequence_dict2)
