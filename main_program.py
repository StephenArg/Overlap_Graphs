import os
import itertools

os.chdir("/Users/BasicallySteve/Desktop")

file = open('data.txt', 'r')
label_list = []
DNA_list = []
DNA_combined = ""
thing = []

for DNA in file.readlines():
    if DNA[0] == ">":
        DNA_list.append(DNA_combined)
        DNA_combined = ""
        DNA = DNA.replace("\n", "")
        DNA = DNA.replace(">", "")
        label_list.append(DNA)
    else:
        DNA = DNA.replace("\n", "")
        DNA_combined += DNA

DNA_list.append(DNA_combined)

del DNA_list[0]

data = dict(zip(label_list, DNA_list))

def is_k_overlap(s1, s2, k):
    return s1[-k:] == s2[:k]


def k_edges(data, k):
    edges = []
    for u,v in itertools.combinations(data, 2):
        u_dna, v_dna = data[u], data[v]

        if is_k_overlap(u_dna, v_dna, k):
            edges.append((u,v))

        if is_k_overlap(v_dna, u_dna, k):
            edges.append((v,u))
    return edges

print(k_edges(data, 3))
