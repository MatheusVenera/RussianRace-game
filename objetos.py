import arcade
import config

# Cria os objetos usados no jogo
class Teto(arcade.Sprite):

    def teto(self):
        self.center_x = None
        self.center_y = None

# Classe chão
class Chao(arcade.Sprite):

    def chao(self):
        self.center_x = None
        self.center_y = None

# Classe moeda
class Moeda(arcade.Sprite):

    def moeda(self):
        self.center_x = None
        self.center_y = None

# Classe saco
class Saco(arcade.Sprite):

    def saco(self):
        self.center_x = None
        self.center_y = None

# Classe maleta
class Maleta(arcade.Sprite):

    def maleta(self):
        self.center_x = None
        self.center_y = None 

# Classe personagem
class Personagem(arcade.Sprite):

    def update(self):
# Movimentação
        self.center_x += self.change_x
        self.center_y += self.change_y

# Colisão com as bordas laterais da tela
        if self.left < 0:
            self.left = 0
        elif self.right > config.LARGURA_TELA:
            self.right = config.LARGURA_TELA


# Classe dos inimigos
class Enemy(arcade.Sprite):

# Movimentação
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

# Colisão com as bordas laterais
        if self.left < -25:
            self.left = -25
        elif self.right > config.LARGURA_TELA + 25:
            self.right = config.LARGURA_TELA + 25