def peek_stack(stack):
    if stack:
        return stack[-1]
    else:
        return None

class Solution:
    def isValid(self, s: str) -> bool:
        openParentheses = ['(', '[', '{']
        closeParentheses = [')', ']', '}']
        stack = []
        i = 0
        while i < len(s):
            if s[i] in openParentheses:
                stack.append(s[i])
            if s[i] in closeParentheses:
                if s[i] == ')' and peek_stack(stack) == '(':
                    stack.pop()
                elif s[i] == ']' and peek_stack(stack) == '[':
                    stack.pop()
                elif s[i] == '}' and peek_stack(stack) == '{':
                    stack.pop()
                else:
                    stack.append(s[i])
            i += 1
        return not stack

# Test script
def main():
    test = Solution()
    print (test.isValid('()]')) # False
    print (test.isValid('()')) # True
    print (test.isValid('(asdasd)')) # True
    print (test.isValid('{(asdasd)]')) # False
    
# Run test script if this file is not being imported
if __name__ == '__main__':
    main()