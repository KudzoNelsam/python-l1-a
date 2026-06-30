l = 4
c = 13
#
# for i in range(l):
#     for j in range(c):
#         print('*', end='')
#     print()
#
# print('********** Version Plus Courte **********')
# for i in range(l):
#     print('*'*c)
#


for i in range(l):
    for j in range(c):
        if      ((i == 0) or
                (i == l -1) or
                ((i != 0 and i != l-1) and (j==0 or j==c-1))):
            print('*', end='')
        else:
            print(' ', end='')
    print()