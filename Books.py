class Book:
    
    def __init__(self, title, author, length, genre):
        self.title = title
        self.author = author
        self.length = length
        self.genre = genre

    # def set_length(self, length):
    #     if length > 0:
    #         self.length = length
    #     # else:
    #     #     dont create and show error