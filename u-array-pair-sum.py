def pair_sum(arr, target):
    if len(arr) < 2:
        return

    seen = set()
    output = set()

    for i in arr:
        t = target-i

        if t not in seen:
            seen.add(i)
        else:
            output.add((
                (
                    min(i, t)
                ),
                (
                    max(i,t)
                )

            )) 

    return output



print(pair_sum([1,3,2,2],4))







# def pair_sum(arr, target):
#     a = {}
#     for i in range(len(arr)):
#         if arr[i] not in a:
#             if (target - arr[i]) in arr:
#                 if target-arr[i] not in a:
#                     a[arr[i]] = (target-arr[i])
#     return a



# def pair_sum(arr, k):
#     if len(arr)<2:
#         return

#     seen = set()
#     output = set()

#     for num in arr:
#         target = k-num
        
#         if target not in seen:
#             seen.add(num)
#         else:
#             output.add(((min(num,target)), max(num,target)))

#     return output


# print(pair_sum([1,3,2,2],4))
