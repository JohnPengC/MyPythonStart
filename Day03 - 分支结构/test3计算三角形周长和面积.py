a=float(input('第一条边的长度：'))
b=float(input('第二条边的长度：'))
c=float(input('第三条边的长度：'))
if a+b>c and a+c>b and b+c>a :
    print('周长: %f' % (a + b + c))
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('面积: %f' % (area))
else:
    print('不能构成三角形')
