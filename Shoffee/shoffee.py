info1 = list(map(lambda x: int(x), input().split()))


N = int(info1[0])
K = int(info1[1])
array = list(map(lambda x: int(x), input().split()))
Vhat = []
for level in range(1,N+1):
    digits_to_add = level
    for integer in range(0,len(array)):
        # for each level, you want to add the current integer with as many of the consecutive one until you hit thje level OR the end is out of the list
        if (integer+level-1) < N:
            count = 0
            current_sum = array[integer]
            while count < digits_to_add -1:
                current_sum += array[integer+count+1]
                count += 1
            Vhat.append(current_sum/level)

type_count = 0
for i in range(0, len(Vhat)):
    if Vhat[i] >= K:
        type_count += 1
print(type_count)