# # points = [
# #     (1,7),
# #     (4,7),
# #     (6,7),
# #     (1,5),
# #     (4,5),
# #     (6,5),
# #     (3,3),
# #     (1,1),
# #     (4,1)
# # ]
#
# # import time
# num_doc = input()
# set_points = []
#
# for i in range(int(num_doc)):
#     x = input()
#     points = []
#     for j in range(int(x)):
#         s = input().split()
#         points.append((int(s[0]), int(s[1])))
#     set_points.append(set(points))
#
# # start_time = time.time()
# cnt = 0
# for k in range(int(num_doc)):
#     answer = 0
#     l = sorted(list(set_points[k].copy()))
#     #print(l)
#     for i in range(len(l)):
#         for j in range(i + 1, len(l)):
#             cnt += 1;
#             #print(l[i], l[j], 'cnt==', cnt)
#             # print(l[i][0], l[j],'cnt==',cnt)
#             if (l[i][0] < l[j][0] and l[i][1] < l[j][1]):
#                 # print(l[i], l[j],'cnt==',cnt)
#
#                 if ((l[i][0], l[j][1]) in set(set_points[k])) and ((l[j][0], l[i][1]) in set(set_points[k])):
#                     answer = answer + 1
#                     # print(l[i][0], l[j][1])
#                     # print(l[j][0], l[i][1])
#                     #print('Выполн')
#                 #print("---------")
#     print(answer)
# #print('cnt=', cnt)

def find_rects(points, points_index):
    answer = 0
    for i, p1 in enumerate(points):
        for j, p2 in enumerate(points[i + 1:]):
            if (p1[0] == p2[0]) or (p1[1] == p2[1]):
                continue
            p3, p4 = (p1[0], p2[1]), (p2[0], p1[1])

            #print(p1, p2, p3, p4)

            if p3 in points_index and p4 in points_index:
                answer = answer + 1
    return answer // 2


x = int(input())
answers = []

for test_idx in range(x):
    h = int(input())
    points = []
    points_index = set()
    for j in range(int(h)):
        s = input().split()
        point = (int(s[0]), int(s[1]))
        points.append(point)
        points_index.add(point)

    #print(points, points_index)
    answers.append(find_rects(points, points_index))
for ans in answers:
    print(ans)