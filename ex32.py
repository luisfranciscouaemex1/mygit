the_count = [1, 2, 3, 4, 5]
2 fruits = ['apples', 'oranges', 'pears', 'apricots']
3 change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
4
5 # this first kind of for- loop goes through a list
www.it-ebooks.info
ptg11539604
LOOPS AND LISTS 107
6 for number in the_count:
7 print "This is count %d" % number
8
9 # same as above
10 for fruit in fruits:
11 print "A fruit of type: %s" % fruit
12
13 # also we can go through mixed lists too
14 # notice we have to use %r since we don't know what's in it
15 for i in change:
16 print "I got %r" % i
17
18 # we can also build lists, first start with an empty one
19 elements = []
20
21 # then use the range function to do 0 to 5 counts
22 for i in range(0, 6):
23 print "Adding %d to the list." % i
24 # append is a function that lists understand
25 elements.append(i)
26
27 # now we can print them out too
28 for i in elements:
29 print "Element was: %d" % i
