import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor('orange')

    brad = turtle.Turtle()
    turtle.shape('circle')
    turtle.color('green')
    turtle.speed(1)

    for i in range(36):
        num = 0
        while num <=3:
            brad.forward(100)
            brad.right(90)
            num +=1

        brad.right(10)
        
        

    

    #time = draw_sqaure()
    #for i in time:
        #brad.right(10)
    
    


       
    #angie = turtle.Turtle()
    #angie.circle(100)
    #angie.shape('arrow')
    #angie.color('blue')

    #tody = turtle.Turtle()
    #tody.shape('triangle')
    #tody.color('green')
    #num = 0
    #while num <=2:
        #tody.forward(100)
        #tody.left(120)
        #num +=1
        

    
    
    

draw_square()
time()

