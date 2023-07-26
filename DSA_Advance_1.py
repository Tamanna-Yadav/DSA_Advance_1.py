# 1. Delete the elements in an linked list whose sum is equal to zero
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def delete_zero_sum(head):
    current = head
    sum_list = 0
    while current:
        sum_list += current.data
        current = current.next

    if sum_list == 0:
   
        return None
    current = head
    while current:
        temp = current.next
        temp_sum = current.data
        while temp:
            temp_sum += temp.data
            if temp_sum == 0:
              
                current.next = temp.next
                break
            temp = temp.next
        current = current.next

    return head
def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()
head = Node(6)
head.next = Node(-6)
head.next.next = Node(8)
head.next.next.next = Node(4)
head.next.next.next.next = Node(-12)
head.next.next.next.next.next = Node(9)
print("Original Linked List:")
print_linked_list(head)
head = delete_zero_sum(head)
print("Modified Linked List:")
print_linked_list(head)

# 2. Reverse a linked list in groups of given size.

class node:
    def __init__(self,data):
        self.data = data
        self.next = None
def reverse_in_groups(head,n):
    current = head
    next_node = None
    prev = None
    count = 0
    while current and count < n:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
        count += 1
    if next_node:
        head.next = reverse_in_groups(next_node,n)
    return prev
def print_linked_list(head):
    current = head
    while current:
        print(current.data ,end = " ")
        current = current.next
    print()
head = node(1)
head.next = node(2)
head.next.next = node(3)
head.next.next.next = node(4)
head.next.next.next.next = node(5)
head.next.next.next.next.next = node(6)
head.next.next.next.next.next.next = node(7)
head.next.next.next.next.next.next.next = node(8)
head.next.next.next.next.next.next.next.next = node(9)
head.next.next.next.next.next.next.next.next.next = node(10)
print('orginal linked list')
print_linked_list(head)

n = 3
head = reverse_in_groups(head, n)

print('modified linked list!')
print_linked_list(head)

# 3. Merge a linked list into another linked list at alternate positions.

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = Node(data)

    def merge_alternate(self, other):
        curr1 = self.head
        curr2 = other.head
        while curr1 and curr2:
            temp = curr1.next
            curr1.next = curr2
            curr2 = curr2.next
            curr1.next.next = temp
            curr1 = temp

        other.head = curr2

    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=' ')
            curr = curr.next

# Example usage
l1 = LinkedList()
l2 = LinkedList()

l1.insert(1)
l1.insert(3)
l1.insert(5)
l2.insert(2)
l2.insert(4)
l2.insert(6)

l1.merge_alternate(l2)
l1.display()

# 4. In an array, Count Pairs with given sum

def count_pairs(arr, target):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                count += 1
    return count


arr = [1, 5, 3, 7, 2]
target = 8
print(count_pairs(arr, target))

# 5. Find duplicates in an array.

arr = [1, 2, 3, 4, 2, 7, 8, 8, 3];     
     
print("Duplicate elements in given array: ");    
#Searches for duplicate element    
for i in range(0, len(arr)):    
    for j in range(i+1, len(arr)):    
        if(arr[i] == arr[j]):    
            print(arr[j]);

# 6. Find the Kth largest and Kth smallest number in an array

def kth_largest_smallest(arr, k):
def kth_largest_smallest(arr, k):
    arr.sort()
    return arr[k-1], arr[-k]

# Example usage
arr = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input("Enter element: "))
    arr.append(ele)
k = int(input("Enter the value of k: "))
kth_largest, kth_smallest = kth_largest_smallest(arr, k)
print(f"The {k}th largest number is {kth_largest}")
print(f"The {k}th smallest number is {kth_smallest}")

# 7. Move all the negative elements to one side of the array

def shift_negative_values(arr):
    left = 0
    right = len(arr)- 1
    while left <= right:
        if arr[left]<0 and arr[right] < 0:
            left += 1
        elif arr[left]>=0 and arr[right]<0:
            arr[left],arr[right] = arr[right],arr[left]
            left += 1
            right -= 1
        elif arr[left]>=0 and arr[right]>=0:
            right -= 1
        else:
            left += 1
            right -= 1
    return arr
array = list(map(int,input('enter the list of array:').split()))
result = shift_negative_values(array)
print('modified array with negative elements shifted to one side:')
print(result)

# 8. Reverse a string using a stack data structure.
def reverse_string(string):
    stack = []
    for char in string:
        stack.append(char)
    reverse = ""
    while len(stack) > 0:
        reverse += stack.pop()
    return reverse

# Example usage
string = input("Enter a string to reverse: ")
print(f"The reversed string is: {reverse_string(string)}")

# 9. Evaluate a postfix expression using stack.

def evaluate_postfix(expression):
    stack = []
    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = perform_operation(char, operand1, operand2)
            stack.append(result)
    return stack.pop()

def perform_operation(operator, operand1, operand2):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 / operand2

# Example usage
expression = input("Enter postfix expression: ")
result = evaluate_postfix(expression)
print("Result: ", result)

# 10. Implement a queue using the stack data structure.

class Queue:
    def _init_(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, value):
        self.stack1.append(value)

    def dequeue(self):
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return "Queue is empty"
        elif len(self.stack2) == 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

queue = Queue()

while True:
    choice = input("Enter 1 to enqueue, 2 to dequeue, and 3 to exit: ")
    if choice == "1":
        value = input("Enter a value to enqueue: ")
        queue.enqueue(value)
    elif choice == "2":
        value = queue.dequeue()
        print(f"Dequeued value: {value}")
    elif choice == "3":
        break
    else:
        print("Invalid choice")