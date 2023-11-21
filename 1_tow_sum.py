
import random
import time
from typing import Optional
# nums=[2,3,4]
# target = 6
# from datetime import datetime



# def tow_sum(nums,target):
#     for i in range(len(nums)-1): 
#         for j in range(len(nums)-i-1):
#             if nums[i]+nums[i+j+1] == target:
#                 return (i,j+i+1)
# n=1000
# s=0
# for i in range(n):       
#     a=datetime.now()
#     tow_sum(nums,target)
#     b=datetime.now()
#     s+= (b-a).total_seconds()
# print(s/n)



# s="pwwkew"

# def long_str(s):
#     d=[]
#     for j in range(len(s)):
#         l=[]
#         for i in range(j,len(s)):
#             if s[i] in l :
#                 break
#             l.append(s[i])
#         d.append(len(l))
#     return max(d)    
# print(long_str(s))




class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def _len(self):
        if self.next:
            return self.next._len() + 1
        return 1

    def __str__(self) -> str:
        if self.next:
            return str(self.next) + str(self.val)
        return str(self.val)

class Solution1:
    def addTwoNumbers(self, l1, l2):
        l3=ListNode((l1.val + l2.val)%10)
        l4=l3
        b = (l1.val + l2.val)//10
        while  l1.next or l2.next :
            if not l1.next:
                l1.next = ListNode()
            elif not l2.next:
                l2.next = ListNode()
   
            l3.next= ListNode((l1.next.val + l2.next.val + b )%10)
            b = (l1.next.val + l2.next.val + b)//10
            l1 = l1.next
            l2 = l2.next
            l3 = l3.next
           
        if b:
            l3.next= ListNode(b)
        return l4

class Solution2:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3=ListNode((l1.val + l2.val)%10)
        l4=l3
        flag1=True
        flag2=True
        b = (l1.val + l2.val)//10
        l0=ListNode()
        while  l1.next  or l2.next :
            if not l1.next:
                flag1 = False
                l1.next =ListNode()
            elif not l2.next:
                flag2=False
                l2.next = ListNode()
   
            l3.next= ListNode((l1.next.val + l2.next.val + b )%10)
            b = (l1.next.val + l2.next.val + b)//10
            l1 = l1.next
            l2 = l2.next
            l3 = l3.next
           
        if b:
            l3.next= ListNode(b)
        return l4

class Solution3:
    def addTwoNumbers(self, l1, l2):
        l0=ListNode()
        l1 = l1 or l0
        l2 = l2 or l0
        l3=ListNode((l1.val + l2.val)%10)
        l4=l3
        b = (l1.val + l2.val)//10
        while  True:
            l1 = l1.next or l0
            l2 = l2.next or l0
            if l1 is l0 and l2 is l0:
                break
            l3.next= ListNode((l1.val + l2.val + b )%10)
            b = (l1.val + l2.val + b)//10
            l3 = l3.next
           
        if b:
            l3.next= ListNode(b)
        return l4
   

class Solution4:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1, s2 = '', ''
        while l1:
            s1 += str(l1.val)
            l1 = l1.next
        while l2:
            s2 += str(l2.val)
            l2 = l2.next
            
        s1 = int(s1[::-1])
        s2 = int(s2[::-1])
        
        total = str(s1 + s2)
        
        head = None
        for c in total:
            n = ListNode(c)
            n.next = head
            head = n
        return head

order = 10 ** 16
v1 = str(random.randint(order, order*10-1))[::-1]
v2 = str(random.randint(order, order*10-1))[::-1]

def g():
    rl1 = l1 = ListNode(int(v1[0]))
    rl2 = l2 = ListNode(int(v2[0]))
    for i in range(1, len(v1)):
        l1.next = ListNode(int(v1[i]))
        l2.next = ListNode(int(v2[i]))
        l1 = l1.next
        l2 = l2.next
    return rl1, rl2

r1,r2 = g()
print('run 1:', end=' ')
a=time.monotonic()
d = Solution1().addTwoNumbers(r1,r2)
b=time.monotonic()
print(f'{b-a} : {d}')

r1,r2 =g()
print('run 2:', end=' ')
a=time.monotonic()
d = Solution2().addTwoNumbers(r1,r2)
b=time.monotonic()
print(f'{b-a} : {d}')


r1,r2 =g()
print('run 3:', end=' ')
a=time.monotonic()
d = Solution3().addTwoNumbers(r1,r2)
b=time.monotonic()
print(f'{b-a} : {d}')

r1,r2 =g()
print('run 3:', end=' ')
a=time.monotonic()
d = Solution4().addTwoNumbers(r1,r2)
b=time.monotonic()
print(f'{b-a} : {d}')
