'''
def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
  # Write your code here
  #APABA
  if not C or not N or not X or not Y:
    return 0
  a_ls = []
  p,b ={},{}
  for i in range(N):
    if C[i] =='A':
      a_ls.append(i)
      p[i]=p.get(i-1,0)
      b[i]=b.get(i-1,0)      
    elif C[i] =='P':
      p[i]=p.get(i-1,0)+1
      b[i]=b.get(i-1,0)
    elif C[i] =='B':
      b[i]=b.get(i-1,0)+1
      p[i]=p.get(i-1,0)
    else:
      p[i]=p.get(i-1,0)
      b[i]=b.get(i-1,0) 
  print(a_ls)    
  print(b)
  print(p)    
  res = 0 
  
  for i in a_ls:
    r_start = N-1 if i+X >=N-1 else i+X-1
    r_end = N-1 if i+Y >= N-1 else i+Y
    l_start = i-Y-1 if i-Y-1 >=0 else 0
    l_end = i-X if i-X >=0 else 0
    print(f"r_start:{r_start}")
    print(f"r_end:{r_end}")
    print(f"l_start:{l_start}")
    print(f"l_end:{l_end}")
    res += (p[r_end]-p[r_start]) * (b[l_end]-b[l_start])
    res += (b[r_end]-b[r_start]) * (p[l_end]-p[l_start])

  return res
'''
def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
  # Prefix 
  pSum = [0]
  bSum = [0]
  
  for c in C:
    if c == "P":
      pSum.append(pSum[-1] + 1)
    else:
      pSum.append(pSum[-1])
  for c in C:
    if c == "B":
      bSum.append(bSum[-1] + 1)
    else:
      bSum.append(bSum[-1])

  result = 0
  
  def bounded(x):
    return max(0, min(x, N))
  
  for i, c in enumerate(C):
    if c == "A":
      #rightWindow = (bounded(i+X), bounded(i+Y+1))
      #leftWindow = (bounded(i-Y), bounded(i-X+1))
      rightWindow = (min(i+X, N), min(i+Y+1,N))
      leftWindow = (max(0,i-Y),max(0,i-X+1))
      print(f"rightWindow: {rightWindow}")
      print(f"leftWindow: {leftWindow}")
      leftPs = pSum[leftWindow[1]] - pSum[leftWindow[0]]
      rightBs = bSum[rightWindow[1]] - bSum[rightWindow[0]]
      result += leftPs * rightBs
      
      rightPs = pSum[rightWindow[1]] - pSum[rightWindow[0]]
      leftBs = bSum[leftWindow[1]] - bSum[leftWindow[0]]
      result += leftBs * rightPs
        
  return result

if __name__ == "__main__":
    print("main called")
    n = getArtisticPhotographCount(8, ".PBAAP.B", 1,3)
    print(n)