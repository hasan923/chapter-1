def print_F():
    for row in range(5):
        for col in range(7):
            if (col==0 or col==1) or (row==0 or row==2):
                print("F",end="")
            else:
                print (end='')
        print()
    print()            

def print_U():
    for row in range(5):
        for col in range(7):
            if((col==0 or col==6) and row<3) or (row==3 and (col==1 or col==5)) or (row==4 and (col>1 and col<5)):
                  print("F",end="")
            else:
                print(end='')
def print_N():
    for row in range(5):
        for col in range(7):
            if((col==0 or col==1 or col==6 or col==7) and (row==col-1)):
                print('N',end='')
            else:
                print(end='')
print_N()