# descending: check if first two elements are ordered correctly
#   and that the rest of the sequence is descending

def descending(l):
  if len(l) < 2:
    return(True)
  return(l[0] >= l[1] and descending(l[1:]))

# updown: a sequence that starts strictly ascending and rest is downup
# downup: a sequence that starts strictly descending and rest is updown
# alternately updown,downup,... or downup,updown,... is alternating

def updown(l):
  if len(l) < 2:
    return(True)
  return(l[0] < l[1] and downup(l[1:]))

def downup(l):
  if len(l) < 2:
    return(True)
  return(l[0] > l[1] and updown(l[1:]))
    
def alternating(l):
  return(updown(l) or downup(l))

# Use list comprehension to initialize product matrix to 0
# Use three nested loops to compute each entry in product

def matmult(m1,m2):
  mult=[len(m2[0])*[0] for i in range(0,len(m1))]
  for i in range(0,len(m1)):
    for j in range(0,len(m2[0])):
      mult[i][j]=0
      for k in range(0,len(m1[0])):
        mult[i][j]=mult[i][j]+m1[i][k]*m2[k][j]
  return(mult)

