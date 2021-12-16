#!/usr/bin/env python3

#create a list of strings

vendors=["cisco", "juniper", "big_ip", "F5", "Arista", "Alta3", "Zach", "Stuart"]

approved_vendors=["cisco", "juniper", "big_ip"]

for x in vendors:
    print("\nThe vendor is "+x, end="") 
    if x not in approved_vendors:
        print(" - NOT AN APPROVED VENDOR!", end="")

print("\nOut loop has ended,") 

