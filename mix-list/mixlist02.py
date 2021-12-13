#1/usr/bin/env python3

#Create a varioable for my list

iplist=[5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh"]

#display the virst vlaue
#drint("The first item in the list (IP): "+ my_list[])

#display the second value
#print("The second item in the list (port): " + str(my_list[1]) )

#dis0play the third item
#print("The last item in the list (state): " + my_list[2] )

# example 1 - add up the strings
print("IP addresses: " + iplist[3] + ", and " + iplist[4])

# example 2 - use the comma separator
print("IP addresses:", iplist[3], ", and", iplist[4])

# example 3 - use an 'f-string'
print(f"IP addresses: {iplist[3]}, and {iplist[4]}")
