class Player:
    def __init__(self, name, symbol,time=30):
        self.name = name
        self.symbol = symbol
        self.time=time
        self.score = 0  # Khởi tạo biến tỉ số cho mỗi người chơi

    def increase_score(self):
        self.score += 1

    def get_score(self):
        return self.score
