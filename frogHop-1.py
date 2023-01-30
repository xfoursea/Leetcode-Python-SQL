
from typing import List
# Frog hop: https://www.metacareers.com/profile/coding_puzzles/?puzzle=977526253003069

def getSecondsRequired(N: int, F: int, P: List[int]) -> int:
  # Write your code here
  min_v = min(P)
  max_v = max(P)
  
  #first, move them to ensure no space
  #steps
  step1 = max_v - min_v - F+1
  
  # steps to move the block to second last
  step2 = N- max_v -1
  
  #steps to move each individual
  step3 = F
  
  
  return step1 + step2 + step3
