class Solution:

    def encode(self, strs: List[str]) -> str:
        msg = ""
        for s in strs:
            length = len(s)
            msg = msg + str(length) + "#" + s
        return msg

    def decode(self, s: str) -> List[str]:
        result = list()
        count = ""
        i = 0

        while i < len(s):
            if s[i].isdigit():
                count = count + s[i]
                i += 1
            else:
                i += 1
                c = int(count)
                count = ""
                string = ""
                while c > 0:
                    string = string + s[i]
                    i += 1
                    c -= 1
                result.append(string)
        return result         
