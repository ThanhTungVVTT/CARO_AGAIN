class Player:
    '''
    Lớp Player đại diện cho một người chơi trong trò chơi
    '''
    def __init__(self, name, symbol,time=30):
        '''
        Khởi tạo người chơi với tên, kí hiệu, thời gian chơi và điểm số mặc định là 0
        '''
        self.name = name
        self.symbol = symbol
        self.time=time
        self.score = 0 



