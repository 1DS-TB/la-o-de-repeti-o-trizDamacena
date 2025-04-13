import random
from random import randint

from Tools.scripts.summarize_stats import emit_specialization_overview

vez = 1
turno = 1

print("======= MENU =======")
escolha = int(input("Deseja jogar:\n[1] Sim\n[2] Não:\n"))
if escolha == 2:
    print("Okay")
else:

    HP = random.randint(200, 1000)
    jogador1 = HP
    inimigo2 = HP

    jogador1Dano = random.randint(1, 50)
    inimigo2Dano = random.randint(1, 50)

    jogador1DFS = random.randint(1, 50)
    inimigo2DFS = random.randint(1, 50)
    while True:

        if vez == 1:
            vez += 1
            print("=== DUELO DE HERÓIS ===")
            print(f"\n--- Turno {turno} ---")
            print(f"=== VOCÊ ===\nHP: {jogador1}\nATQ: {jogador1Dano}      DEF: {jogador1DFS}\n")
            print(f"=== INIMIGO ===\nHP: {inimigo2}\nATQ: {inimigo2Dano}      DEF: {inimigo2DFS}")
            acao = int(input("Sua vez: [1] Atacar ou [2] Curar:\n "))
            if acao == 1:
                dano = jogador1Dano - jogador1DFS
                if dano < 0:
                    dano *= -1
                dano = max(0, dano)
                inimigo2 -= dano
                print(f"Você ataca! Inimigo perde {dano} HP.\n")

            else:
                cura = random.randint(10, 50)
                jogador1 += cura
                if jogador1 > HP:
                    jogador1 = HP
                    print(f"Você se cura em {cura} HP!\n")

            if inimigo2 <= 0:
                print("Você ganhou!")
            turno+=1

        else:
            print("=== DUELO DE HERÓIS ===")
            print(f"\n--- Turno {turno} ---")
            print(f"=== VOCÊ ===\nHP: {jogador1}\nATQ: {jogador1Dano}      DEF: {jogador1DFS}\n")
            print(f"=== INIMIGO ===\nHP: {inimigo2}\nATQ: {inimigo2Dano}      DEF: {inimigo2DFS}")
            escolha = random.choice(["atacar", "curar"])
            print(f"O inimigo escolhe: `{escolha}")
            if escolha == "atacar":
                dano = inimigo2Dano - inimigo2DFS
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
                    inimigo2 += cura
                    print(f"O inimigo se cura em {cura} HP!\n")


            vez -= 1
            turno += 1
