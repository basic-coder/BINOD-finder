import os

def isBinod(filename):
    with open(filename,"r") as f:
        fileContent = f.read()

    #detect all forms
    if "binod" in fileContent.lower():
        return True
    else:
        return False


if __name__ == "__main__":
    #listing the content of this folder
    dir_cont = os.listdir()
    #
    # print(dir_cont)

    nBinod = 0
    #for each text file run isBinod function
    for item in dir_cont:
        if item.endswith('.txt'):
            print(f"dectecting Binod in {item}")
            flag = isBinod(item)
            if (flag):
                print(f"binod found in {item}")
                nBinod+=1
            else:
                print(f"binod not found {item}")


    print("Binod detector summary")
    print(f"{nBinod} files found ")