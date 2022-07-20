# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 09:14:30 2022

@author: xiao.chen
"""

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return "->".join(nodes)


if __name__ == '__main__':

    llist = LinkedList()
    print("llist",llist)
    
    first_node = Node("a")
    llist.head = first_node
    print("llist",llist)
    
    second_node = Node("b")
    third_node = Node("c")
    first_node.next = second_node
    second_node.next = third_node
    print("llist",llist)








































