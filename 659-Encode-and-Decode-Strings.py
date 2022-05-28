# encode needs to separate words using some means that can be differentiated from the contents of the original strings
# basically just implmenting escape characters
class Solution:
    # """
    # @param: strs: a list of strings
    # @return: encodes a list of strings to a single string.
    # """
    def encode(self, strs):
        encoded = []
        
        for str in strs:
            for char in str:
                if char == '|':
                    encoded.append('@|')
                else:
                    encoded.append(char)
            encoded.append('|')
        return ''.join(encoded)

    # """
    # @param: str: A string
    # @return: dcodes a single string to a list of strings
    # """
    def decode(self, str):
        decoded = []
        delimiter = '|' # can imagine instead of a single character, this was a list of characters
        escape_char = '@'
        idx = 0
        tmp_str = []
     
        while idx < len(str):
            if str[idx] == delimiter: # could instead check if str[idx] is in list of special characters
                if str[idx - 1] == escape_char:
                    tmp_str.append(str[idx])
                    idx += 1
                else:
                    decoded.append(''.join(tmp_str))
                    tmp_str = []
                    idx += 1
            else:
                if str[idx] == escape_char:
                    idx += 1
                    continue
                tmp_str.append(str[idx])
                idx += 1
        
        return decoded
# Test
def main():
    test = Solution()
    n = ["li|nt","c|ode","love","you"]
    print(test.encode(n)) # ["lint|code|love|you"]
    print(test.decode(test.encode(n))) # ["lint","code","love","you"]
    
# Run test script if this file is not being imported
if __name__ == '__main__':
    main()