# encode needs to separate words using some means that can be differentiated from the contents of the original strings
class Solution:
    # """
    # @param: strs: a list of strings
    # @return: encodes a list of strings to a single string.
    # """
    def encode(self, strs):
        encoded = []
        delimiter = '|'
        
        for str in strs:
            for char in str:
                if char == delimiter:
                    encoded.append(delimiter)
                encoded.append(char)
            encoded.append(delimiter + ' ')  
        return ''.join(encoded)

    # """
    # @param: str: A string
    # @return: dcodes a single string to a list of strings
    # """
    def decode(self, str):
        decoded = []
        delimiter = '|'
        idx = 0
        char_list = []
     
        while idx < len(str):
            if str[idx] == delimiter:
                if str[idx + 1] == delimiter:
                    char_list.append(str[idx])
                    idx += 2
                elif str[idx + 1] == ' ':
                    decoded.append(''.join(char_list))
                    char_list = []
                    idx += 2
            else:
                char_list.append(str[idx])
                idx += 1
        
        return decoded
# Test
def main():
    test = Solution()
    n = ["li|nt","code","love| ","| you| "]
    print(test.encode(n)) # ["lint|code|love|you"]
    print(test.decode(test.encode(n))) # ["lint","code","love","you"]
    
# Run test script if this file is not being imported
if __name__ == '__main__':
    main()