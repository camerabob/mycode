#!/usr/bin/pythom3
# This is a simple example of Python lists (PERL arrays)
# Defining the list
my_list = [ "192.168.0.5", 5060, "UP" ]
# Outputting the elements in the list
print ("The first item in the list (IP): " + my_list[0] )
print ("The second item in the list (port): " + str(my_list[1] ))
print ("The third item in the list (state): " + my_list[2] )
# Create a secone list
new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]
# Print the output as defined in the example
print ("When I " + new_list[5] + " into " + new_list[3] + \
        " or " + new_list[4] + " I am unable to PING ports " + \
        str(new_list[0]) + ", " + str(new_list[1]) + \
        " or " + str(new_list[2] ))
