# Este algoritmo evalua las particiones para generar una suma. Diciendo 'particiones' damos a entender que 2+1+1 = 1+2+1 = 1+1+2. 
# Definen la misma particion estos elementos. Esa es la diferencia entre este problema y las soluciones que hice en otros problemas donde buscaba
# simplemente todas las combinaciones posibles en todos los ordenes
# En este caso, se puede decir que el orden no importaria.

arr = [1,2,5]
amount = 5
# 5
# 2+2+1
# 2+1+1+1
# 1+1+1+1+1


# No es cuestion de hacer combinatoria, porque voy a tener arrays
# con los mismos elementos en diferente orden
# Necesito aplicar la teoria de Integer partitions
# Cuantas maneras hay de generar un entero a partir de la suma de enteros menores?

# Dado un array de enteros, y un entero representando la suma total deseada
# Yo voy a ir generando las distintas sumas hasta el total, pero tambien considerando que mi array es variable, por lo que ahora mi subproblems_arr (referirse a otros ejercicios hechos con tabulacion) no sera un array sino una matriz de total*(len(arr)+1)
# por que?
# Primero voy a ir generando las sumas suponiendo que tengo un array vacio
# Luego voy a generar las mismas sumas pero considerando agregar a mi array una de las monedas disponibles.
# and so on, por eso es una matriz.
# En cada subproblema, voya preguntarme, uso la moneda actual que quiero agregar o no? Es posible usarla? poque tal vez, la moneda es mas grande que el subtotal, en ese caso, mi solucion solo dependera de la solucion al mismo subtotal, pero sin tener en cuenta a x, porque justamente no voy a poder utilizarla
# Si considero NO usarla, voy a tener en cuenta entonces las soluciones al subproblema de la fila de arriba (subproblema donde justamente NO considerabamos a la moneda x) y ese sera mi resultado.
# Si considero usar la moneda, ademas de la solucion de arriba, voy a tener en cuenta (si es posible) la solucion para el subtotal i - x, donde i es el subtotal actual y x la moneda. Es decir, si pude generar i-x, seguro voy a poder generar i

# Por que 'si es posible'? porque puede pasar que i-x < 0, por lo que no es posible usar la moneda x para el subtotal i. Seria como intentar generar 50 con monedas de 70.

# A nivel practico, cada subproblema dependera de la fila anterior y de x-columnas anteriores

def total_unique_ways(total, coins):
    subproblems_arr = [ [ 0 for i in range(total+1)] for j in range(len(coins)+1)]
   
    for i in range(len(coins)+1):
        subproblems_arr[i][0] = 1 
    for j in range(1,total+1):
        subproblems_arr[0][j] = 0
    # solo hay una forma de generar al subtotal 0: tomando ninguna moneda, por eso es una combinacion posible
    #con 0 monedas, solo es posible formar el subtotal 0, el resto no es posible, por lo que hya 0 formas para el resto de la fila 0
    # ESTOS serian mis semillas, a partir de aca puedo aplicar el algoritmo
    
    for row in range(1, len(coins)+1):
        for col in range(1, total+1):
            print(f"Subproblema para el subtotal {col} con las monedas{coins[:row]}")
            aux1 = subproblems_arr[row - 1][col] if (row - 1)>=0 else 0
            last_coin_inserted = coins[:row][-1] if len(coins[:row])>0 else 0 
            aux2 = subproblems_arr[row][col-last_coin_inserted] if (col-last_coin_inserted) >= 0 else 0
            subproblems_arr[row][col] = aux1 + aux2
            
    
    
    print(subproblems_arr)
    return subproblems_arr[-1][-1]

print(total_unique_ways(amount, arr))
