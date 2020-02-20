# Autores:Jhonnatan G. Levandowski
#         Matheus O. Venera
#         Yasmin J. Piske

# Importa as bibliotecas e arquivos necessários
import menu_principal
import config
import objetos
import telas
import fases
import arcade
import os
import random

# Classe utilizada para remover as vidas do personagem
class PerderVida():

# Função utilizada para remover uma vida ao jogador morrer uma vez
    def perdervida(self):
        self.vidas += -1
        self.lista_vidas.remove(self.lista_vidas[-1])
        for i in range(len(self.lista_inimigo)):
            self.lista_inimigo[i].center_x = 45
            self.lista_inimigo[i].center_y = 62
            self.lista_inimigo[i].change_x = 0
            self.lista_inimigo[i].change_y = 0
        self.sprite_personagem.center_x = 450
        self.sprite_personagem.center_y = 62
        self.sprite_personagem.change_x = 0
        self.sprite_personagem.change_y = 0
        if self.fase == 1 or self.fase == 2:
            self.movimento_lado_inimigo = 2
        elif self.fase == 3 or self.fase == 4:
            self.movimento_lado_inimigo = 3
        self.placar_parcial = 0

# Classe principal, onde são executados todas as ações
class MyGame(arcade.Window):

# Função utilizada para criar as variáveis
    def __init__(self, width, height, title):
# Herança de classe padrão do arcade
        super().__init__(width, height, title)
# Diretório atual
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        self.estado_som = True
        self.icone_estado_som = None
        self.lista_icone_estado_som = None
        self.jumping_sound = arcade.load_sound("sounds/jump.wav")
        self.pick_money_sound = arcade.load_sound("sounds/pick_coin.wav")
        self.laugh_sound = arcade.load_sound("sounds/laugh.wav")
        self.game_win_sound = arcade.load_sound("sounds/game_win.wav")
        self.bump_sound = arcade.load_sound("sounds/bump.wav")
        self.game_over_sound = arcade.load_sound("sounds/game_over.wav")
        self.death_sound = arcade.load_sound("sounds/death.wav")
        self.pause_sound = arcade.load_sound("sounds/pause.wav")
        self.score_update_sound = arcade.load_sound("sounds/score.wav")
        self.gover = True
        self.laugh = 1
        self.pause = False
        self.ajuda_contagem = 1
        self.modo_2_jogadores = False
        self.ajuda = False
        self.mouse_pressionado_jogar = False
        self.mouse_pressionado_ajuda = False
        self.mouse_pressionado_2_jogadores = False
        self.menu_principal = True
        self.colisao_inimigo_com_inimigo = False
        self.vidas = 3
        self.lista_vidas = None
        self.placar_parcial = 0
        self.fase = 1
        self.movimento_lado_inimigo = 2
        self.quantidade_inimigos = 0
        self.lista_personagem = None
        self.lista_moeda = None
        self.lista_saco = None
        self.lista_maleta = None
        self.lista_inimigo = None
        self.lista_chao = None
        self.lista_teto = None
        self.lista_plataforma = None
        self.fundo = None
        self.gameover = False
        self.tempo = 0
        self.segundos = 0
        self.minutos = 0
        self.reg_contador = "00:00"
        self.placar = 0
        self.call_contreg = False
        self.reg_tempo = 0
        self.reg_segundos = 3
        self.change_level = False
        self.gamewin = False
        self.draw_cont = False
        self.cont_tempo = True
        self.sprite_pause = None
        self.lista_pause = None
        self.sprite_personagem = None
        self.sprite_inimigo = None
        self.sprite_moeda = None
        self.sprite_saco = None
        self.sprite_maleta = None
        self.sprite_teto = None
        self.sprite_chao = None
        self.a_pressionado = False
        self.d_pressionado = False
        self.w_pressionado = False
        self.UP_pressionado = False
        self.LEFT_pressionado = False
        self.RIGHT_pressionado = False
        arcade.set_background_color(arcade.color.AMAZON)

# Função utilizada para atribuir os valores das variáveis
    def setup(self):
        self.lista_icone_estado_som = arcade.SpriteList()
        self.lista_pause = arcade.SpriteList()
        self.lista_vidas = arcade.SpriteList()
        self.lista_personagem = arcade.SpriteList()
        self.lista_moeda = arcade.SpriteList()
        self.lista_saco = arcade.SpriteList()
        self.lista_maleta = arcade.SpriteList()
        self.lista_inimigo = arcade.SpriteList()
        self.lista_plataforma = arcade.SpriteList()
        self.lista_teto = arcade.SpriteList()
        self.lista_chao = arcade.SpriteList()
        self.fundo = arcade.load_texture("images/fundo.png")
        self.plataforma_center_x = [225,675,75,450,825,450,150,750]
        self.plataforma_center_y = [135,135,260,250,260,385,510,510]
        posicao_x = 885
        for i in range(3):
            self.sprite_vida = arcade.Sprite("images/cabeca_personagem.png", 0.25)
            self.sprite_vida.center_x = posicao_x
            self.sprite_vida.center_y = 645
            self.lista_vidas.append(self.sprite_vida)
            posicao_x += -30
        self.icone_estado_som = arcade.Sprite("images/icone_som_ligado.png", 1)
        self.icone_estado_som.center_x = 867
        self.icone_estado_som.center_y = 20
        self.lista_icone_estado_som.append(self.icone_estado_som)
        self.icone_estado_som = arcade.Sprite("images/icone_som_desligado.png", 1)
        self.icone_estado_som.center_x = 874
        self.icone_estado_som.center_y = 20
        self.lista_icone_estado_som.append(self.icone_estado_som)
        self.sprite_personagem = objetos.Personagem("images/personagem.png", config.ESCALA_PERSONAGEM)
        self.sprite_personagem.center_x = 450
        self.sprite_personagem.center_y = 62
        self.lista_personagem.append(self.sprite_personagem)
        self.sprite_inimigo = objetos.Enemy("images/inimigo.png", config.ESCALA_INIMIGO)
        self.sprite_inimigo.center_x = 45
        self.sprite_inimigo.center_y = 62
        self.lista_inimigo.append(self.sprite_inimigo)
        self.quantidade_inimigos = 1
        self.sprite_teto = objetos.Teto("images/teto_e_chao.png", config.ESCALA_CHAO_TETO)
        self.sprite_teto.center_x = 450
        self.sprite_teto.center_y = 645
        self.lista_teto.append(self.sprite_teto)
        self.sprite_chao = objetos.Chao("images/teto_e_chao.png", config.ESCALA_CHAO_TETO)
        self.sprite_chao.center_x = 450
        self.sprite_chao.center_y = 15
        self.lista_chao.append(self.sprite_chao)
        self.sprite_moeda = objetos.Moeda("images/moeda.png", config.ESCALA_MOEDA)
        self.sprite_moeda.center_x = random.randint(1,900)
        self.sprite_saco = objetos.Saco("images/saco_de_dinheiro.png", config.ESCALA_SACO)
        self.sprite_saco.center_x = random.randint(1,900)
        self.sprite_saco.center_y = random.randint(1,660)
        self.sprite_maleta = objetos.Maleta("images/maleta_de_dinheiro.png", config.ESCALA_MALETA)
        self.sprite_maleta.center_x = random.randint(1,900)
        self.sprite_maleta.center_y = random.randint(1,660)
        self.sprite_pause = arcade.Sprite("images/tela_pause.png", 1)
        self.sprite_pause.center_x = 450
        self.sprite_pause.center_y = 330
        self.lista_pause.append(self.sprite_pause)
# Cria os sprites das plataformas
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

# Escolhe de forma aleatória um item para ser gerado para o drop
    def drops(self):
        chance = random.randint(1,10)
        if chance >= 1 and chance <= 5:
            return "moeda"
        elif chance >= 6 and chance <= 8:
            return "saco"
        elif chance >=9 and chance <= 10:
            return "maleta"

# Classe utilizada para desenhar tudo na tela
    def on_draw(self):
        arcade.start_render()
        if self.menu_principal == False:
            if self.pause == False:
                if self.ajuda == False:
                    if self.gameover == False:
                        arcade.draw_texture_rectangle(config.LARGURA_TELA // 2, config.ALTURA_TELA // 2,config.LARGURA_TELA, config.ALTURA_TELA, self.fundo)
                        self.lista_moeda.draw()
                        self.lista_saco.draw()
                        self.lista_maleta.draw()
                        self.lista_personagem.draw()
                        self.lista_inimigo.draw()
                        self.lista_plataforma.draw()
                        self.lista_chao.draw()
                        self.lista_teto.draw()
                        self.lista_vidas.draw()
                        if self.segundos % config.TEMPO_DROP == 0 and self.segundos != 0 and self.tempo < 2 and (len(self.lista_moeda) + len(self.lista_saco) + len(self.lista_maleta)) < 10:
                            MyGame.drops(self)
                            if MyGame.drops(self) == "moeda":
                                self.sprite_moeda = objetos.Moeda("images/moeda.png", config.ESCALA_MOEDA)
                                self.sprite_moeda.center_x = random.randint(50,850)
                                self.sprite_moeda.center_y = random.randint(50,610)
                                hit_list_moeda_plataforma = arcade.check_for_collision_with_list(self.sprite_moeda, self.lista_plataforma)
                                if len(hit_list_moeda_plataforma) > 0:
                                    self.sprite_moeda.center_y += -33
                                self.lista_moeda.append(self.sprite_moeda)
                            elif MyGame.drops(self) == "saco":
                                self.sprite_saco = objetos.Saco("images/saco_de_dinheiro.png", config.ESCALA_SACO)
                                self.sprite_saco.center_x = random.randint(50,850)
                                self.sprite_saco.center_y = random.randint(50,610)
                                hit_list_saco_plataforma = arcade.check_for_collision_with_list(self.sprite_saco, self.lista_plataforma)
                                if len(hit_list_saco_plataforma) > 0:
                                    self.sprite_saco.center_y += -33
                                self.lista_saco.append(self.sprite_saco)
                            elif MyGame.drops(self) == "maleta":
                                self.sprite_maleta = objetos.Maleta("images/maleta_de_dinheiro.png", config.ESCALA_MALETA)
                                self.sprite_maleta.center_x = random.randint(50,850)
                                self.sprite_maleta.center_y = random.randint(50,610)
                                hit_list_maleta_plataforma = arcade.check_for_collision_with_list(self.sprite_maleta, self.lista_plataforma)
                                if len(hit_list_maleta_plataforma) > 0:
                                    self.sprite_maleta.center_y += -33
                                self.lista_maleta.append(self.sprite_maleta)
                        if self.modo_2_jogadores == False:
                            if self.segundos % config.TEMPO_INIMIGO == 0 and (self.minutos == 0 and self.segundos !=0) and self.tempo == 1  and (self.minutos == 0 and self.segundos < 21):
                                self.novo_sprite_inimigo = objetos.Enemy("images/inimigo.png", config.ESCALA_INIMIGO)
                                self.novo_sprite_inimigo.center_x = 450
                                self.novo_sprite_inimigo.center_y = 62
                                self.lista_inimigo.append(self.novo_sprite_inimigo)
                                self.quantidade_inimigos += 1
                        if self.draw_cont == True:
                            if self.fase == 1:
                                if self.reg_segundos == 3:
                                    self.tela = arcade.load_texture("images/fase1_3.png")
                                    arcade.draw_texture_rectangle(config.LARGURA_TELA // 2, config.ALTURA_TELA // 2,config.LARGURA_TELA, config.ALTURA_TELA, self.tela)
                                elif self.reg_segundos == 2:
                                    self.tela = arcade.load_texture("images/fase1_2.png")
                                    arcade.draw_texture_rectangle(config.LARGURA_TELA // 2, config.ALTURA_TELA // 2,config.LARGURA_TELA, config.ALTURA_TELA, self.tela)
                                elif self.reg_segundos == 1:
                                    self.tela = arcade.load_texture("images/fase1_1.png")
                                    arcade.draw_texture_rectangle(config.LARGURA_TELA // 2, config.ALTURA_TELA // 2,config.LARGURA_TELA, config.ALTURA_TELA, self.tela)
                            elif self.fase == 2:
                                if self.reg_segundos == 3:
                                    self.tela = arcade.load_texture("images/fase2_3.png")
                                    arcade.draw_texture_rectangle(config.LARGURA_TELA // 2, config.ALTURA_TELA // 2,config.LARGURA_TELA, config.ALTURA_TELA, self.tela)
                                elif self.reg_segundos == 2:
                                    self.tela = arcade.load_texture("images/fase2_2.png")
                                    arcade.draw_texture_rectangle(config.LARGURA_TELA // 2, config.ALTURA_TELA // 2,config.LARGURA_TELA, config.ALTURA_TELA, self.tela)
                                elif self.reg_segundos == 1:
                                    self.tela = arcade.load_texture("images/fase2_1.png")
                                    arcade.draw_texture_rectangle(config.LARGURA_TELA // 2, config.ALTURA_TELA // 2,config.LARGURA_TELA, config.ALTURA_TELA, self.tela)
                            elif self.fase == 3:
                                if self.reg_segundos == 3:
                                    self.tela = arcade.load_texture("images/fase3_3.png")
                                    arcade.draw_texture_rectangle(config.LARGURA_TELA // 2, config.ALTURA_TELA // 2,config.LARGURA_TELA, config.ALTURA_TELA, self.tela)
                                elif self.reg_segundos == 2:
                                    self.tela = arcade.load_texture("images/fase3_2.png")
                                    arcade.draw_texture_rectangle(config.LARGURA_TELA // 2, config.ALTURA_TELA // 2,config.LARGURA_TELA, config.ALTURA_TELA, self.tela)
                                elif self.reg_segundos == 1:
                                    self.tela = arcade.load_texture("images/fase3_1.png")
                                    arcade.draw_texture_rectangle(config.LARGURA_TELA // 2, config.ALTURA_TELA // 2,config.LARGURA_TELA, config.ALTURA_TELA, self.tela)
                        if self.call_contreg == False:
                            arcade.draw_text(self.contador,5,5,arcade.color.WHITE,20)
                            if self.fase == 1:
                                arcade.draw_text(("R$: "+ str(self.placar) + "/1000"),5,635,arcade.color.WHITE,20)
                            elif self.fase == 2:
                                arcade.draw_text(("R$: "+ str(self.placar) + "/1500"),5,635,arcade.color.WHITE,20)
                            elif self.fase == 3:
                                arcade.draw_text(("R$: "+ str(self.placar) + "/1000"),5,635,arcade.color.WHITE,20)
                            elif self.fase == 4:
                                arcade.draw_text(("R$: "+ str(self.placar) + "/1000"),5,635,arcade.color.WHITE,20)
                            if self.placar_parcial == 0:
                                arcade.draw_text((str(self.placar_parcial)),self.sprite_personagem.center_x-5,self.sprite_personagem.center_y + 40,arcade.color.WHITE,20)
                            elif self.placar_parcial > 0 and self.placar_parcial < 100:
                                arcade.draw_text((str(self.placar_parcial)),self.sprite_personagem.center_x - 10,self.sprite_personagem.center_y + 40,arcade.color.WHITE,20)
                            elif self.placar_parcial >= 100 and self.placar_parcial < 1000:
                                arcade.draw_text((str(self.placar_parcial)),self.sprite_personagem.center_x - 17,self.sprite_personagem.center_y + 40,arcade.color.WHITE,20)
                            elif self.placar_parcial >= 1000:
                                arcade.draw_text((str(self.placar_parcial)),self.sprite_personagem.center_x - 25,self.sprite_personagem.center_y + 40,arcade.color.WHITE,20)
                    elif self.gameover == True:
                        telas.GameOver.game_over(self)
                        if self.gover == True:
                            if self.estado_som == True:
                                if self.modo_2_jogadores == False:
                                    arcade.play_sound(self.game_over_sound)
                                elif self.modo_2_jogadores == True:
                                    arcade.play_sound(self.game_win_sound)
                            self.gover = False
                elif self.ajuda == True:
                    telas.Ajuda.ajuda(self)
                if self.gamewin == True:
                    telas.GameWin.game_win(self)
                    if self.gover == True:
                        if self.estado_som == True:
                            arcade.play_sound(self.game_win_sound)
                        self.gover = False
            elif self.pause == True:
                arcade.draw_texture_rectangle(config.LARGURA_TELA // 2, config.ALTURA_TELA // 2,config.LARGURA_TELA, config.ALTURA_TELA, self.fundo)
                self.lista_moeda.draw()
                self.lista_saco.draw()
                self.lista_maleta.draw()
                self.lista_personagem.draw()
                self.lista_inimigo.draw()
                self.lista_plataforma.draw()
                self.lista_chao.draw()
                self.lista_teto.draw()
                self.lista_vidas.draw()
                if self.call_contreg == False:
                    arcade.draw_text(self.contador,5,5,arcade.color.WHITE,20)
                    if self.fase == 1:
                        arcade.draw_text(("R$: "+ str(self.placar) + "/1000"),5,635,arcade.color.WHITE,20)
                    elif self.fase == 2:
                        arcade.draw_text(("R$: "+ str(self.placar) + "/1500"),5,635,arcade.color.WHITE,20)
                    elif self.fase == 3:
                        arcade.draw_text(("R$: "+ str(self.placar) + "/1000"),5,635,arcade.color.WHITE,20)
                    elif self.fase == 4:
                        arcade.draw_text(("R$: "+ str(self.placar) + "/1000"),5,635,arcade.color.WHITE,20)
                    if self.placar_parcial == 0:
                        arcade.draw_text((str(self.placar_parcial)),self.sprite_personagem.center_x-5,self.sprite_personagem.center_y + 40,arcade.color.WHITE,20)
                    elif self.placar_parcial > 0 and self.placar_parcial < 100:
                        arcade.draw_text((str(self.placar_parcial)),self.sprite_personagem.center_x - 10,self.sprite_personagem.center_y + 40,arcade.color.WHITE,20)
                    elif self.placar_parcial >= 100 and self.placar_parcial < 1000:
                        arcade.draw_text((str(self.placar_parcial)),self.sprite_personagem.center_x - 17,self.sprite_personagem.center_y + 40,arcade.color.WHITE,20)
                    elif self.placar_parcial >= 1000:
                        arcade.draw_text((str(self.placar_parcial)),self.sprite_personagem.center_x - 25,self.sprite_personagem.center_y + 40,arcade.color.WHITE,20)
                self.lista_pause.draw()
                if self.estado_som == True:
                    self.lista_icone_estado_som[0].draw()
                elif self.estado_som == False:
                    self.lista_icone_estado_som[1].draw()
        elif self.menu_principal == True:
            menu_principal.MenuPrincipal.menu_principal(self)
            if self.estado_som == True:
                self.lista_icone_estado_som[0].draw()
            elif self.estado_som == False:
                self.lista_icone_estado_som[1].draw()

# Função utilizada para atualizar o jogo(contador de tempo, posições, colisões, etc.)
    def update(self, delta_time):
        if self.menu_principal == False:
            if self.pause == False:
                if self.ajuda == False:
                    self.sprite_personagem.change_y += -0.3
                    self.sprite_personagem.change_x = 0
# Inicia a contagem regressiva antes do início de uma fase
                    for i in range(len(self.lista_inimigo)):
                        self.lista_inimigo[i].change_y += -0.3
                        self.lista_inimigo[i].change_x = 0
                    self.tempo += 1
                    if self.tempo == 56:
                        self.tempo = 0
                        self.segundos += 1
                    if self.segundos == 60:
                        self.segundos = 0
                        self.minutos += 1
                    if self.call_contreg == True:
                        self.reg_tempo += 1
                        if self.fase<=3:
                            self.draw_cont = True
                            if self.reg_tempo == 56:
                                self.reg_tempo = 0
                                self.reg_segundos -= 1
                                if self.reg_segundos == 0:
                                    self.call_contreg = False
                                    self.reg_segundos = 3
                                    self.change_level = True
                                    self.draw_cont = False
                        else:
                            self.gamewin = True
# Muda de fase
                    if self.change_level == True:
                        if self.fase == 1:
                            self.fase = 2
                            arcade.finish_render()
                            fases.Fase2.fase2(self)
                            MyGame.on_draw(self)
                            self.change_level = False
                        elif self.fase == 2:
                            self.fase = 3
                            arcade.finish_render()
                            fases.Fase3.fase3(self)
                            MyGame.on_draw(self)
                            self.change_level = False
                        elif self.fase == 3:
                            self.fase = 4
                            arcade.finish_render()
                            fases.Fase4.fase4(self)
                            MyGame.on_draw(self)
                            self.change_level = False
                        else:
                            self.change_level = False
                            self.gamewin = True
# Atribui os valores do contador de tempo e da contagem regressiva
                    self.contador = str(self.minutos) + ":" + str(self.segundos)
                    self.reg_contador = str(self.reg_segundos)
# Checa as colisões entre as listas de sprites
                    hit_list_moeda = arcade.check_for_collision_with_list(self.sprite_personagem, self.lista_moeda)
                    hit_list_saco = arcade.check_for_collision_with_list(self.sprite_personagem, self.lista_saco)
                    hit_list_maleta = arcade.check_for_collision_with_list(self.sprite_personagem, self.lista_maleta)
                    hit_list_chao_personagem = arcade.check_for_collision_with_list(self.sprite_personagem, self.lista_chao)
                    hit_list_chao_inimigo = arcade.check_for_collision_with_list(self.sprite_inimigo, self.lista_chao)
                    hit_list_teto_inimigo = arcade.check_for_collision_with_list(self.sprite_inimigo, self.lista_teto)
                    hit_list_inimigo = arcade.check_for_collision_with_list(self.sprite_personagem, self.lista_inimigo)
# Tira uma vida ao personagem colidir com um inimigo
                    if len(hit_list_inimigo) > 0 and self.call_contreg == False:
                        if self.vidas != 1:
                            if self.estado_som == True:
                                arcade.play_sound(self.death_sound)
                            PerderVida.perdervida(self)
                        elif self.vidas == 1:
                            self.gameover = True
# Verifica a colisão com o chão
                    if len(hit_list_chao_personagem) > 0:
                        self.sprite_personagem.change_y = 0
                        self.sprite_personagem.bottom = self.sprite_chao.top + 1
                    if (self.sprite_personagem.bottom - 1) < self.sprite_chao.top:
                        self.sprite_personagem.change_y = 0
                    if (self.sprite_personagem.top + 1) > self.sprite_teto.bottom:
                        self.sprite_personagem.top = self.sprite_teto.bottom - 1
                        self.sprite_personagem.change_y = 0
                        self.sprite_personagem.change_y += -0.3
                    for i in range(len(self.lista_inimigo)):
                        if len(hit_list_chao_inimigo) > 0:
                            self.lista_inimigo[i].change_y = 0
                            self.lista_inimigo[i].bottom = self.sprite_chao.top + 1
                        if (self.lista_inimigo[i].bottom - 1) < self.sprite_chao.top:
                            self.lista_inimigo[i].change_y = 0
                    if len(hit_list_teto_inimigo) > 0:
                        for i in range(len(self.lista_inimigo)):
                            self.lista_inimigo[i].top = self.sprite_teto.bottom - 1
                            self.lista_inimigo[i].change_y = 0
                            self.lista_inimigo[i].change_y += -0.3
# Verifica a colisão com as plataformas e de que direção e onde ela ocorre
                    for k in range(len(self.lista_inimigo)):
                        for i in range(len(self.lista_plataforma)):
                            hit_sprite_personagem = arcade.check_for_collision(self.sprite_personagem, self.lista_plataforma[i])
                            hit_sprite_inimigo = arcade.check_for_collision(self.lista_inimigo[k], self.lista_plataforma[i])
                            if hit_sprite_personagem == True:
                                if self.sprite_personagem.top >= self.lista_plataforma[i].bottom and self.sprite_personagem.left < self.lista_plataforma[i].right and self.sprite_personagem.right > self.lista_plataforma[i].left and (self.lista_plataforma[i].bottom + 10) - (171 * 0.4) >= self.sprite_personagem.bottom:
                                    self.sprite_personagem.change_y = 0
                                    self.sprite_personagem.change_y += -0.3
                                    self.sprite_personagem.top = self.lista_plataforma[i].bottom - 1
                                elif self.sprite_personagem.bottom <= self.lista_plataforma[i].top and self.sprite_personagem.left < self.lista_plataforma[i].right and self.sprite_personagem.right > self.lista_plataforma[i].left and ((self.lista_plataforma[i].top - 10) + (171 * 0.4) <= self.sprite_personagem.top):
                                    self.sprite_personagem.change_y = 0
                                    self.sprite_personagem.change_x = -self.sprite_personagem.change_x
                                else:
                                    self.sprite_personagem.change_x = -self.sprite_personagem.change_x * 1.5
                                    self.w_pressionado = False
                                    self.sprite_personagem.change_y += -0.3
                                    self.a_pressionado = False
                                    self.d_pressionado = False
                            if hit_sprite_inimigo == True:
                                if self.lista_inimigo[k].top >= self.lista_plataforma[i].bottom and self.lista_inimigo[k].left < self.lista_plataforma[i].right and self.lista_inimigo[k].right > self.lista_plataforma[i].left and (self.lista_plataforma[i].bottom + 10) - (171 * 0.4) >= self.lista_inimigo[k].bottom:
                                    self.lista_inimigo[k].change_y = 0
                                    self.lista_inimigo[k].change_y += -0.3
                                    self.lista_inimigo[k].top = self.lista_plataforma[i].bottom - 1
                                elif self.lista_inimigo[k].bottom <= self.lista_plataforma[i].top and self.lista_inimigo[k].left < self.lista_plataforma[i].right and self.lista_inimigo[k].right > self.lista_plataforma[i].left and ((self.lista_plataforma[i].top - 10) + (171 * 0.4) <= self.lista_inimigo[k].top):
                                    self.lista_inimigo[k].change_y = 0
                                    self.lista_inimigo[k].change_x = -self.lista_inimigo[k].change_x
                                else:
                                    self.lista_inimigo[k].change_x = -self.lista_inimigo[k].change_x * 1.5
                                    self.lista_inimigo[k].change_y += -0.3
                    if self.sprite_personagem.left > 387 and self.sprite_personagem.right < 511 and self.sprite_personagem.bottom < 105:
                        if self.placar_parcial != 0:
                            if self.estado_som == True:
                                arcade.play_sound(self.score_update_sound)
                            self.placar += self.placar_parcial
                        self.placar_parcial = 0
# Coleta as moedas, sacos e maletas de dinheiro ao colidirem com o personagem
                    for self.sprite_moeda in hit_list_moeda:
                        self.placar_parcial += 10
                        self.lista_moeda.remove(self.sprite_moeda)
                        if self.estado_som == True:
                            arcade.play_sound(self.pick_money_sound)
                    for self.sprite_saco in hit_list_saco:
                        self.placar_parcial += 25
                        self.lista_saco.remove(self.sprite_saco)
                        if self.estado_som == True:
                            arcade.play_sound(self.pick_money_sound)
                    for self.sprite_maleta in hit_list_maleta:
                        self.placar_parcial += 50
                        self.lista_maleta.remove(self.sprite_maleta)
                        if self.estado_som == True:
                            arcade.play_sound(self.pick_money_sound)
# Movimentação dos automática inimigos
                    if self.modo_2_jogadores == False:
                        for i in range(len(self.lista_inimigo)):
                            if self.sprite_personagem.left > self.lista_inimigo[i].right:
                                self.lista_inimigo[i].change_x = self.movimento_lado_inimigo
                            elif self.sprite_personagem.right < self.lista_inimigo[i].left:
                                self.lista_inimigo[i].change_x = -self.movimento_lado_inimigo
                            if self.lista_inimigo[i].right > self.lista_plataforma[0].left and self.lista_inimigo[i].left < self.lista_plataforma[0].right and self.lista_plataforma[0].bottom - 30 < self.lista_inimigo[i].top and self.lista_inimigo[i].center_y < self.lista_plataforma[0].bottom:
                                pass
                            else:
                                if self.sprite_personagem.bottom > self.lista_inimigo[i].top and self.lista_inimigo[i].change_y == 0:
                                    self.lista_inimigo[i].change_y = config.VELOCIDADE_CIMA_INIMIGO
# Atualiza o nível de dificuldade de acordo com cada fase
                    if self.fase == 1:
                        if self.minutos == 3 and self.placar < 1000:
                            self.gameover = True
                        elif self.placar >= 10:
                            self.call_contreg = True
                            if self.laugh == 1:
                                if self.estado_som == True:
                                    arcade.play_sound(self.laugh_sound)
                                self.laugh = 2
                    elif self.fase == 2:     
                        if self.minutos == 3 and self.placar < 1500:
                            self.gameover = True
                        elif self.placar >= 15:
                            self.call_contreg = True
                            if self.laugh == 2:
                                if self.estado_som == True:
                                    arcade.play_sound(self.laugh_sound)
                                self.laugh = 3
                    elif self.fase == 3:          
                        if self.minutos == 2 and self.segundos == 30 and self.placar < 1000:
                            self.gameover = True
                        elif self.placar >= 10:
                            self.call_contreg = True
                            if self.laugh == 3:
                                if self.estado_som == True:
                                    arcade.play_sound(self.laugh_sound)
                                self.laugh = 4
                    elif self.fase == 4:
                        if self.minutos == 2 and self.placar < 1000:
                            self.gameover = True
                        elif self.placar >= 10:
                            self.call_contreg = True
                            if self.laugh == 4:
                                if self.estado_som == True:
                                    arcade.play_sound(self.game_win_sound)
                                self.laugh = 5
# Movimentação do personagem e do inimigo no modo 2 jogadores
                    if self.w_pressionado:
                        self.sprite_personagem.change_y = config.VELOCIDADE_CIMA
                        self.w_pressionado = False
                    if self.a_pressionado and not self.d_pressionado:
                        self.sprite_personagem.change_x = -config.MOVIMENTO_LADO_PERSONAGEM
                    elif self.d_pressionado and not self.a_pressionado:
                        self.sprite_personagem.change_x = config.MOVIMENTO_LADO_PERSONAGEM
                    if self.UP_pressionado:
                        self.sprite_inimigo.change_y = config.VELOCIDADE_CIMA
                        self.UP_pressionado = False
                    if self.LEFT_pressionado and not self.RIGHT_pressionado:
                        self.sprite_inimigo.change_x = -config.MOVIMENTO_LADO_PERSONAGEM
                    elif self.RIGHT_pressionado and not self.LEFT_pressionado:
                        self.sprite_inimigo.change_x = config.MOVIMENTO_LADO_PERSONAGEM
                    self.lista_personagem.update()
                    self.lista_inimigo.update()
                    self.lista_plataforma.update()
        elif self.menu_principal == True:
            self.ajuda_contagem = 1

# Função que executa ações ao pressionar uma tecla
    def on_key_press(self, key, modifiers):
# Teclas para interagir com o menu
        if key == arcade.key.ENTER and self.menu_principal == True:
            self.mouse_pressionado_jogar = True
        if key == arcade.key.ESCAPE and self.menu_principal == True:
                MyGame.close(self)
# Teclas para interagir com o jogo
        elif key == arcade.key.ESCAPE and self.menu_principal == False and self.gameover == False and self.gamewin == False and self.ajuda == False and self.pause == False:
            self.menu_principal = True
        if key == arcade.key.ESCAPE and self.gamewin == True:
            self.gamewin = False
            self.menu_principal = True
        if self.menu_principal == False:
# Movimentação do personagem
            if self.modo_2_jogadores == False:
                if (key == arcade.key.W or key == arcade.key.UP) and self.sprite_personagem.change_y == 0:
                    if self.estado_som == True:
                        arcade.play_sound(self.jumping_sound)
                    self.w_pressionado = True
                elif key == arcade.key.A or key == arcade.key.LEFT:
                    self.a_pressionado = True
                elif key == arcade.key.D or key == arcade.key.RIGHT:
                    self.d_pressionado = True
            elif self.modo_2_jogadores == True:
                if key == arcade.key.W and self.sprite_personagem.change_y == 0:
                    if self.estado_som == True:
                        arcade.play_sound(self.jumping_sound)
                    self.w_pressionado = True
                elif key == arcade.key.A:
                    self.a_pressionado = True
                elif key == arcade.key.D:
                    self.d_pressionado = True

                if key == arcade.key.UP and self.sprite_inimigo.change_y == 0:
                    if self.estado_som == True:
                        arcade.play_sound(self.jumping_sound)
                    self.UP_pressionado = True
                elif key == arcade.key.LEFT:
                    self.LEFT_pressionado = True
                elif key == arcade.key.RIGHT:
                    self.RIGHT_pressionado = True
# Reinicia o jogo ao perder e a tecla "R" ser pressionada
            if self.gameover == True and key == arcade.key.R:
                self.gameover = False
                self.gover = True
                arcade.finish_render()
                MyGame.on_draw(self)
# Reinicia o jogo ao ganhar e a tecla "R" ser pressionada
            if self.gamewin == True and key == arcade.key.R:
                self.gamewin = False
                self.gover = True
                arcade.finish_render()
                MyGame.on_draw(self)
# Pausa o jogo quando ele estiver em execução e toca o som de pause
            if key == arcade.key.P and self.gameover == False and self.gamewin == False and self.call_contreg == False and self.ajuda == False and self.menu_principal == False and self.pause == False:
                if self.estado_som == True:
                    arcade.play_sound(self.pause_sound)
                self.pause = True
# Despausa o jogo quando ele estiver pausado e toca o som de despause
            elif key == arcade.key.P and self.gameover == False and self.gamewin == False and self.call_contreg == False and self.menu_principal == False and self.pause == True:
                if self.estado_som == True:
                    arcade.play_sound(self.pause_sound)
                self.pause = False
# Passa para a próxima página de ajuda quando alguma tecla diferente de ESC for pressionada
            if self.ajuda == True and key != arcade.key.ESCAPE:
                self.ajuda_contagem += 1

# Função que executa ações ao soltar uma tecla
    def on_key_release(self, key, modifiers):
# Para de movimentar o personagem quando as teclas de movimento deixarem de ser pressionadas
        if key == arcade.key.ENTER and self.menu_principal == True:
            self.mouse_pressionado_jogar = False
            self.menu_principal = False
        if self.modo_2_jogadores == False:
            if key == arcade.key.W or key == arcade.key.UP:
                self.w_pressionado = False
            elif key == arcade.key.A or key == arcade.key.LEFT:
                self.a_pressionado = False
            elif key == arcade.key.D or key == arcade.key.RIGHT:
                self.d_pressionado = False
        elif self.modo_2_jogadores == True:
            if key == arcade.key.W:
                self.w_pressionado = False
            elif key == arcade.key.A:
                self.a_pressionado = False
            elif key == arcade.key.D:
                self.d_pressionado = False
            elif key == arcade.key.UP:
                self.UP_pressionado = False
            elif key == arcade.key.LEFT:
                self.LEFT_pressionado = False
            elif key == arcade.key.RIGHT:
                self.RIGHT_pressionado = False

# Função que executa ações ao clicar em algum botão do mouse, é usado principalmente no menu principal para causar efeitos no botões
    def on_mouse_press(self, x, y, button, modifiers):
        if self.menu_principal == True:
            if button == arcade.MOUSE_BUTTON_LEFT:
                if x > 341 and x < 556 and y > 275 and y < 338:
                    self.mouse_pressionado_jogar = True
                elif x > 341 and x < 556 and y > 187 and y < 250:
                    self.mouse_pressionado_ajuda = True
                elif x > 341 and x < 556 and y > 96 and y < 162:
                    self.mouse_pressionado_2_jogadores = True
                elif x > 851 and x < 899 and y > 3 and y < 36:
                    if self.estado_som == True:
                        self.estado_som = False
                    elif self.estado_som == False:
                        self.estado_som = True
        if self.pause == True:
            if button == arcade.MOUSE_BUTTON_LEFT:
                if x > 851 and x < 899 and y > 3 and y < 36:
                    if self.estado_som == True:
                        self.estado_som = False
                    elif self.estado_som == False:
                        self.estado_som = True


# Função que executa ações ao soltar algum botão do mouse
    def on_mouse_release(self, x, y, button, modifiers):
# Quando o botão esquerdo do mouse deixar de ser pressionado em cima do botão jogar no menu principal, o jogo se inicia
        if self.menu_principal == True:
            if self.mouse_pressionado_jogar == True:
                if button == arcade.MOUSE_BUTTON_LEFT:
                    if x > 341 and x < 556 and y > 275 and y < 338:
                        self.mouse_pressionado_jogar = False
                        self.menu_principal = False
                    else:
                        self.mouse_pressionado_jogar = False
# Quando o botão esquerdo do mouse deixar de ser pressionado em cima do botão ajuda no menu principal, a página de ajuda é aberta
            elif self.mouse_pressionado_ajuda == True:
                if button == arcade.MOUSE_BUTTON_LEFT:
                    if x > 341 and x < 556 and y > 187 and y < 250:
                        self.mouse_pressionado_ajuda = False
                        self.ajuda = True
                        self.menu_principal = False
                    else:
                        self.mouse_pressionado_ajuda = False
            elif self.mouse_pressionado_2_jogadores == True:
                if x > 341 and x < 556 and y > 96 and y < 162:
                    self.mouse_pressionado_2_jogadores = False
                    self.modo_2_jogadores = True
                    self.menu_principal = False
                else:
                    self.mouse_pressionado_2_jogadores = False
        if self.ajuda == True:
            if button == arcade.MOUSE_BUTTON_LEFT:
                self.ajuda_contagem += 1

# Função principal, onde é criada a janela do jogo
def main():
    window = MyGame(config.LARGURA_TELA, config.ALTURA_TELA, config.TITULO)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()