def main():
    nums = []
    #fin = open("output_file.txt", mode = 'w')
    #fin.write("This is how you create a new file and write in it from python\n")
    #fin.write(f"2 + 5 = {2+5}\n")
    with open("myfile.txt") as fin:
        data = fin.readlines()
        for line in data:
            nums.append(int(line.strip()))
        print(f'{nums}')
    #data = fin.readlines()
    #for line in data:
        #print(f'{line.strip}')
        #nums.append(int(line.strip()))

    #print(f'{nums}')
    fin.close()


if __name__ == "__main__":
    main()