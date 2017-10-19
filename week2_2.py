def intreverse(n):
# Build up the answer digit by digit
# Extract rightmost digit as remainder when dividing by 10
# Append it to answer by shifting current answer left (multply by 10)
  ans = 0
  while n > 0:
    (d,n) = (n%10,n//10)
    ans = 10*ans + d
  return(ans)

def matched(s):
# Keep track of nesting depth
# Each "(" increases nesting depth, each ")" decreases nesting depth
# If nesting depth is ever negative, more ")" than "(", so False
# Otherwise, check that all "(" have been closed, so nesting depth 0
  nested = 0
  for i in range(0,len(s)):
    if s[i] == "(":
       nested = nested+1
    elif s[i] == ")":
       nested = nested-1
       if nested < 0:
          return(False)    
  return(nested == 0)

def factors(n):
# Brute force: check each number 1..n
  factorlist = []
  for i in range(1,n+1):
    if n%i == 0:
      factorlist = factorlist + [i]
  return(factorlist)

def isprime(n):
# n is a prime if its only factors are 1 and n
  return(factors(n) == [1,n])


def sumprimes(l):
# Check each element in l, if prime add to sum
  sum = 0
  for i in range(0,len(l)):
    if isprime(l[i]):
      sum = sum+l[i]
  return(sum)

