class Solution:

    # revised
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

    # initial quick and dirty
    def merge_old(self, intervals: List[List[int]]) -> List[List[int]]:
            res = []

        tmp1 = intervals.pop()
        print(tmp1)
        while intervals:
            tmp2 = intervals.pop()
            if tmp2[1] >= tmp1[0]:
                tmp1 = [tmp2[0], max(tmp1[1], tmp2[1])]
                print(tmp1)
            else:
                res.append(tmp1)
                tmp1 = tmp2
        res.append(tmp1)

        res.sort(key=lambda x: x[1])
        res1 = []
        tmp1 = res.pop()
        while res:
            tmp2 = res.pop()
            if tmp2[1] >= tmp1[0]:
                tmp1 = [min(tmp1[0], tmp2[0]), tmp1[1]]
            else:
                res1.append(tmp1)
                tmp1 = tmp2
        res1.append(tmp1)

        return res1
