def factors(n):
    def dfs(n, i, combi, combis):
        while i * i <= n:
            if n % i == 0:
                combis.append(combi + [i, n // i])
                dfs(n // i, i, combi + [i], combis)
            i += 1
        return combis

    return dfs(n, 2, [], [])


res = factors(32)

print(res)
