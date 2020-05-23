# Analise_Combinatoria
 
 
""" importing functools for reduce()"""
import functools

"""importing operator for operator functions"""
import operator


print(
    "Gerador de questões COMBINATÓRIAS, onde a ordem das escolhas não importa. Do tipo:"
)

print(
    '\n\n Uma estante de biblioteca tem {qtd_livros} livros: {qtd_livro_EF} exemplares o livro "Combinatória é fácil" e {qtd_livro_NED} exemplares de "Combinatória não é difícil". Considere que os livros com mesmo título sejam indistinguíveis. Determine de quantas maneiras diferentes podemos dispor os {qtd_livros} livros na estante de modo que dois exemplares de "Combinatória não é difícil" nunca estejam juntos.'
)


quest = 1
qt = 1

d = True
while (d):

    print("\n\n Insira os dados abaixo:")

    n = input(
        "\n\nInsira o valor da quantidade de livros, de modelo determinado, que tem o maior volume: {qtd_livro_EF} \n"
    )

    k = input(
        "Insira o valor da quantidade de livros, de modelo determinado, que não pode ficar um do lado do outro: {qtd_livro_NED}\n"
    )

    if not k.isnumeric() or not n.isnumeric():
        print(
            "\n\n***Você deve inserir números validos, não é permitido letras ou números flutuantes!***\n\n"
        )
        continue
    else:
        n = int(n)
        k = int(k)
        kk = k
        nn = n + 1
        if n < k or k == 0:
            print(
                "\n\n***Não é possivel satisfazer o calculo, tente novamento com novos valores.***\n\n"
            )
            continue

    qt = qt - 1
    quest = quest - (qt)
    print(f" \n\nQuestão ({quest})")
    print(
        f'Uma estante de biblioteca tem {(nn + kk)-1} livros: {nn-1} exemplares o livro "Combinatória é fácil" e {kk} exemplares de "Combinatória não é difícil". Considere que os livros com mesmo título sejam indistinguíveis. Determine de quantas maneiras diferentes podemos dispor os {(nn + kk)-1} livros na estante de modo que dois exemplares de "Combinatória não é difícil" nunca estejam juntos.'
    )
    print("\nAguarde os valores serem gerados para calculo.\n")
    quest += 1
    qt += 1

    dif = nn - k
    total_dif = list(range(1, dif + 1))

    dif_fat = str(total_dif).replace(",", "*")
    dif_fat = "".join(dif_fat)
    proddif = functools.reduce(operator.mul, total_dif)

    total_n = list(range(1, nn + 1))

    n_fat = str(total_n).replace(",", "*")
    n_fat = "".join(n_fat)
    n = functools.reduce(operator.mul, total_n)

    total_k = list(range(1, k + 1))

    k_fat = str(total_k).replace(",", "*")
    k_fat = "".join(k_fat)
    k = functools.reduce(operator.mul, total_k)

    comb = n / (k * (proddif))

    print("\nResolução:\n")

    print(f"\n\nC(n,k)= {nn}!/({kk}!*({nn}-{kk})!")

    print(
        f"\n{n_fat}\n______________________________________________________________________________________________\n({k_fat}*{dif_fat})")

    print(f"\n\nC(n,k)= {n}/({k}*({proddif})) = {comb}")

    print(
        f"\n\n Existem {comb} maneiras possiveis de se organizar esses livros")

    cont = True
    while (cont):
        resp = input("\n\nDeseja criar outra questão? (Y/N) \n")

        x = resp.upper()

        if x == "Y":
            cont = False
        elif x == "N":
            d = False
            cont = False
        else:
            print("\n\n***Você precisa escolher Y(sim) ou N(não)***\n\n")
            continue
