class Solution(object):
    def insert(self, intervals, newInterval):

        result = []

        for interval in intervals:

            # Case 1: Current interval ends before newInterval starts
            if interval[1] < newInterval[0]:
                result.append(interval)

            # Case 2: Current interval starts after newInterval ends
            elif interval[0] > newInterval[1]:
                result.append(newInterval)
                newInterval = interval

            # Case 3: Overlapping intervals
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        result.append(newInterval)

        return result