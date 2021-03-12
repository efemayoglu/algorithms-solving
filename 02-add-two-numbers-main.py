# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        arr1 = NodeToArray(l1)
        arr2 = NodeToArray(l2)

        result = list()
        if findLongest(l1,l2): 
            result = sumTwoArray(arr1,arr2)
        else: 
            result = sumTwoArray(arr2,arr1)
        
        return arrayToNode(list(reversed(result)))

def arrayToNode(arr: list) -> ListNode:
    tail = head = ListNode(arr[0])
    for i in arr[1:]:
        tail.next = ListNode(i)
        tail = tail.next
    tail.next = None

    return head

def sumTwoArray(arr1: list, arr2: list) -> list:
    sum = []
    for i,n in enumerate(arr1):
        if len(sum) <= i:
            sum.append(0)
        arr2Value = 0 if len(arr2) <=i else arr2[i]
        currentSum = n + arr2Value + sum[i]
        
        if(currentSum>=10):
            sum.append(0)
            sum[i+1] = sum[i+1]  + 1
            sum[i] =  currentSum % 10
        else:
            sum[i] = currentSum         
    return sum

def NodeToArray(l: ListNode) -> list:
    arr = []
    while l.next != None:
        arr.append(l.val)
        l = l.next
    arr.append(l.val)
    return arr


def findLongest(l1: ListNode, l2: ListNode) -> bool:
    l1Count = 0
    l2Count = 0
    while l1.next != None:
        l1 = l1.next
        l1Count = l1Count + 1
    while l2.next != None:
        l2 = l2.next
        l2Count = l2Count + 1

    return True if l1Count >= l2Count else False
    



l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
l2 = ListNode(9, ListNode(9, ListNode(9)))

solution = Solution()
print(solution.addTwoNumbers(l1,l2))