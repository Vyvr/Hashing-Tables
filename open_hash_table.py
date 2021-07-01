"""definition of open hash table"""
import re
import sys


class OpenTable:
    def __init__(self):
        self.capacity = 10
        self.element_counter = 0
        self.tab = [None] * self.capacity
        self.move = 0
        i = 0
        while i < self.capacity:
            self.tab[i] = None
            i += 1

    def hash_fun(self, val):
        return (val + self.move) % self.capacity

    def print(self):
        for i in range(0, len(self.tab)):
            print(re.sub('None|-1', '', f"{i}: {self.tab[i]}"))

    def insert(self, val):
        # checking if rehash needed
        if self.element_counter/self.capacity > 0.7:
            self.rehash('UP')

        #insert
        modulo = self.hash_fun(val)
        if self.find_inside(val):
            return

        if self.tab[modulo] == -1 or self.tab[modulo] is None:
            self.tab[modulo] = val
            self.element_counter += 1
            return
        else:
            while True:
                self.move += 1
                modulo = self.hash_fun(val)
                if self.tab[modulo] == -1 or self.tab[modulo] is None:
                    self.tab[modulo] = val
                    self.move = 0
                    self.element_counter += 1
                    return
                if self.move == self.capacity - 1:
                    # print("open-hash table is full. Can't insert new value")
                    self.move = 0
                    return

    def find(self, val):
        modulo = self.hash_fun(val)

        comparisons = 1
        if self.tab[modulo] == val:
            # print(f"{val} found by open-hash table!")
            return comparisons

        while True:
            self.move += 1
            modulo = self.hash_fun(val)
            comparisons += 1
            if self.tab[modulo] == val:
                # print(f"{val} found by open-hash table!")
                self.move = 0
                return comparisons
            elif self.tab[modulo] is None or self.move == self.capacity - 1:
                # print(f"{val} NOT found by open-hash table!")
                self.move = 0
                return comparisons

    def find_inside(self, val):
        modulo = self.hash_fun(val)

        if self.tab[modulo] == val:
            return True

        while True:
            self.move += 1
            modulo = self.hash_fun(val)
            if self.tab[modulo] == val:
                self.move = 0
                return True
            elif self.tab[modulo] is None or self.move == self.capacity - 1:
                self.move = 0
                return False

    def delete(self, val):
        if self.capacity == 0:
            return

        # checking if rehash needed
        if self.element_counter/self.capacity < 0.3:
            self.rehash('DOWN')

        # delete
        modulo = self.hash_fun(val)

        if self.tab[modulo] == val:
            self.tab[modulo] = -1
            self.element_counter -= 1
            # print(f"{val} deleted by open-hash table!")
            return
        elif self.element_counter > 1:
            while True:
                self.move += 1
                modulo = self.hash_fun(val)
                if self.tab[modulo] == val:
                    self.tab[modulo] = -1
                    self.element_counter -= 1
                    # print(f"{val} deleted by open-hash table!")
                    self.move = 0
                    return
                elif self.tab[modulo] is None or self.move == self.capacity - 1:
                    # print(f"{val} NOT found and NOT deleted by open-hash table!")
                    self.move = 0
                    return

    def rehash(self, resize):
        temp_tab = []
        # rewrite all values from chain_hash table to temporary table
        for t in self.tab:
            if t is not None:
                temp_tab.append(t)

        # set new capacity of chain_hash table
        if resize == 'UP':
            self.capacity = int((self.capacity * 150) / 100)
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
            self.tab[i] = None
            i += 1

        # rewrite values from temporary table to chain_hash table
        self.element_counter = 0
        for val in temp_tab:
            self.insert(val)

    def get_element_counter(self):
        return self.element_counter
