from typing import List
from collections import Counter

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        cnt = Counter(students)
        for s in sandwiches:
            if cnt[s] > 0:
                res -= 1
                cnt[s] -= 1
            else:
                return res
        return res

# Taking user input
students = list(map(int, input().split()))
sandwiches = list(map(int, input().split()))

# Example usage:
solution = Solution()
print(solution.countStudents(students, sandwiches))