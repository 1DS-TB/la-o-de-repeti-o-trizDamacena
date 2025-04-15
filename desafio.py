import random
from os import remove
from random import randint

from Tools.scripts.summarize_stats import emit_specialization_overview
passar = 0
passar1 = 1
vezes = 0
dfs = 0
vezesPocoes = 0
vezesPocao3 = 0
respostaDano = 0
danoPocao = 0
turno = 1

verdade1 = False
verdade2 = False
verdade3 = False

pocoes = ["[1] Bate Ganha: Se o inimigo atacou, ganhe 5% de cura por duas rodadas",
          "[2] Apanha Bate: Caso o inimigo atacar, cause 2% de dano adicional de volta por duas rodadas",
          "[3] Aumentar poder de ataque por dois turnos",
          "[4] Receba todos os HP de volta, somente em uma rodada"]

pocoes2 = ["[1] Bate Ganha: Ataque o inimigo e ganhe 5% de cura",
          "[2] Apanha Bate: Caso o inimigo atacar, cause 2% de dano de volta",
          "[3] Aumentar poder de ataque por dois turnos",
          "[4] Receba todos os HP de volta, somente em uma rodada"]

status = ["[1] Buffer Overflow:  A cada turno, o personagem sofre dano equivalente a 5% do seu HP máximo",
          "[2] Loop Infinito: O alvo perde a vez por 1 turno enquanto reinicia o sistema",
          "[3] Tela Azul: Reduz a defesa para 0 por 2 turnos",
          "[4] Cache Hit: Recupera 30% do HP máximo. Só pode ser usado quando HP está abaixo de 25%."
          ]


print("======= MENU =======")
escolha = int(input("Deseja jogar:\n[1] Sim\n[2] Não:\n"))
multi = int(input("Deseja jogar multiplayer:\n[1] Sim\n[2] Não:\n "))
if escolha == 2:
    print("Okay")


else:
    if multi == 2:
        HP = random.randint(200, 1000)
        jogador1 = HP
        inimigo2 = HP
        jogador1_25 = (jogador1 * 25)//100
        inimigo2_25 = (inimigo2 * 25) // 100

        jogador1Dano = random.randint(1, 50)
        inimigo2Dano = random.randint(1, 50)

        jogador1DFS = random.randint(1, 50)
        inimigo2DFS = random.randint(1, 50)

        jogador1_dobroDano = 0
        if jogador1_dobroDano > 0:
            jogador1_dobroDano = 0
        inimigo2_dobroDano = ''



        while True:


            print("=== DUELO DE HERÓIS ===")
            print(f"\n--- Turno {turno} ---")
            print(f"=== VOCÊ ===\nHP: {jogador1}\nATQ: {jogador1Dano}      DEF: {jogador1DFS}\n")
            print(f"=== INIMIGO ===\nHP: {inimigo2}\nATQ: {inimigo2Dano}      DEF: {inimigo2DFS}")
            acao = int(input("Sua vez\n[1] Atacar ou [2] Curar: "))

            if respostaDano == 0:
                respostaDano = int(input("Deseja usar dobro de dano\n[1] Sim ou [2] Não: "))
            print(f"\nVocê tem as poções\n[0] Não ")
            for pocao in pocoes:
                print(pocao)
            opcaoPocao = int(input("Quer usar alguma: "))

            if opcaoPocao == 0:
                print("Você pode escolher um efeito status! Deseja usar algum:\n[0] Não")
                for st in status:
                    print(st)
                respostaStatus = int(input(": "))

                if respostaStatus == 1:
                    inimigo2 -= (HP * 5)//100
                elif respostaStatus == 2:
                    passar = 1
                elif respostaStatus == 3 or dfs < 3:
                    inimigo2DFS = 0
                    dfs += 1
                elif respostaStatus == 4:
                    if jogador1 <= jogador1_25:
                        jogador1 += (HP*30)//100


            if passar == 0:
                escolha = random.choice(["atacar", "curar"])
                inimigo2_dobroDano = random.choice(["sim", ''])
            else:
                print("Inimigo paralisado! ")
                passar -= passar

            if verdade1 == True:
                vezesPocoes +=1
                cura = curaPocao
                if vezesPocoes > 2:
                    verdade1 = False
                    vezesPocoes -= vezesPocao3

            elif verdade2 == True:
                vezesPocoes+=1
                danoSofrido = HP - jogador1
                danoPocao = inimigo2 - ((danoSofrido * 2) / 100)
                if vezesPocoes > 2:
                    verdade1 = False
                    danoPocao = 0
                    opcaoPocao -= opcaoPocao

            elif verdade3 == True:
                jogador1Dano = (jogador1Dano * 30) // 100
                if vezesPocoes > 2:
                    verdade3 = False
                    vezesPocoes -= vezesPocao3



            if acao == 1:
                if danoPocao != 0:
                    dano = jogador1Dano - jogador1DFS
                    dano += danoPocao
                else:
                    dano = jogador1Dano - jogador1DFS

    #OPÇÕES DE POCOES ---------------------------------------------------------------------------------------------------
                if opcaoPocao == 1:
                    curaPocao = random.randint(10, 50)
                    curaPocao = (curaPocao * 5) // 100
                    pocoes.remove("[1] Bate Ganha: Se o inimigo atacou, ganhe 5% de cura por duas rodadas")
                    roda = 0
                    verdade = True
                    verdade1 = True
                    opcaoPocao -= opcaoPocao

                elif opcaoPocao == 2:
                    if jogador1 != HP:
                        pocoes.remove("[2] Apanha Bate: Caso o inimigo atacar, cause 2% de dano adicional de volta por duas rodadas")
                        verdade2 = True


                elif opcaoPocao == 3:
                    jogador1Dano = (jogador1Dano*30)/100
                    pocoes.remove("[3] Aumentar poder de ataque por dois turnos")
                    verdade3 = True

                elif opcaoPocao == 4:
                    jogador1 = HP
                    pocoes.remove("[4] Receba todos os HP de volta, somente em uma rodada")

    #OPÇÕES DE POCOES ---------------------------------------------------------------------------------------------------
                if respostaDano == 1:
                    respostaDano += 1
                    jogador1_dobroDano = dano * 2
                    dano += jogador1_dobroDano
                    if dano < 0:
                        dano *= -1

                    inimigo2 -= dano
                    print(f"Você ataca! Inimigo perde {dano} HP.")
                else:
                    if dano < 0:
                        dano *= -1
                    dano = max(0, dano)
                    inimigo2 -= dano
                    print(f"Você ataca! Inimigo perde {dano} HP.")

                if escolha == "atacar" or vezes >2:
                    dano = inimigo2Dano - inimigo2DFS
                    if inimigo2 == "sim":
                        vezes = 0
                        inimigo2_dobroDano = dano * 2
                        dano += inimigo2_dobroDano
                        if dano < 0:
                            dano *= -1
                        dano = max(0, dano)
                        jogador1 -= dano
                        print(f"Inimigo ataca! Você perde {dano} HP.\n")
                    else:
                        if dano < 0:
                            dano *= -1
                        dano = max(0, dano)
                        jogador1 -= dano
                        print(f"Inimigo ataca! Você perde {dano} HP.\n")

                else:
                    vezes += 1
                    cura = random.randint(10, 50)
                    inimigo2 += cura
                    if inimigo2 >= HP:
                        inimigo2 = HP
                    print(f"O inimigo se cura em {cura} HP!\n")


            else:
                cura = random.randint(10, 50)
                jogador1 += cura

                if jogador1 < HP:
                    jogador1 = HP
                print(f"Você se cura em {cura} HP!\n")
                if escolha == "atacar" or vezes > 2:
                    vezes = 0
                    dano = inimigo2Dano - inimigo2DFS
                    if dano < 0:
                        dano *= -1
                    dano = max(0, dano)
                    jogador1 -= dano
                    print(f"Inimigo ataca! Você perde {dano} HP.\n")

                else:
                    vezes += 1
                    cura = random.randint(10, 50)
                    inimigo2 += cura
                    if inimigo2 >= HP:
                        inimigo2 = HP
                    print(f"O inimigo se cura em {cura} HP!\n")

                if inimigo2 <= 0:
                    print("Você ganhou!")
                    break
                elif jogador1 <= 0:
                    print("Você perdeu!")
                    break

            turno += 1
    else:
        HP = random.randint(200, 1000)
        jogador1 = HP
        inimigo2 = HP
        jogador1_25 = (jogador1 * 25) // 100
        inimigo2_25 = (inimigo2 * 25) // 100

        jogador1Dano = random.randint(1, 50)
        inimigo2Dano = random.randint(1, 50)

        jogador1DFS = random.randint(1, 50)
        inimigo2DFS = random.randint(1, 50)

        jogador1_dobroDano = 0
        if jogador1_dobroDano > 0:
            jogador1_dobroDano = 0
        inimigo2_dobroDano = ''

        while True:

            print("=== DUELO DE HERÓIS ===")
            print(f"\n--- Turno {turno} ---")
            print(f"=== VOCÊ ===\nHP: {jogador1}\nATQ: {jogador1Dano}      DEF: {jogador1DFS}\n")
            print(f"=== INIMIGO ===\nHP: {inimigo2}\nATQ: {inimigo2Dano}      DEF: {inimigo2DFS}")
            if passar1 != 0:
                acao = int(input("Sua vez\n[1] Atacar ou [2] Curar: "))
            else:
                print("Paralisado")
                passar1 -= passar1

            if respostaDano == 0:
                respostaDano = int(input("Deseja usar dobro de dano\n[1] Sim ou [2] Não: "))
            print(f"\nVocê tem as poções\n[0] Não ")
            for pocao in pocoes:
                print(pocao)
            opcaoPocao = int(input("Quer usar alguma: "))

            if opcaoPocao == 0:
                print("Você pode escolher um efeito status! Deseja usar algum:\n[0] Não")
                for st in status:
                    print(st)
                respostaStatus = int(input(": "))

            if respostaStatus == 1:
                inimigo2 -= (HP * 5) // 100
            elif respostaStatus == 2:
                passar = 1
            elif respostaStatus == 3 or dfs < 3:
                inimigo2DFS = 0
                dfs += 1
            elif respostaStatus == 4:
                if jogador1 <= jogador1_25:
                    jogador1 += (HP * 30) // 100

            if passar == 0:
                escolha = int(input("Deseja [1] Atacar [2] Curar: "))
                inimigo2_dobroDano = int(input("Deseja [1] Sim [2] Não: "))
                print(f"\nVocê tem as poções\n[0] Não ")
                for pocao in pocoes2:
                    print(pocao)
                opcaoPocao2 = int(input("Quer usar alguma: "))

                if opcaoPocao2 == 0:
                    print("Você pode escolher um efeito status! Deseja usar algum:\n[0] Não")
                    for st in status:
                        print(st)
                    respostaStatus2 = int(input(": "))

                if respostaStatus2 == 1:
                    jogador1 -= (HP * 5) // 100
                elif respostaStatus2 == 2:
                    passar1 = 1
                elif respostaStatus2 == 3 or dfs < 3:
                    jogador1DFSDFS = 0
                    dfs += 1
                elif respostaStatus2 == 4:
                    if inimigo2 <= inimigo2_25:
                        inimigo2 += (HP * 30) // 100
            else:
                print("Inimigo paralisado! ")
                passar -= passar

            if verdade1 == True:
                vezesPocoes +=1
                cura = curaPocao
                if vezesPocoes > 2:
                    verdade1 = False
                    vezesPocoes -= vezesPocao3

            elif verdade2 == True:
                vezesPocoes+=1
                danoSofrido = HP - jogador1
                danoPocao = inimigo2 - ((danoSofrido * 2) / 100)
                if vezesPocoes > 2:
                    verdade1 = False
                    danoPocao = 0
                    opcaoPocao -= opcaoPocao

            elif verdade3 == True:
                jogador1Dano = (jogador1Dano * 30) // 100
                if vezesPocoes > 2:
                    verdade3 = False
                    vezesPocoes -= vezesPocao3

            if acao == 1:
                if danoPocao != 0:
                    dano = jogador1Dano - jogador1DFS
                    dano += danoPocao
                else:
                    dano = jogador1Dano - jogador1DFS

                # OPÇÕES DE POCOES ---------------------------------------------------------------------------------------------------
                if opcaoPocao == 1:
                    curaPocao = random.randint(10, 50)
                    curaPocao = (curaPocao * 5) // 100
                    pocoes.remove("[1] Bate Ganha: Se o inimigo atacou, ganhe 5% de cura por duas rodadas")
                    roda = 0
                    verdade = True
                    verdade1 = True
                    opcaoPocao -= opcaoPocao

                elif opcaoPocao == 2:
                    if jogador1 != HP:
                        pocoes.remove("[2] Apanha Bate: Caso o inimigo atacar, cause 2% de dano adicional de volta por duas rodadas")
                        verdade2 = True


                elif opcaoPocao == 3:
                    jogador1Dano = (jogador1Dano*30)/100
                    pocoes.remove("[3] Aumentar poder de ataque por dois turnos")
                    verdade3 = True

                elif opcaoPocao == 4:
                    jogador1 = HP
                    pocoes.remove("[4] Receba todos os HP de volta, somente em uma rodada")

                # OPÇÕES DE POCOES ---------------------------------------------------------------------------------------------------
                if respostaDano == 1:
                    respostaDano += 1
                    jogador1_dobroDano = dano * 2
                    dano += jogador1_dobroDano
                    if dano < 0:
                        dano *= -1

                    inimigo2 -= dano
                    print(f"Você ataca! Inimigo perde {dano} HP.")
                else:
                    if dano < 0:
                        dano *= -1
                    dano = max(0, dano)
                    inimigo2 -= dano
                    print(f"Você ataca! Inimigo perde {dano} HP.")

                if escolha == 1:
                    dano = inimigo2Dano - inimigo2DFS
                    if inimigo2 == 1:

                        inimigo2_dobroDano = dano * 2
                        dano += inimigo2_dobroDano
                        if dano < 0:
                            dano *= -1
                        dano = max(0, dano)
                        jogador1 -= dano
                        print(f"Inimigo ataca! Você perde {dano} HP.\n")
                    else:
                        if dano < 0:
                            dano *= -1
                        dano = max(0, dano)
                        jogador1 -= dano
                        print(f"Inimigo ataca! Você perde {dano} HP.\n")

                else:

                    cura = random.randint(10, 50)
                    inimigo2 += cura
                    if inimigo2 >= HP:
                        inimigo2 = HP
                    print(f"O inimigo se cura em {cura} HP!\n")


            else:
                cura = random.randint(10, 50)
                jogador1 += cura

                if jogador1 < HP:
                    jogador1 = HP
                print(f"Você se cura em {cura} HP!\n")
                if escolha == 1:
                    vezes = 0
                    dano = inimigo2Dano - inimigo2DFS
                    if dano < 0:
                        dano *= -1
                    dano = max(0, dano)
                    jogador1 -= dano
                    print(f"Inimigo ataca! Você perde {dano} HP.\n")

                else:
                    vezes += 1
                    cura = random.randint(10, 50)
                    inimigo2 += cura
                    if inimigo2 >= HP:
                        inimigo2 = HP
                    print(f"O inimigo se cura em {cura} HP!\n")

                if inimigo2 <= 0:
                    print("Você ganhou!")
                    break
                elif jogador1 <= 0:
                    print("Você perdeu!")
                    break

            turno += 1