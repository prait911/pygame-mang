
class GameStats():
    """Check game statistics"""
    
    def __init__(self):
        """initsialitseerida statistika"""
        self.game_active = False
        self.reset_stats()
        
        
    def reset_stats(self):
        """initsialitseerida skoor, mida näitab mängu ajal"""
        self.score = 0
        self.level = 1
        self.bonus = 0