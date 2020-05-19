import turtle
import time
 
 
# 清屏函数
def clear_all():
    turtle.penup()
    turtle.goto(0, 0)
    turtle.color('white')
    turtle.pensize(800)
    turtle.pendown()
    turtle.setheading(0)
    turtle.fd(300)
    turtle.bk(600)
 
 
# 重定位海龟的位置
def go_to(x, y, state):
    turtle.pendown() if state else turtle.penup()
    turtle.goto(x, y)
 
 
# 画线
# state为真时海龟回到原点，为假时不回到原来的出发点
def draw_line(length, angle, state):
    turtle.pensize(1)
    turtle.pendown()
    turtle.setheading(angle)
    turtle.fd(length)
    turtle.bk(length) if state else turtle.penup()
    turtle.penup()

# 画爱心
def draw_heart(size):
    turtle.color('palevioletred', 'crimson')
    turtle.pensize(2)
    turtle.pendown()
    turtle.setheading(150)
    turtle.begin_fill()
    turtle.fd(size)
    turtle.circle(size * -3.745, 45)
    turtle.circle(size * -1.431, 165)
    turtle.left(120)
    turtle.circle(size * -1.431, 165)
    turtle.circle(size * -3.745, 45)
    turtle.fd(size)
    turtle.end_fill()
 
# 画出发射爱心的小人
def draw_people(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.pensize(2)
    turtle.color('black')
    turtle.setheading(0)
    turtle.circle(60, 360)
    turtle.penup()
    turtle.setheading(90)
    turtle.fd(75)
    turtle.setheading(180)
    turtle.fd(20)
    turtle.pensize(4)
    turtle.pendown()
    turtle.circle(2, 360)
    turtle.setheading(0)
    turtle.penup()
    turtle.fd(40)
    turtle.pensize(4)
    turtle.pendown()
    turtle.circle(-2, 360)
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(-90)
    turtle.pendown()
    turtle.fd(20)
    turtle.setheading(0)
    turtle.fd(35)
    turtle.setheading(60)
    turtle.fd(10)
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(-90)
    turtle.pendown()
    turtle.fd(40)
    turtle.setheading(0)
    turtle.fd(35)
    turtle.setheading(-60)
    turtle.fd(10)
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(-90)
    turtle.pendown()
    turtle.fd(60)
    turtle.setheading(-135)
    turtle.fd(60)
    turtle.bk(60)
    turtle.setheading(-45)
    turtle.fd(30)
    turtle.setheading(-135)
    turtle.fd(35)
    turtle.penup()
 
 
# 第3个画面，显示文字
def page2():
    turtle.penup()
    turtle.goto(-350, 0)
    turtle.color('mediumvioletred')
    turtle.write('祝母上大人节日快乐啦', font=('宋体', 60, 'normal'))
    time.sleep(3)
 
 
# 第2个画面，显示发射爱心的小人
def page1():
    turtle.speed(10)
    draw_people(-250, 20)
    turtle.penup()
    turtle.goto(-150, -30)
    draw_heart(14)
    turtle.penup()
    turtle.goto(-20, -60)
    draw_heart(25)
    turtle.penup()
    turtle.goto(250, -100)
    draw_heart(45)
    turtle.hideturtle()
    time.sleep(3)

def page0():
# 设置初始位置
    turtle.penup()  # 提起画笔
    turtle.left(90)  # 逆时针旋转九十度
    turtle.fd(200)  # 向前移动一段距离 fd=forward
    turtle.pendown()  # 放下画笔移动画笔开始绘制
    turtle.right(90)   # 顺时针旋转九十度

    # 花蕊
    turtle.fillcolor("crimson")  # 填充颜色
    turtle.begin_fill()  # 开始填充
    turtle.circle(10, 180)  # 画一圆，10是半径，180是弧度
    turtle.circle(25, 110)
    turtle.left(50)
    turtle.circle(60, 45)
    turtle.circle(20, 170)
    turtle.right(24)
    turtle.fd(30)
    turtle.left(10)
    turtle.circle(30, 110)
    turtle.fd(20)
    turtle.left(40)
    turtle.circle(90, 70)
    turtle.circle(30, 150)
    turtle.right(30)
    turtle.fd(15)
    turtle.circle(80, 90)
    turtle.left(15)
    turtle.fd(45)
    turtle.right(165)
    turtle.fd(20)
    turtle.left(155)
    turtle.circle(150, 80)
    turtle.left(50)
    turtle.circle(150, 90)
    turtle.end_fill()  # 结束填充

# 花瓣1
    turtle.left(150)
    turtle.circle(-90, 70)
    turtle.left(20)
    turtle.circle(75, 105)
    turtle.setheading(60)  # urtle.setheading(angle) 或 turtle.seth(angle):改变行进方向 angle:行进方向的绝对角度，可以为负值
    turtle.circle(80, 98)
    turtle.circle(-90, 40)

# 花瓣2
    turtle.left(180)
    turtle.circle(90, 40)
    turtle.circle(-80, 98)
    turtle.setheading(-83)

# 叶子1
    turtle.fd(30)
    turtle.left(90)
    turtle.fd(25)
    turtle.left(45)
    turtle.fillcolor("forestgreen")
    turtle.begin_fill()
    turtle.circle(-80, 90)
    turtle.right(90)
    turtle.circle(-80, 90)
    turtle.end_fill()

    turtle.right(135)
    turtle.fd(60)
    turtle.left(180)
    turtle.fd(85)
    turtle.left(90)
    turtle.fd(80)

# 叶子2
    turtle.right(90)
    turtle.right(45)
    turtle.fillcolor("forestgreen")
    turtle.begin_fill()
    turtle.circle(80, 90)
    turtle.left(90)
    turtle.circle(80, 90)
    turtle.end_fill()

    turtle.left(135)
    turtle.fd(60)
    turtle.left(180)
    turtle.fd(60)
    turtle.right(90)
    turtle.circle(200, 60)

def main():
    turtle.setup(900, 500)
    page0()
    clear_all()
    page1()
    clear_all()
    page2()
    turtle.done()
 
 
main()
