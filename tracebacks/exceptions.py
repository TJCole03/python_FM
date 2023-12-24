# try:
#     int('a')
#     d = {'a'}
#     c = []
# except ValueError:
#     print('an exception happened')
# print('end of program')

try:
    d = {'a'}
    c = []
    int('a')
except ValueError:
    print('an exception happened')
except KeyError:
    print('end of program')

# try:
#     int('8')
# except:
#     print('an exception happened')
# print('end of program')