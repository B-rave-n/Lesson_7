def second_index(text, some_str):
    if text.count(some_str) > 1:
        index = 0
        for i in range(2):
            text[index:].index(some_str)
            index_1 = index
            index = text[index:].index(some_str)+1
        return (index-1+index_1)
    else:
        return



assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')