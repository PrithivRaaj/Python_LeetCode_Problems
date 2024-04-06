class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=[]
        left=0
        right=0
        for ch in s:
            if ch == '(':
                left+=1
            elif ch==')':
                right+=1
            if right>left:
                right-=1
            else:
                    stack.append(ch)
        result=""
        while stack:
            current_char=stack.pop()
            if left>right and current_char=='(':
                left-=1
            else:
                result+=current_char
        return result[::-1]

        

String_Great=Solution()
result=input()
print(String_Great.minRemoveToMakeValid(result))