import arcade
import config
import objetos
import random

# Classe menu principal
class MenuPrincipal():

# Atualiza a tela do menu principal, caso alguns dos botões do menu principal forem pressionados
    def menu_principal(self):
# Define o placar para 0
        self.placar = 0
        self.placar_parcial = 0
        if self.mouse_pressionado_jogar == False and self.mouse_pressionado_ajuda == False and self.mouse_pressionado_2_jogadores == False:
            self.tela = None
            self.tela = arcade.load_texture("images/menu_principal_1.png")
            arcade.draw_texture_rectangle(config.LARGURA_TELA // 2, config.ALTURA_TELA // 2,config.LARGURA_TELA, config.ALTURA_TELA, self.tela)
        elif self.mouse_pressionado_jogar == True:
            self.tela = None
            self.tela = arcade.load_texture("images/menu_principal_2.png")
            arcade.draw_texture_rectangle(config.LARGURA_TELA // 2, config.ALTURA_TELA // 2,config.LARGURA_TELA, config.ALTURA_TELA, self.tela)
        elif self.mouse_pressionado_ajuda == True:
            self.tela = None
            self.tela = arcade.load_texture("images/menu_principal_3.png")
            arcade.draw_texture_rectangle(config.LARGURA_TELA // 2, config.ALTURA_TELA // 2,config.LARGURA_TELA, config.ALTURA_TELA, self.tela)
        elif self.mouse_pressionado_2_jogadores == True:
            self.tela = None
            self.tela = arcade.load_texture("images/menu_principal_4.png")
            arcade.draw_texture_rectangle(config.LARGURA_TELA // 2, config.ALTURA_TELA // 2,config.LARGURA_TELA, config.ALTURA_TELA, self.tela)
        self.laugh = 1
        self.vidas = 3
        self.lista_vidas = None
        self.lista_vidas = arcade.SpriteList()
        self.modo_2_jogadores = False
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
        self.change_level = False
        self.draw_cont = False
        self.call_contreg = False
        self.movimento_lado_inimigo = 2
# Define as posições para as iniciais novamente
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
        self.reg_contador == "3"
# Reseta o placar
        self.fase = 1
# Gera as novas plataformas
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
# Redefine o chão e o teto
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
# Redefine o fundo
        self.fundo = None
        self.fundo = arcade.load_texture("images/fundo.png")