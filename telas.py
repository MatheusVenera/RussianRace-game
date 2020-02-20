import arcade
import config
import objetos
import random

# Classe ajuda
class Ajuda():

# Atualiza a página da ajuda
    def ajuda(self):
        if self.ajuda_contagem == 2:
            self.tela = None
            self.tela = arcade.load_texture("images/ajuda_ajuda.png")
            arcade.draw_texture_rectangle(config.LARGURA_TELA // 2, config.ALTURA_TELA // 2,config.LARGURA_TELA, config.ALTURA_TELA, self.tela)
        elif self.ajuda_contagem == 3:
            self.tela = None
            self.tela = arcade.load_texture("images/ajuda_teclas.png")
            arcade.draw_texture_rectangle(config.LARGURA_TELA // 2, config.ALTURA_TELA // 2,config.LARGURA_TELA, config.ALTURA_TELA, self.tela)
        elif self.ajuda_contagem == 4:
            self.tela = None
            self.tela = arcade.load_texture("images/ajuda_desc.png")
            arcade.draw_texture_rectangle(config.LARGURA_TELA // 2, config.ALTURA_TELA // 2,config.LARGURA_TELA, config.ALTURA_TELA, self.tela)
        elif self.ajuda_contagem == 5:
            self.tela = None
            self.tela = arcade.load_texture("images/ajuda_objetos.png")
            arcade.draw_texture_rectangle(config.LARGURA_TELA // 2, config.ALTURA_TELA // 2,config.LARGURA_TELA, config.ALTURA_TELA, self.tela)
        elif self.ajuda_contagem == 6:
            self.tela = None
            self.tela = arcade.load_texture("images/ajuda_tela.png")
            arcade.draw_texture_rectangle(config.LARGURA_TELA // 2, config.ALTURA_TELA // 2,config.LARGURA_TELA, config.ALTURA_TELA, self.tela)
        elif self.ajuda_contagem == 7:
            self.tela = None
            self.tela = arcade.load_texture("images/ajuda_2_jogadores.png")
            arcade.draw_texture_rectangle(config.LARGURA_TELA // 2, config.ALTURA_TELA // 2,config.LARGURA_TELA, config.ALTURA_TELA, self.tela)
        elif self.ajuda_contagem == 8:
            self.tela = None
            self.tela = arcade.load_texture("images/ajuda_teclas_2_jogadores.png")
            arcade.draw_texture_rectangle(config.LARGURA_TELA // 2, config.ALTURA_TELA // 2,config.LARGURA_TELA, config.ALTURA_TELA, self.tela)
        elif self.ajuda_contagem > 8:
            self.ajuda = False
            self.menu_principal = True
            self.ajuda_contagem = 1

# Classe da vitória do jogo
class GameWin():

# Reseta para os valores iniciais, caso o jogador queira reiniciar o jogo
    def game_win(self):
        self.vidas = 3
        self.lista_vidas = None
        self.lista_vidas = arcade.SpriteList()
        posicao_x = 885
        for i in range(3):
            self.sprite_vida = arcade.Sprite("images/cabeca_personagem.png", 0.25)
            self.sprite_vida.center_x = posicao_x
            self.sprite_vida.center_y = 645
            self.lista_vidas.append(self.sprite_vida)
            posicao_x += -30
        self.call_contreg = False
        self.reg_tempo = 0
        self.reg_segundos = 3
        self.change_level = False
        self.draw_cont = False
        self.cont_tempo = True
        self.laugh = 1
        if self.modo_2_jogadores == False:
            self.tela = None
            self.tela = arcade.load_texture("images/tela_game_win.png")
            arcade.draw_texture_rectangle(config.LARGURA_TELA // 2, config.ALTURA_TELA // 2,config.LARGURA_TELA, config.ALTURA_TELA, self.tela)
        elif self.modo_2_jogadores == True:
            self.tela = None
            self.tela = arcade.load_texture("images/player_1_won.png")
            arcade.draw_texture_rectangle(config.LARGURA_TELA // 2, config.ALTURA_TELA // 2,config.LARGURA_TELA, config.ALTURA_TELA, self.tela)
        self.change_level = False
        self.draw_cont = False
        self.call_contreg = False
        self.movimento_lado_inimigo = 2
        self.sprite_inimigo.center_x = 45
        self.sprite_inimigo.center_y = 62
        self.sprite_inimigo.change_x = 0
        self.sprite_inimigo.change_y = 0
        self.sprite_personagem.center_x = 450
        self.sprite_personagem.center_y = 62
        self.sprite_personagem.change_x = 0
        self.sprite_personagem.change_y = 0
        self.quantidade_inimigos = 0
        self.lista_inimigo = None
        self.lista_inimigo = arcade.SpriteList()
        self.sprite_inimigo = objetos.Enemy("images/inimigo.png", config.ESCALA_INIMIGO)
        self.sprite_inimigo.center_x = 45
        self.sprite_inimigo.center_y = 62
        self.lista_inimigo.append(self.sprite_inimigo)
        self.quantidade_inimigos = 1
        self.lista_moeda = None
        self.lista_saco = None
        self.lista_maleta = None
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
        self.tempo = 0
        self.segundos = 0
        self.minutos = 0
        self.contador = "00:00"
        self.reg_contador == "3"
        self.placar = 0
        self.fase = 1
        self.lista_plataforma = []
        self.lista_plataforma = arcade.SpriteList()
        self.plataforma_center_x = [225,675,75,450,825,450,150,750]
        self.plataforma_center_y = [135,135,260,250,260,385,510,510]
        for i in range(8):
            if (i == 0) or (i == 1) or (i == 2) or (i == 4):
                self.plataforma_sprite = arcade.Sprite("images/plat225.png", config.ESCALA_PLATAFORMA)
            elif (i == 3):
                self.plataforma_sprite = arcade.Sprite("images/plat240.png", config.ESCALA_PLATAFORMA)
            elif (i == 5):
                self.plataforma_sprite = arcade.Sprite("images/plat600.png", config.ESCALA_PLATAFORMA)
            else:
                self.plataforma_sprite = arcade.Sprite("images/plat300.png", config.ESCALA_PLATAFORMA)
            self.plataforma_sprite.center_x = self.plataforma_center_x[i]
            self.plataforma_sprite.center_y = self.plataforma_center_y[i]
            self.lista_plataforma.append(self.plataforma_sprite)
        self.lista_chao = None
        self.lista_teto = None
        self.lista_teto = arcade.SpriteList()
        self.lista_chao = arcade.SpriteList()
        self.sprite_teto = objetos.Teto("images/teto_e_chao.png", config.ESCALA_CHAO_TETO)
        self.sprite_teto.center_x = 450
        self.sprite_teto.center_y = 645
        self.lista_teto.append(self.sprite_teto)
        self.sprite_chao = objetos.Chao("images/teto_e_chao.png", config.ESCALA_CHAO_TETO)
        self.sprite_chao.center_x = 450
        self.sprite_chao.center_y = 15
        self.lista_chao.append(self.sprite_chao)
        self.fundo = None
        self.fundo = arcade.load_texture("images/fundo.png")

# Classe da derrota do jogo
class GameOver():

# Reseta para os valores iniciais, caso o jogador queira reiniciar o jogo
    def game_over(self):
        self.laugh = 1
        self.vidas = 3
        self.lista_vidas = None
        self.lista_vidas = arcade.SpriteList()
        posicao_x = 885
        for i in range(3):
            self.sprite_vida = arcade.Sprite("images/cabeca_personagem.png", 0.25)
            self.sprite_vida.center_x = posicao_x
            self.sprite_vida.center_y = 645
            self.lista_vidas.append(self.sprite_vida)
            posicao_x += -30
        self.call_contreg = False
        self.reg_tempo = 0
        self.reg_segundos = 3
        self.change_level = False
        self.draw_cont = False
        self.cont_tempo = True
        if self.modo_2_jogadores == False:
            self.tela = None
            self.tela = arcade.load_texture("images/tela_game_over.png")
            arcade.draw_texture_rectangle(config.LARGURA_TELA // 2, config.ALTURA_TELA // 2,config.LARGURA_TELA, config.ALTURA_TELA, self.tela)
        elif self.modo_2_jogadores == True:
            self.tela = None
            self.tela = arcade.load_texture("images/player_2_won.png")
            arcade.draw_texture_rectangle(config.LARGURA_TELA // 2, config.ALTURA_TELA // 2,config.LARGURA_TELA, config.ALTURA_TELA, self.tela)
        self.sprite_inimigo.center_x = 45
        self.sprite_inimigo.center_y = 62
        self.sprite_inimigo.change_x = 0
        self.sprite_inimigo.change_y = 0
        self.sprite_personagem.center_x = 450
        self.sprite_personagem.center_y = 62
        self.sprite_personagem.change_x = 0
        self.sprite_personagem.change_y = 0
        self.movimento_lado_inimigo = 2
        self.quantidade_inimigos = 0
        self.lista_inimigo = None
        self.lista_inimigo = arcade.SpriteList()
        self.sprite_inimigo = objetos.Enemy("images/inimigo.png", config.ESCALA_INIMIGO)
        self.sprite_inimigo.center_x = 45
        self.sprite_inimigo.center_y = 62
        self.lista_inimigo.append(self.sprite_inimigo)
        self.quantidade_inimigos = 1
        self.lista_moeda = None
        self.lista_saco = None
        self.lista_maleta = None
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
        self.tempo = 0
        self.segundos = 0
        self.minutos = 0
        self.contador = "00:00"
        self.reg_contador == "3"
        self.placar = 0
        self.fase = 1
        self.lista_plataforma = []
        self.lista_plataforma = arcade.SpriteList()
        self.plataforma_center_x = [225,675,75,450,825,450,150,750]
        self.plataforma_center_y = [135,135,260,250,260,385,510,510]
        if self.fase == 1:
            for i in range(8):
                if (i == 0) or (i == 1) or (i == 2) or (i == 4):
                    self.plataforma_sprite = arcade.Sprite("images/plat225.png", config.ESCALA_PLATAFORMA)
                elif (i == 3):
                    self.plataforma_sprite = arcade.Sprite("images/plat240.png", config.ESCALA_PLATAFORMA)
                elif (i == 5):
                    self.plataforma_sprite = arcade.Sprite("images/plat600.png", config.ESCALA_PLATAFORMA)
                else:
                    self.plataforma_sprite = arcade.Sprite("images/plat300.png", config.ESCALA_PLATAFORMA)
                self.plataforma_sprite.center_x = self.plataforma_center_x[i]
                self.plataforma_sprite.center_y = self.plataforma_center_y[i]
                self.lista_plataforma.append(self.plataforma_sprite)
        elif self.fase == 2:
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
        elif self.fase == 3:
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
        elif self.fase == 4:
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
        #Redefine o chão e o teto
        self.lista_chao = None
        self.lista_teto = None
        self.lista_teto = arcade.SpriteList()
        self.lista_chao = arcade.SpriteList()
        if self.fase == 1:
            self.sprite_teto = objetos.Teto("images/teto_e_chao.png", config.ESCALA_CHAO_TETO)
            self.sprite_teto.center_x = 450
            self.sprite_teto.center_y = 645
            self.lista_teto.append(self.sprite_teto)
            self.sprite_chao = objetos.Chao("images/teto_e_chao.png", config.ESCALA_CHAO_TETO)
            self.sprite_chao.center_x = 450
            self.sprite_chao.center_y = 15
            self.lista_chao.append(self.sprite_chao)
        elif self.fase == 2:
            self.sprite_teto = objetos.Teto("images/teto_e_chao_2.png", config.ESCALA_CHAO_TETO)
            self.sprite_teto.center_x = 450
            self.sprite_teto.center_y = 645
            self.lista_teto.append(self.sprite_teto)
            self.sprite_chao = objetos.Chao("images/teto_e_chao_2.png", config.ESCALA_CHAO_TETO)
            self.sprite_chao.center_x = 450
            self.sprite_chao.center_y = 15
            self.lista_chao.append(self.sprite_chao)
        elif self.fase == 3:
            self.sprite_teto = objetos.Teto("images/teto_e_chao.png_3", config.ESCALA_CHAO_TETO)
            self.sprite_teto.center_x = 450
            self.sprite_teto.center_y = 645
            self.lista_teto.append(self.sprite_teto)
            self.sprite_chao = objetos.Chao("images/teto_e_chao.png_3", config.ESCALA_CHAO_TETO)
            self.sprite_chao.center_x = 450
            self.sprite_chao.center_y = 15
            self.lista_chao.append(self.sprite_chao)
        elif self.fase == 4:
            self.sprite_teto = objetos.Teto("images/teto_e_chao_4.png", config.ESCALA_CHAO_TETO)
            self.sprite_teto.center_x = 450
            self.sprite_teto.center_y = 645
            self.lista_teto.append(self.sprite_teto)
            self.sprite_chao = objetos.Chao("images/teto_e_chao_4.png", config.ESCALA_CHAO_TETO)
            self.sprite_chao.center_x = 450
            self.sprite_chao.center_y = 15
            self.lista_chao.append(self.sprite_chao)
        #Redefine o fundo
        self.fundo = None
        self.fundo = arcade.load_texture("images/fundo.png")