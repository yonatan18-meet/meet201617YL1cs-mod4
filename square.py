from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self,length):
        super(Square,self).__init__(length,length)
        #square_instance = Square(length)

    def set_length(self,length):
        super().set_length(length)
        super().set_height(length)

