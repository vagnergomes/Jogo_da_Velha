"""
Jogo da velha
Autor: Vagner Gomes
10/07/2019
"""
import sys

jogador1 = 'JOGADOR 1'
jogador2 = 'JOGADOR 2'
ptd_jogador1 = 0
ptd_jogador2 = 0
ptd_empate = 0
partidas_jogadas = 0
jogador_atual = 0
venceu = False
empate = False

tab_inicial = f""" 
    - Para jogar, digite um número correspondente à posição indicada na tabela abaixo:
      1|2|3 
    ---------
      4|5|6
    ---------
      7|8|9
    """

while True:
    tb = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    print('--- Bem-vindo ao Jogo da Velha! ---'.upper())

    while jogador_atual != 1 and jogador_atual != 2:
        print(f'\n- Quem vai começar, {jogador1} (1) ou {jogador2} (2)? ')
        jogador_atual = int(input())

    jogador1 = input(f'\n- Digite um apelido para o(a) {jogador1}: ')
    jogador2 = input(f'- Digite um apelido para o(a) {jogador2}: ')

    print(f"\n- O(a) {jogador1} vai ficar com 'O' e o(a) {jogador2} vai ficar com 'X'.")
    print(f"\n- Muito bem, o(a) {jogador1 if jogador_atual == 1 else jogador2} começa!")

    print(tab_inicial)


    def tab_atualizado():
        tabuleiro = f"""
      {tb[0]}|{tb[1]}|{tb[2]} 
    ---------
      {tb[3]}|{tb[4]}|{tb[5]}
    ---------
      {tb[6]}|{tb[7]}|{tb[8]}
    """
        print(tabuleiro)


    def verificar_quem_joga():
        global jogador_atual
        global jogador1
        global jogador2
        num_jogador = jogador_atual
        jogador = ''
        if num_jogador == 1:
            jogador_atual = 2
            jogador = jogador1
        if num_jogador == 2:
            jogador_atual = 1
            jogador = jogador2
        return jogador, num_jogador


    def jogada():
        jogador, num_jogador = verificar_quem_joga()
        global jogador_atual
        global tb
        pos_a = 0
        pos_b = 0
        if num_jogador == 1:
            while pos_a not in range(1, (9+1)):
                pos_a = input(f"- É a vez do(a) {jogador}. Escolha uma posição para marcar 'O': ")
                if not pos_a.isnumeric():
                    print("É necessário digitar um número.")
                else:
                    pos_a = int(pos_a)
                    if pos_a not in range(1, (9+1)):
                        print("Posição inválida. Escolha entre 1 e 9.")

            pos_a = pos_a - 1
            tb.pop(pos_a)
            tb.insert(pos_a, 'O')
        if num_jogador == 2:
            while pos_b not in range(1, (9 + 1)):
                pos_b = input(f"- É a vez do(a) {jogador}. Escolha uma posição para marcar 'X': ")
                if not pos_b.isnumeric():
                    print("É necessário digitar um número.")
                else:
                    pos_b = int(pos_b)
                    if pos_b not in range(1, (9 + 1)):
                        print("Posição inválida. Escolha entre 1 e 9.")
            pos_b = pos_b - 1
            tb.pop(pos_b)
            tb.insert(pos_b, 'X')
        tab_atualizado()


    def verificar_vencedor():
        global tb
        global jogador1
        global jogador2
        global ptd_jogador1
        global ptd_jogador2
        global ptd_empate
        global empate

        # jogadas = ([0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 7], [2, 4, 6])
        jogadas_atuais = [tb[0:3], tb[3:6], tb[6:9], tb[0:7:3], tb[1:8:3], tb[2:9:3], tb[0:9:4], tb[2:7:2]]

        verifica_x = bool([jg for jg in jogadas_atuais if jg.count('X') >= 3])
        verifica_o = bool([jg for jg in jogadas_atuais if jg.count('O') >= 3])

        if not verifica_x and not verifica_o:
            empate = all([type(t) == str for t in tb])

        if not empate:
            if verifica_o is True:
                ptd_jogador1 = ptd_jogador1 + 1
                return True, False, jogador1
            if verifica_x is True:
                ptd_jogador2 = ptd_jogador2 + 1
                return True, False, jogador2
            else:
                return False, False, ''
        else:
            ptd_empate = ptd_empate + 1
            return False, True, ''


    def atulizar_placar():
        print("-----------------PLACAR------------------")
        print(f"|  Partida(s) jogada(s): {ptd_jogador1 + ptd_jogador2 + ptd_empate}  ")
        print(f"|  {jogador1}: {ptd_jogador1} partida(s) ")
        print(f"|  {jogador2}: {ptd_jogador2} partida(s) ")
        print(f"|  Empate: {ptd_empate} empate(s) ")
        print("----------------------------------------")


    while not venceu and not empate:
        v, e, vencedor = verificar_vencedor()
        if not v and not e:
            jogada()
        elif e and not v:
            print(f"--- EMPATE ---")
            empate = False
            break
        elif v and not e:
            print(f"--- Parabéns, {vencedor}. Você ganhou! ---")
            break
        else:
            print("- Houve um problema!")
            break

    while True:
        atulizar_placar()
        print("\n- Digite S para continuar jogando ou N para sair.")
        comecar = input().lower()
        break

    if comecar == 's' or comecar == "'s'":
        continue
    elif comecar != 's' or comecar != "'s'":
        sys.exit(0)
