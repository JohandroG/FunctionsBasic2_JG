#========================================= Coutdown =============================================


def countDown(num):

    result = []
    for i in range (num, -1, -1):
        result.append(i)
    print(result)


countDown(5)



#========================================= Print and Return =============================================

def print_and_return(arr):
    
    for i in range (1,3,1):
        print(arr[0])
        return arr[1]

print_and_return([1,5])


#========================================= First Plus Length =============================================

def first_plus_length(arr):

    sum = 0

    for i in range(0,len(arr),1):
        sum = arr[0] + len(arr)
    print(sum)

first_plus_length ([1,2,3,4,5])


#========================================= Values Greater than Second =============================================

def values_greater_than_second(arr):

    greatervalues = []
    
    if len(arr) < 2:
        return False
    else:
        for i in range (0, len(arr), 1):
            if arr[i] > arr[1]:
                greatervalues.append(arr[i])
    
    print (len(greatervalues))
    return greatervalues
    

print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))



#========================================= List Length, That Value =============================================

def length_and_value(a,b):

    array = []

    for i in range (0,a,1):
        array.append(b)
    print(array)

length_and_value(4,7)
length_and_value(6,2)

