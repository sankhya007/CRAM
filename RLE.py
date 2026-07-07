# run length encoding (RLE)

class Solution: 
    def encode(self, s): 
        if not s: 
            return ""
        encoded = []
        count = 1
        for i in range(1, len(s)): 
            if s[i] == s[i - 1]: 
                count += 1
            else: 
                encoded.append(f"{count}{s[i - 1]}")
                count = 1
        encoded.append(f"{count}{s[-1]}")
        return "".join(encoded)
    
file_read = open("example.txt", "r")
sol = Solution()
print(sol.encode(file_read.read()))  

# with open("example.txt", 'r') as file:  #to read the content of a file
#     content = file.read()
# print(content)

# LZ77 LZ78 LZW 