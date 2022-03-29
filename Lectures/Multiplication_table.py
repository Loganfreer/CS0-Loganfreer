def print_table(table_size):
    print(f"{'':>4}", end = '')
    for i in range(table_size):
        print(f"{i+1:>4}", end = '')
    print("")
    for i in range(table_size+1):
            print(f"----", end = '')
    print("")
    for i in range(table_size):
        print(f"{i+1:<4}", end='')
        for k in range(table_size):
            print(f"{(k+1)*(i+1):>4}", end='')
        print('')

def input_size():
    size_of_table = int(input('Please enter size of multiplication table to print: '))
    
    return size_of_table
def main():
    size_of_table = input_size()
    print_table(size_of_table)


main()