from collections import deque
# num_doc = input()
#
#
# docs = []
# for i in range(int(num_doc)):
#     tags = []
#     x = input()
#     for j in range(int(x)):
#         tag = input().lower()
#         tags.append(tag)
#     docs.append(tags)
#print(docs)

docs = [
    ['</x>'],
    ['<x>', '<x>', '<x>', '</x>', '</x>'],
    ['<html>', '<biba>', '</biba>', '</aaa>', '</kuka>','</html>'],
    ['<html>', '<tag>', '<button>', '</button>', '<tag>', '</html>'],
    ['<x>', '</y>', '</x>']
]

#print(docs)
for doc in docs:
    stack = deque()
    one_tag = []
    if len(doc) == 1:
        print('ALMOST '+doc[0].upper())
    else:
        for tag in doc:
            #print(tag)
            if tag[1] != '/':
                stack.append(tag)
                #print(stack)
            else:
                if len(stack) != 0:
                    last_elem = stack.pop()
                    if tag.replace('/', '') == last_elem:
                        #print(stack)
                        continue
                    else:
                        one_tag.append(tag)
                        stack.append(last_elem)
                        continue
                else:
                    one_tag.append(tag)
                    continue

        if len(stack) == 0 and len(one_tag) == 0:
            print('CORRECT')
        elif len(stack) == 0 and len(one_tag) == 1:
            print('ALMOST ' + str(one_tag[0]).upper())
        else:
            print('INCORRECT')
        #print('------------')



