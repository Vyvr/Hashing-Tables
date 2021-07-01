from chain_hash_table import ChainTable
from open_hash_table import OpenTable
from random import randint
import matplotlib.pyplot as plt


all_find_elements_present = False
random_elements = True

max_element_number = 1_000_000

chain_table = ChainTable()
open_table = OpenTable()

comparisons_chain_table = []
comparisons_open_table = []

chain_comparision_average = []
open_comparision_average = []

elements_chain_table = []
elements_open_table = []

find_moment = 1
run = 1

chain_sum = 0
open_sum = 0

chain_avg = 0
open_avg = 0

if all_find_elements_present:
    while True:
        run += 1
        val = randint(0, 100000000)

        if not chain_table.find_inside(val) and not open_table.find_inside(val):
            chain_table.insert(val)
            open_table.insert(val)

            chain_comparision_average.append(chain_table.find(val))
            open_comparision_average.append(open_table.find(val))

            if find_moment % 5 == 0:
                print("done")
                for i in chain_comparision_average:
                    chain_sum += i
                for i in open_comparision_average:
                    open_sum += i

                chain_avg = chain_sum/5
                open_avg = open_sum/5

                comparisons_chain_table.append(chain_avg)
                comparisons_open_table.append(open_avg)

                elements_chain_table.append(chain_table.get_element_counter())
                elements_open_table.append(open_table.get_element_counter())

                chain_comparision_average.clear()
                open_comparision_average.clear()

        if chain_table.get_element_counter() != open_table.get_element_counter() or len(comparisons_chain_table) != len(comparisons_open_table):
            print('something went wrong :(')
            break

        if chain_table.get_element_counter() == max_element_number or open_table.get_element_counter() == max_element_number:
            break

        if run % 10_000 == 0:
            print(f'run: {run}')
            print(f'chain elem: {chain_table.get_element_counter()}')
            print(f'open elem: {open_table.get_element_counter()}')
            print()

        find_moment += 1

    plt.title("liczba elementów w słowniku do średniej liczby porównań (wszystkie szukane elementy obecne w tablicach)")
    plt.plot(elements_chain_table, comparisons_chain_table, 'green', label='Chain hash table')
    plt.plot(elements_open_table, comparisons_open_table, 'red', label='Open hash table')
    plt.legend(loc='upper left')
    fig = plt.gcf()
    fig.set_size_inches(16, 9)
    fig.savefig('number_of_elements_to_number_of_comparisons_all_find_elements_present.png', dpi=300)

if random_elements:
    while True:
        run += 1
        val = randint(0, 100000000)

        if not chain_table.find_inside(val) and not open_table.find_inside(val):
            chain_table.insert(val)
            open_table.insert(val)

            rand = randint(0, 1000000)

            chain_comparision_average.append(chain_table.find(rand))
            open_comparision_average.append(open_table.find(rand))

            if find_moment % 5 == 0:
                for i in chain_comparision_average:
                    chain_sum += i
                for i in open_comparision_average:
                    open_sum += i

                chain_avg = chain_sum/5
                open_avg = open_sum/5

                comparisons_chain_table.append(chain_avg)
                comparisons_open_table.append(open_avg)

                elements_chain_table.append(chain_table.get_element_counter())
                elements_open_table.append(open_table.get_element_counter())

                chain_comparision_average.clear()
                open_comparision_average.clear()

        if chain_table.get_element_counter() != open_table.get_element_counter() or len(comparisons_chain_table) != len(comparisons_open_table):
            print('something went wrong :(')
            break

        if chain_table.get_element_counter() == max_element_number or open_table.get_element_counter() == max_element_number:
            break

        if run % 10_000 == 0:
            print(f'run: {run}')
            print(f'chain elem: {chain_table.get_element_counter()}')
            print(f'open elem: {open_table.get_element_counter()}')
            print()

        find_moment += 1

    plt.title("liczba elementów w słowniku do średniej liczby porównań (szukane randomowe elementy)")
    plt.plot(elements_chain_table, comparisons_chain_table, 'green', label='Chain hash table')
    plt.plot(elements_open_table, comparisons_open_table, 'red', label='Open hash table')
    plt.legend(loc='upper left')
    fig = plt.gcf()
    fig.set_size_inches(16, 9)
    fig.savefig('number_of_elements_to_number_of_comparisons_all_find_elements_random.png', dpi=300)