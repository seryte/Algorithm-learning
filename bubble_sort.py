def bubble_sort(target_list):
    """
    暴力排序O平方
    :param target_list:
    :return:
    """
    ret = target_list.copy()
    for i in range(len(ret) - 1):
        print("外循环i: ", target_list[i])
        for j in range(len(ret) - i - 1):
            print("j: ", target_list[j])
            if ret[j] > ret[j + 1]:
                ret[j], ret[j + 1] = ret[j + 1], ret[j]
        print(ret)
    return ret


target_list = [5, 8, 6, 3, 9, 2, 1, 7]
r = bubble_sort(target_list)
print(r)
