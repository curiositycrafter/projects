class node:
    def __init__(self,val):
        self.prev=None
        self.val=val
        self.next=None
def printt(n):
    while n.next:
        print(n.val,end='->')
        n=n.next
    print(n.val)
def printt2(n):
    while n.prev:
        print(n.val,end='->')
        n=n.prev
    print(n.val)    
n1=node(1)
n2=node(2)
n3=node(3)
n4=node(4)
n5=node(5)
n5.prev,n2.prev,n3.prev,n4.prev=n4,n1,n2,n3
n1.next,n2.next,n3.next,n4.next=n2,n3,n4,n5
printt(n1)
printt2(n5)
