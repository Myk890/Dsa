## Generate Document Problem

def compare_strings(a, b):
    result = True
    if len(a) != len(b):
        print('string lengths do not match!')
    for i, (x, y) in enumerate(zip(a, b)):
        if x != y:
            print(f'char miss-match {x, y} in element {i}')
            result = False
    if result:
        print('strings match!')
    return result
 
 
 
# print(compare_strings("Algo expert !!", " !! trepxe oglA"))
print(compare_strings("Algo expert !!", " !! trepxe oglA"))


