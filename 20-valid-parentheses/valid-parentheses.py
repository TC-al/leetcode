class Solution(object):
    def isValid(self, s):
        lst = [char for char in s]

        pairs = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        if len(lst) % 2 != 0:
            return False

        for x in range(len(lst) / 2):
            for y in range(len(lst)):
                if y < len(lst)-1 and lst[y] in pairs and pairs[lst[y]] == lst[y + 1]:
                    lst.pop(y+1)
                    lst.pop(y)

            if len(lst) != 0 and lst[0] in pairs and pairs[lst[0]] == lst[-1]:
                lst.pop()
                lst.pop(0)


        if len(lst) == 0:
            return True

        else:
            if ord(lst[-1]) - ord('0') == (ord(lst[0]) - ord('0')) - 1:
                return True
            return False

        return True
         