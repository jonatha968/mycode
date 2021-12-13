#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   List - simple list"""

def main():
    # create a list called list1
    list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]

    # display list1
    print(list1)

    #display list[1] which shoud only display arista_eos
    print(list1[1])
    
    #create a new list containing a single item
    list2=["juniper"]

    #extend list1 and list2 (combin both lists together into a single list)
    list1.extend(list2)

    #dislay list1, which noew contains list two
    print(list1)
    
    #create list3
    list3=["10.1.0.1", "10.2.0.1", "10.3.01.1"]

    #use the append operation to append list1 by list3
    list1.append(list3)

    #display the new complex list1
    print(list1)

main()

