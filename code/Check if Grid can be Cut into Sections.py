from typing import List

class Solution:
    def mergeLine(self, lines: List[List[int]]) -> List[List[int]]:
        lines.sort(key=lambda x: x[0])
        merged_lines = [lines[0]]
        for i in range(1, len(lines)):
            if lines[i][0] < merged_lines[-1][1]:
                merged_lines[-1][1] = max(merged_lines[-1][1], lines[i][1])
            else:
                merged_lines.append(lines[i])
        return merged_lines

    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        horizontal_lines = [[rect[0], rect[2]] for rect in rectangles]
        vertical_lines = [[rect[1], rect[3]] for rect in rectangles]

        horizontal_lines = self.mergeLine(horizontal_lines)
        vertical_lines = self.mergeLine(vertical_lines)

        print(horizontal_lines)
        print(vertical_lines)

        return len(horizontal_lines) >= 3 or len(vertical_lines) >= 3
        


rectangles = [[0,0,1,4],[1,0,2,4],[2,0,3,4],[3,0,4,4]]
n = 4
sol = Solution()
result = sol.checkValidCuts(n, rectangles)
print(result)
