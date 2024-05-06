class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        
        hashmap = {}
        mapped_chars = set()

        for i in range(len(s)):
            s_char, t_char = s[i], t[i]

            if s_char in hashmap:
                if hashmap[s_char] != t_char:
                    return False
            else:
                if t_char in mapped_chars:
                    return False
                hashmap[s_char] = t_char
                mapped_chars.add(t_char)

        return True
