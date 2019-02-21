
def main():
    which_DB = int(input("Which DB do you want to connect to ?"
                     "Enter :\n"
                     "1 for PerfLab\n"
                     "2 for Perf04 - softLayer\n"
                     "3 for StorageLab\n"))

    if(which_DB not in [1,2,3]):
        print("please enter either 1, 2 or 3 as your input")

    else:
        pass
        #call the set of functions here


if __name__ == '__main__':
    main()