# khi tạo 2 biến có cùng giá trị, chúng cùng trỏ tới 1 obj
x = 2
y = 2
# ===> chúng có cùng id


# sau khi gán giá trị mới cho biến, python tạo ra obj mới
x = 2 
x = 3
# ===> khác id


# truyền 
a = {'a': 123}

def change(x):
    x['a'] = 11
    return x

change(a)
print(a)

