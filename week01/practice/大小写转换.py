str_in = input("输入字符串")
str_out = ""
for i in str_in:
    if 65 <= ord(i) <= 90:
        str_out += chr(ord(i) + 32)
        continue
    if 97 <= ord(i) <= 122:
        str_out += chr(ord(i) - 32)
        continue
    else:
        str_out += i
print(str_out)