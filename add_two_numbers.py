'''You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.'''

class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

def addTwoNumbers(l1,l2):
    #l1 and l2 are linked list
    n1 = build_num(l1)
    n2 = build_num(l2)
    n3 = list(str(n1+n2))#make a list of the sum of n1 and n2
    head = ListNode(n3[len(n3)-1])
    curr = head
    #create linked nodes in reverse
    for i in range(len(n3)-2,-1,-1):
        next = ListNode(n3[i])
        curr.next = next
        curr = next
    return head

def build_num(ll):
    #conver the linked node into an int
    degree = 1
    node = ll
    number = 0
    while node != None:
        number = number + (node.val*degree)
        degree = degree * 10
        node = node.next
    return(number)

def make_ll(li):
    ll_li = [ListNode(x) for x in li]
    head = ll_li[0]
    curr = head
    for node in ll_li[1:]:
        curr.next = node
        curr = node
    return head
def main():
    x = make_ll([2,4,3])
    y = make_ll([5,6,4])
    z = addTwoNumbers(x,y)
    node = z
    while node != None:
        print(node.val)
        node = node.next
if __name__ == '__main__':
    main()