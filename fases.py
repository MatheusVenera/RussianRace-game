import arcade
import objetos
import config
import telas
import random

# Classe responsável pela fase 2
class Fase2():

    def fase2(self):
        self.movimento_lado_inimigo = 2
# Redefine as posições iniciais novamente
        self.sprite_inimigo.center_x = 45
        self.sprite_inimigo.center_y = 62
        self.sprite_inimigo.change_x = 0
        self.sprite_inimigo.change_y = 0
        self.sprite_personagem.center_x = 450
        self.sprite_personagem.center_y = 62
        self.sprite_personagem.change_x = 0
        self.sprite_personagem.change_y = 0
# Redefine o chão e o teto
        self.lista_chao = None
        self.lista_teto = None
        self.lista_teto = arcade.SpriteList()
        self.lista_chao = arcade.SpriteList()
        self.sprite_teto = objetos.Teto("images/teto_e_chao_2.png", config.ESCALA_CHAO_TETO)
        self.sprite_teto.center_x = 450
        self.sprite_teto.center_y = 645
        self.lista_teto.append(self.sprite_teto)
        self.sprite_chao = objetos.Chao("images/teto_e_chao_2.png", config.ESCALA_CHAO_TETO)
        self.sprite_chao.center_x = 450
        self.sprite_chao.center_y = 15
        self.lista_chao.append(self.sprite_chao)
# Redefine o fundo
        self.fundo = None
        self.fundo = arcade.load_texture("images/fundo.png")
# Define a quantidade de inimigos como 0 para eliminar todos os inimigos que foram gerados anteriormente
        self.quantidade_inimigos = 0
# Reria o inimigo
        self.lista_inimigo = None
        self.lista_inimigo = arcade.SpriteList()
        self.sprite_inimigo = objetos.Enemy("images/inimigo.png", config.ESCALA_INIMIGO)
        self.sprite_inimigo.center_x = 45
        self.sprite_inimigo.center_y = 62
        self.lista_inimigo.append(self.sprite_inimigo)
        self.quantidade_inimigos = 1
# Elimina todos os drops(moedas, sacos e maletas de dinheiro)
        self.lista_moeda = None
        self.lista_saco = None
        self.lista_maleta = None
# Recria os drops
        self.lista_moeda = arcade.SpriteList()
        self.lista_saco = arcade.SpriteList()
        self.lista_maleta = arcade.SpriteList()
        self.sprite_moeda = objetos.Moeda("images/moeda.png", config.ESCALA_MOEDA)
        self.sprite_moeda.center_x = random.randint(1,900)
        self.sprite_moeda.center_y = random.randint(1,660)
        self.sprite_saco = objetos.Saco("images/saco_de_dinheiro.png", config.ESCALA_SACO)
        self.sprite_saco.center_x = random.randint(1,900)
        self.sprite_saco.center_y = random.randint(1,660)
        self.sprite_maleta = objetos.Maleta("images/maleta_de_dinheiro.png", config.ESCALA_MALETA)
        self.sprite_maleta.center_x = random.randint(1,900)
        self.sprite_maleta.center_y = random.randint(1,660)
# Reseta o contador de tempo
        self.tempo = 0
        self.segundos = 0
        self.minutos = 0
        self.contador = "00:00"
# Reseta o placar
        self.placar = 0
# Gera as novas plataformas
        self.lista_plataforma = []
        self.lista_plataforma = arcade.SpriteList()
        self.plataforma_center_x = [225,675,75,450,825,450,150,750]
        self.plataforma_center_y = [135,135,260,250,260,385,510,510]
        for i in range(8):
            if (i == 0) or (i == 1) or (i == 2) or (i == 4):
                self.plataforma_sprite = arcade.Sprite("images/plat225_2.png", config.ESCALA_PLATAFORMA)
            elif (i == 3):
                self.plataforma_sprite = arcade.Sprite("images/plat240_2.png", config.ESCALA_PLATAFORMA)
            elif (i == 5):
                self.plataforma_sprite = arcade.Sprite("images/plat600_2.png", config.ESCALA_PLATAFORMA)
            else:
                self.plataforma_sprite = arcade.Sprite("images/plat300_2.png", config.ESCALA_PLATAFORMA)
            self.plataforma_sprite.center_x = self.plataforma_center_x[i]
            self.plataforma_sprite.center_y = self.plataforma_center_y[i]
            self.lista_plataforma.append(self.plataforma_sprite)

class Fase3():

    def fase3(self):
# Define a velocidade do inimigo maior que a anterior, aumentando a dificuldade
        self.movimento_lado_inimigo = 3
# Redefine as posições iniciais
        self.sprite_inimigo.center_x = 45
        self.sprite_inimigo.center_y = 62
        self.sprite_inimigo.change_x = 0
        self.sprite_inimigo.change_y = 0
        self.sprite_personagem.center_x = 450
        self.sprite_personagem.center_y = 62
        self.sprite_personagem.change_x = 0
        self.sprite_personagem.change_y = 0
# Define a quantidade de inimigos como 0 para eliminar todos os inimigos que foram gerados anteriormente
        self.quantidade_inimigos = 0
# Redefine o chão e o teto
        self.lista_chao = None
        self.lista_teto = None
        self.lista_teto = arcade.SpriteList()
        self.lista_chao = arcade.SpriteList()
        self.sprite_teto = objetos.Teto("images/teto_e_chao_3.png", config.ESCALA_CHAO_TETO)
        self.sprite_teto.center_x = 450
        self.sprite_teto.center_y = 645
        self.lista_teto.append(self.sprite_teto)
        self.sprite_chao = objetos.Chao("images/teto_e_chao_3.png", config.ESCALA_CHAO_TETO)
        self.sprite_chao.center_x = 450
        self.sprite_chao.center_y = 15
        self.lista_chao.append(self.sprite_chao)
# Recria o inimigo
        self.lista_inimigo = None
        self.lista_inimigo = arcade.SpriteList()
        self.sprite_inimigo = objetos.Enemy("images/inimigo.png", config.ESCALA_INIMIGO)
        self.sprite_inimigo.center_x = 45
        self.sprite_inimigo.center_y = 62
        self.lista_inimigo.append(self.sprite_inimigo)
        self.quantidade_inimigos = 1
# Elimina todos os drops
        self.lista_moeda = None
        self.lista_saco = None
        self.lista_maleta = None
# Recria os drops
        self.lista_moeda = arcade.SpriteList()
        self.lista_saco = arcade.SpriteList()
        self.lista_maleta = arcade.SpriteList()
        self.sprite_moeda = objetos.Moeda("images/moeda.png", config.ESCALA_MOEDA)
        self.sprite_moeda.center_x = random.randint(1,900)
        self.sprite_moeda.center_y = random.randint(1,660)
        self.sprite_saco = objetos.Saco("images/saco_de_dinheiro.png", config.ESCALA_SACO)
        self.sprite_saco.center_x = random.randint(1,900)
        self.sprite_saco.center_y = random.randint(1,660)
        self.sprite_maleta = objetos.Maleta("images/maleta_de_dinheiro.png", config.ESCALA_MALETA)
        self.sprite_maleta.center_x = random.randint(1,900)
        self.sprite_maleta.center_y = random.randint(1,660)
# Reseta o contador de tempo
        self.tempo = 0
        self.segundos = 0
        self.minutos = 0
        self.contador = "00:00"
# Reseta o placar
        self.placar = 0
# Gera as plataformas em novas posições
        self.lista_plataforma = []
        self.lista_plataforma = arcade.SpriteList()
        self.plataforma_center_x = [225,675,75,450,825,450,150,750]
        self.plataforma_center_y = [135,135,260,250,260,385,510,510]
        for i in range(8):
            if (i == 0) or (i == 1) or (i == 2) or (i == 4):
                self.plataforma_sprite = arcade.Sprite("images/plat225_3.png", config.ESCALA_PLATAFORMA)
            elif (i == 3):
                self.plataforma_sprite = arcade.Sprite("images/plat240_3.png", config.ESCALA_PLATAFORMA)
            elif (i == 5):
                self.plataforma_sprite = arcade.Sprite("images/plat600_3.png", config.ESCALA_PLATAFORMA)
            else:
                self.plataforma_sprite = arcade.Sprite("images/plat300_3.png", config.ESCALA_PLATAFORMA)
            self.plataforma_sprite.center_x = self.plataforma_center_x[i]
            self.plataforma_sprite.center_y = self.plataforma_center_y[i]
            self.lista_plataforma.append(self.plataforma_sprite)

class Fase4():

    def fase4(self):
# Define a velocidade do inimigo maior que a anterior
        self.movimento_lado_inimigo = 3
# Redefine as posições iniciais
        self.sprite_inimigo.center_x = 45
        self.sprite_inimigo.center_y = 62
        self.sprite_inimigo.change_x = 0
        self.sprite_inimigo.change_y = 0
        self.sprite_personagem.center_x = 450
        self.sprite_personagem.center_y = 62
        self.sprite_personagem.change_x = 0
        self.sprite_personagem.change_y = 0
# Define a quantidade de inimigos como 0 para eliminar todos os inimigos que foram gerados anteriormente
        self.quantidade_inimigos = 0
# Redefine o chão e o teto
        self.lista_chao = None
        self.lista_teto = None
        self.lista_teto = arcade.SpriteList()
        self.lista_chao = arcade.SpriteList()
        self.sprite_teto = objetos.Teto("images/teto_e_chao_4.png", config.ESCALA_CHAO_TETO)
        self.sprite_teto.center_x = 450
        self.sprite_teto.center_y = 645
        self.lista_teto.append(self.sprite_teto)
        self.sprite_chao = objetos.Chao("images/teto_e_chao_4.png", config.ESCALA_CHAO_TETO)
        self.sprite_chao.center_x = 450
        self.sprite_chao.center_y = 15
        self.lista_chao.append(self.sprite_chao)
# Recria o inimigo
        self.lista_inimigo = None
        self.lista_inimigo = arcade.SpriteList()
        self.sprite_inimigo = objetos.Enemy("images/inimigo.png", config.ESCALA_INIMIGO)
        self.sprite_inimigo.center_x = 45
        self.sprite_inimigo.center_y = 62
        self.lista_inimigo.append(self.sprite_inimigo)
        self.quantidade_inimigos = 1
# Elimina todos os drops
        self.lista_moeda = None
        self.lista_saco = None
        self.lista_maleta = None
# Recria os drops
        self.lista_moeda = arcade.SpriteList()
        self.lista_saco = arcade.SpriteList()
        self.lista_maleta = arcade.SpriteList()
        self.sprite_moeda = objetos.Moeda("images/moeda.png", config.ESCALA_MOEDA)
        self.sprite_moeda.center_x = random.randint(1,900)
        self.sprite_moeda.center_y = random.randint(1,660)
        self.sprite_saco = objetos.Saco("images/saco_de_dinheiro.png", config.ESCALA_SACO)
        self.sprite_saco.center_x = random.randint(1,900)
        self.sprite_saco.center_y = random.randint(1,660)
        self.sprite_maleta = objetos.Maleta("images/maleta_de_dinheiro.png", config.ESCALA_MALETA)
        self.sprite_maleta.center_x = random.randint(1,900)
        self.sprite_maleta.center_y = random.randint(1,660)
# Reseta o contador de tempo
        self.tempo = 0
        self.segundos = 0
        self.minutos = 0
        self.contador = "00:00"
# Reseta o placar
        self.placar = 0
# Gera as plataformas em novas posições
        self.lista_plataforma = []
        self.lista_plataforma = arcade.SpriteList()
        self.plataforma_center_x = [225,675,75,450,825,450,150,750]
        self.plataforma_center_y = [135,135,260,250,260,385,510,510]
        for i in range(8):
            if (i == 0) or (i == 1) or (i == 2) or (i == 4):
                self.plataforma_sprite = arcade.Sprite("images/plat225_4.png", config.ESCALA_PLATAFORMA)
            elif (i == 3):
                self.plataforma_sprite = arcade.Sprite("images/plat240_4.png", config.ESCALA_PLATAFORMA)
            elif (i == 5):
                self.plataforma_sprite = arcade.Sprite("images/plat600_4.png", config.ESCALA_PLATAFORMA)
            else:
                self.plataforma_sprite = arcade.Sprite("images/plat300_4.png", config.ESCALA_PLATAFORMA)
            self.plataforma_sprite.center_x = self.plataforma_center_x[i]
            self.plataforma_sprite.center_y = self.plataforma_center_y[i]
            self.lista_plataforma.append(self.plataforma_sprite)