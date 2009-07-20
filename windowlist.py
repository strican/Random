__FIRST = 0
__LAST = 100

##Test for the tail
def tailTest(list):
    tailtest = False
    for x in list:
        if x > __LAST:
            tailtest = True
    return tailtest

##Test for the head
def headTest(list):
    headtest = False
    for x in list:
        if x < __FIRST:
            headtest = True
    return headtest

def main():
    window = int(input("Window = "))
    overlap = int(input("Overlap = "))
    head = bool(int(input("head: 0/1 = ")))
    tail = bool(int(input("tail: 0/1 = ")))
    init = 0
    end = 101
    count = 0
    last = []

    #Define range according to presence of head and tail
    if head:
        init -= window
    if not tail:
        end -= window

    for i in range(init, end, window - overlap):
        list = [x for x in range(i,i + window)]

        #Booleans to determine the head and tail
        tailtest = tailTest(list)
        headtest = headTest(list)

        if not headtest and not tailtest:
            print list
            last = list

            #Print the head
            if count != 0:
                for i in range(0,count):
                    print list
                count = 0
                
        #Keeps track of how many times the first valid list is printed for the head        
        elif headtest:
            count += 1

        #Prints the last valid list each time the tail is not in the range    
        elif tailtest:
            print last


if __name__ == "__main__":
   main() 
