def parindrome(s):
    if s[::] == s[::-1]:
        return True
    return False

def string_parindrome(s):
    if parindrome(s):
        N = len(s)
        if parindrome(s[:((N-1)//2):]) and parindrome(s[((N+3)//2)-1::]):
            return "Yes"
    return "No"
    

S = input()
print(string_parindrome(S))
