import os
class Methods:
    def __init__(self,game):
         self.o = 1

    def load_wave(self):
            for filename in os.listdir(self.directory):
                with open(os.path.join(self.directory, filename)) as f:
                    tx = f.read()
                    tx = tx.split(" ")
                    game.waves.append(tx)


