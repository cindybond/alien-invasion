filename = 'high_score.txt'

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start Alien Invasion in an active state
        self.game_active = False

        # high score should never be reset
        self.high_score = self.load_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit  
        self.score = 0
        self.level = 1
    
    def load_high_score(self):
        """Load high score from a file"""
        with open(filename) as f:
            return int(f.read())

    def save_high_score(self):
        """Save high score to a file"""
        with open(filename, 'w') as f:
            f.write(str(self.high_score))