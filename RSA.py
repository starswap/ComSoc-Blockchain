import random
def miller_rabin(integer):
  twoToS = 1
  S = 0
  while (integer%twoToS == 0):
    twoToS *= 2
    S+=1
  twoToS /= 2
  S -= 1
  q = integer/twoToS 
  a = random.randint(1,integer)
  if (pow(a,q,integer)):
    return True
  else:
    for (i in range(S)):
      