def min_amount_of_coins(total, coins, memo):
    if total == 0:return 0 # para un total de 0 , necesito 0 monedas
    if total <0: return -1 # no hay combinacion posible
    if total in memo:
        return memo[total]
    
    aux = []
    for coin in coins:
        res = min_amount_of_coins(total - coin, coins, memo)
        if res>=0:
            aux.append(res)
    min_value = min(aux)
    memo[total] = min_value+1
    return memo[total]

coins = [1, 3, 5, 6, 9]
total = 90 #deberia dar 10
memo_dict = {}
res = min_amount_of_coins(total, coins, memo_dict)
print(res)
