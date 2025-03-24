from typing import List
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        cur = []
        num_of_letters = 0

        for w in words:
            if num_of_letters + len(w) + len(cur) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    cur[i % (len(cur) - 1 or 1)] += ' '
                res.append(''.join(cur))
                cur, num_of_letters = [], 0
            cur += [w]
            num_of_letters += len(w)

        return res + [' '.join(cur).ljust(maxWidth)]


example1 = ["This", "is", "an", "example", "of", "text", "justification."]
example2 = ["What", "must", "be", "acknowledgment", "shall", "be"]
example3 = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"]
example4 = ["The", "longest", "word", "in", "the", "English", "language", "is", "pneumonoultramicroscopicsilicovolcanoconiosis"]

solution = Solution()
max_width1 = 16
result = solution.fullJustify(example1, max_width1)
for line in result:
    print(f'"{line}"')

