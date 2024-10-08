def decode_message(s: str, p: str) -> bool:
    
    len_s, len_p = len(s), len(p)

    
    dp = [[False] * (len_p + 1) for _ in range(len_s + 1)]
    
    
    dp[0][0] = True

    
    for j in range(1, len_p + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]

    
    for i in range(1, len_s + 1):
        for j in range(1, len_p + 1):
            if p[j - 1] == '*':
               
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
            elif p[j - 1] == '?' or p[j - 1] == s[i - 1]:
               
                dp[i][j] = dp[i - 1][j - 1]

   
    return dp[len_s][len_p]


if __name__ == "__main__":
    print(decode_message("aa", "a"))      
    print(decode_message("aa", "*"))       
    print(decode_message("cb", "?a"))      
    print(decode_message("adceb", "*a*b"))
    print(decode_message("acdcb", "a*c?b")) 
    
