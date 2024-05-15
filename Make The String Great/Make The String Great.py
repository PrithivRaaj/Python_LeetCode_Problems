class Solution:
    def makeGood(self, s: str) -> str:
        Anser=[]
        for ch in s:
            if Anser and Anser[-1].isupper() and Anser[-1].lower() == ch:
                Anser.pop()
            elif Anser and Anser[-1].islower() and Anser[-1].upper() == ch:
                Anser.pop()
            else:
                Anser.append(ch)
        return "".join(Anser)

String_Great=Solution()
result=input()
print(String_Great.makeGood(result))