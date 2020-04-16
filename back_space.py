"""Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c" ==> result = ac
Output: true
Explanation: Both S and T become "ac".

ab##c -> c

"""



def backspaceCompare(S, T):
    
    
    def backspace(s):
        bcount = 0
        result = ""
        
        idx = len(s) - 1
        
        while idx >= 0:
            while s[idx] == "#":
                bcount += 1
                idx -= 1
            while idx >=0 and s[idx] != "#":
                if bcount > 0:
                    bcount -= 1
                else:
                    result = s[idx] + result
                idx -= 1
        
        return result
       
    
    s = backspace(S)
    t = backspace(T)
    print('s',s)
    print('t',t)
    
    return s == t
        
    
        
print(backspaceCompare("ab#c","ad#c"))