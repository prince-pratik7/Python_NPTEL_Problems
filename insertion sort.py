def insert(seq,k):
    pos=k
    while pos>0 and seq[pos] < seq[pos-1]:
        (seq[pos],seq[pos-1])=(seq[pos-1],seq[pos])
        pos=pos-1
        
def isort(seq,k):
    if k>1:
        isort(seq,k-1)
        insert(seq,k-1)
        
def insertionsort(seq):
    isort(seq,len(seq))
    return seq
'''use this if you want to increase the recursion limit in python interpreter
import sys
sys.setrecursionlimit(10000)
'''
