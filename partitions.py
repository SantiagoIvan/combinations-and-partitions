def partitions(total):
    integers = [ i for i in range(1,total+1)]
    subproblems_arr = [ [ 0 for i in range(total+1)] for j in range(len(integers)+1)]
   
    for i in range(len(integers)+1):
        subproblems_arr[i][0] = 1 
    for j in range(1,total+1):
        subproblems_arr[0][j] = 0
    
    for row in range(1, len(integers)+1):
        for col in range(1, total+1):
            aux1 = subproblems_arr[row - 1][col] if (row - 1)>=0 else 0
            last_integer_inserted = integers[:row][-1] if len(integers[:row])>0 else 0 
            aux2 = subproblems_arr[row][col-last_integer_inserted] if (col-last_integer_inserted) >= 0 else 0
            subproblems_arr[row][col] = aux1 + aux2
            
    return subproblems_arr[-1][-1]
