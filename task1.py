a = 1
b = 1.1
c = "hello"
d = ["acd", "123"]
x = ("b", "3")
y = {"russia : moscow"}

spisok = [a, b, c, d, x, y]
for i in spisok:
    print(f'{i}  {type(i)}')