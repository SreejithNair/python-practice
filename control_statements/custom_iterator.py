#implement custom iterator

class Library:

    books = ['harry poter','Mahathma', 'Bhagavath Geetha', 'Ramayan','Jackpot','Red Sea','Mission']
    def __init__(self,maximum_can_borrow=6):
        self.maximum_can_borrow=maximum_can_borrow
    
    def __iter__(self):
        self.start_index=0
        return self

    def __next__(self):
        #store the current position to a local variable
        current_position = self.start_index

        #stop iteration when current limit reach
        if current_position > self.maximum_can_borrow:
            raise StopIteration
        self.start_index += 1
        return Library.books[current_position]

lib = Library()
for b in lib:
    print(b)
    