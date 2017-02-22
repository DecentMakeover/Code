class Parent():
    def __init__(self,last_name,eye_color):
        self.last_name = last_name
        self.color = eye_color


ryan_dsouza = Parent('dsouza', 'blue')
print (ryan_dsouza.last_name)


class Child(Parent):
    def __init__(self,last_name,eye_color,number_of_toys):
        Parent.__init__(self,last_name,eye_color)
        self.number_of_toys = number_of_toys


miley_cyrus = Child('cyrus', 'blue',10)
print (miley_cyrus.number_of_toys)
