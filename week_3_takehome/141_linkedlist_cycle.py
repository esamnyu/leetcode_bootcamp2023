import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def has_cycle(head):
    """
    Check if the linked list has a cycle.
    """
    if not head:
        return False
    
    slow, fast = head, head
    
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    return False

def visualize_linked_list(head):
    """
    Visualize the linked list and highlight the nodes where slow and fast pointers are pointing.
    """
    fig, ax = plt.subplots()
    
    # Initial positions
    x, y = 0, 0
    slow, fast = head, head
    ax.set_xlim(-1, 10)
    ax.set_ylim(-1, 2)
    
    nodes = []
    while head:
        ax.add_patch(patches.Circle((x, y), radius=0.4, fill=True))
        ax.text(x, y, str(head.value), ha="center", va="center", color="white")
        
        nodes.append((x, y, head))
        head = head.next
        x += 2
    
    for x, y, node in nodes:
        if node.next:
            next_x = x + 2
            ax.arrow(x + 0.4, y, 1.2, 0, head_width=0.2, head_length=0.2, fc='k', ec='k')
    
    plt.show()

# Sample linked list with a cycle
node1 = Node(3)
node2 = Node(2)
node3 = Node(0)
node4 = Node(-4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # create a cycle

# Check for cycle
print(has_cycle(node1))  # This should print True

# Visualize
visualize_linked_list(node1)
