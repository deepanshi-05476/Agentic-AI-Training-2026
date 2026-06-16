class Solution(object):
    def longestPalindrome(self, s):
        maxi = 0 
        start = 0 

        for i in range(len(s)):
            l = i
            r = i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > maxi:
                    start = l
                    maxi = r - l + 1
                l -= 1
                r += 1

            l = i
            r = i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > maxi:
                    start = l
                    maxi = r - l + 1
                l -= 1
                r += 1

        return s[start:start + maxi]


s = "babad"       
obj = Solution()
result = obj.longestPalindrome(s)
print(result)
