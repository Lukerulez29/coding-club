class ListNode:
    def __init__(self, x, next = None):
         self.val = x
         self.next = next


l1 = ListNode(0)
duml1 = l1
l2 = ListNode(0)
duml2 = l2
one = [5,2,9,8,7]
two = [7,9]


for i in one:
    duml1.next = ListNode(int(i))
    duml1 = duml1.next
for i in two:
    duml2.next = ListNode(int(i))
    duml2 = duml2.next

#real code starts
num1 = []
node1 = l1.next
while node1 != None:
    num1.append(int(node1.val))
    node1 = node1.next

num2 = []
node2 = l2.next
while node2 != None:
    num2.append(int(node2.val))
    node2 = node2.next


ans = []
carry = 0
counter = 0
final = []

while (counter < len(num1)) or (carry > 0) or (counter < len(num2)):
    if (0 <= counter < len(num1)) and (0 <= counter < len(num2)):
        final = (num1[counter] + num2[counter] + carry)%10
        carry = (num1[counter] + num2[counter] + carry) // 10
    elif (0 <= counter < len(num1)) and not (0 <= counter < len(num2)):
        final = (num1[counter] + carry)%10
        carry = (num1[counter] + carry) // 10
    elif (0 <= counter < len(num2)) and not 0 <= counter < len(num1):
        final = (num2[counter] + carry)%10
        carry = (num2[counter] + carry) // 10
    elif carry > 0 and not 0 <= counter < len(num1) and not 0 <= counter < len(num2):
        final = carry
        carry = carry // 10
    ans.append(final)
    counter+=1

dummy = ListNode(0)
curr = dummy
for i in ans:
    curr.next = ListNode(int(i))
    curr = curr.next
node = dummy.next
while node:
    print(node.val)
    node = node.next