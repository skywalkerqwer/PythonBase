def my_spl(str, spl):
    list_str = []
    index_start = 0
    index_end = 1
    for i in range(len(str)):
        if str[i] != spl:
            index_end += 1
        else:
            index_end -= 1
            list_str.append(str[index_start:index_end])
            index_start = index_end +1
            index_end += 2
    list_str.append(str[index_start:index_end])
    return list_str


a = 'name#age#aaa#123#'
a = my_spl(a, '#')
print(a)
