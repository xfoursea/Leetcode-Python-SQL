from typing import List

class Solution:
    '''
    Input: tasks = ["A","A","A","B","B","B"], n = 2
    Output: 8
    Explanation:
    A -> B -> idle -> A -> B -> idle -> A -> B
    '''
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_ls = [0] * 26
        for ch in tasks:
            task_ls[ord(ch) -ord('A')] += 1
        f_max = max(task_ls)
        n_max = task_ls.count(f_max)


        return max(len(tasks),(f_max -1) * (n+1) + n_max )

