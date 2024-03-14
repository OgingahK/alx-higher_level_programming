#!/usr/bin/python3
def add_args(argv):
   i = len(argv) - 1
   if i == 0:
       print("{:d}".format(i))
       return
   else:
       x = 1
       add = 0
       while x <= i:
           add += int(argv[x])
           x += 1
           print("{:d}".format(add))

if __name__=="__main__":
    import sys
    add_args(sys.argv)
