"""definition of chain hash table"""
import sys


class ChainTable:
    def __init__(self):
        self.capacity = 10
        self.element_counter = 0
        self.tab = [None] * self.capacity
        i = 0
        while i < self.capacity:
            self.tab[i] = []
            i += 1

    def hash_fun(self, val):
        return val % self.capacity

    def print(self):
        for i in range(0, len(self.tab)):
            print(f"{i}: {self.tab[i]}")

    def insert(self, val):
        # checking if rehash needed
        if (self.element_counter/self.capacity) > 7.5:
            self.rehash('UP')

        # insert
        modulo = self.hash_fun(val)

        if self.find_inside(val):
            return

        if modulo < self.capacity:
            self.tab[modulo].append(val)
            self.element_counter += 1
            return
        else:
            print("No key found in hash-chain table, insert function")
            return

    def find(self, arg):
        modulo = self.hash_fun(arg)

        comparisons = 0
        for v in self.tab[modulo]:
            comparisons += 1
            if v == arg:
               # print(f"{arg} found by hash-chain table!")
                return comparisons

       # print(f"{arg} NOT found by hash-chain table")
        return comparisons

    def find_inside(self, arg):
        modulo = self.hash_fun(arg)
        for v in self.tab[modulo]:
            if v == arg:
                return True
        return False

    def delete(self, arg):
        # checking if rehash needed
        counter = 0
        for t in self.tab:
            for _ in t:
                counter += 1

        if (counter/self.capacity) < 0.3:
            self.rehash('DOWN')

        # delete
        modulo = self.hash_fun(arg)

        if arg in self.tab[modulo]:
            self.tab[modulo].remove(arg)
            self.element_counter -= 1
           # print(f"value {arg} deleted from hash-chain table")
            return

      #  print(f"{arg} NOT found and NOT deleted by hash-chain table")
        return

    def rehash(self, resize):
        temp_tab = []
        # rewrite all values from chain_hash table to temporary table
        for t in self.tab:
            for val in t:
                temp_tab.append(val)

        # set new capacity of chain_hash table
        if resize == 'UP':
            self.capacity = int((self.capacity * 120) / 100)
            self.tab = [None] * self.capacity
        elif resize == 'DOWN':
            new_capacity = int((self.capacity * 70) / 100)
            if new_capacity >= 10:
                self.capacity = new_capacity
                self.tab = [None] * self.capacity
        else:
            sys.exit('fun resize: Wrong argument.')
        i = 0
        while i < self.capacity:
            self.tab[i] = []
            i += 1

        # rewrite values from temporary table to chain_hash table
        self.element_counter = 0
        for val in temp_tab:
            self.insert(val)

    def get_element_counter(self):
        return self.element_counter
