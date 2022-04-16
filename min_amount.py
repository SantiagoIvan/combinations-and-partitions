# Resuelto utilizando el enfoque recursivo o Up-to-Down, usando depthfirst
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

# Resuelto usando el enfoque de tabulacion, o Down-to-Up.
def min_amount_of_coins2(total, coins):
    subproblems_arr = [total if i != 0 else 0 for i in range(total+1)]# deberia inicializar con un numero infinito a todos los demas casilleros, para que de esa forma, la primera vez que haga 'min()' sea True. O puedo hacer que sea igual al maximo posible que en este casoes 'total'
    
    for i in range(total+1):
        if subproblems_arr[i] == None: continue
        
        for coin in coins:
            if i+coin<=total:
                subproblems_arr[i+coin] = min(subproblems_arr[i]+1, subproblems_arr[i+coin])
    return subproblems_arr[-1]


coins = [1, 3, 5, 6, 9]
total = 90 #deberia dar 10
memo_dict = {}
res = min_amount_of_coins(total, coins, memo_dict)
print(res)
res = min_amount_of_coins2(total, coins)
print(res)
