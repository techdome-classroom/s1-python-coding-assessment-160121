def decode_message(s: str, p: str) -> bool:
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[m][n] = True
    
    for j in range(n - 1, -1, -1):
        if p[j] == '*':
            dp[m][j] = dp[m][j + 1]
    
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if p[j] == s[i] or p[j] == '?':
                dp[i][j] = dp[i + 1][j + 1]
            elif p[j] == '*':
                dp[i][j] = dp[i][j + 1] or dp[i + 1][j]
    
    return dp[0][0]
