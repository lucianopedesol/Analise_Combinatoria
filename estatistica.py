import functools
import operator

print(
    "\n\nGerador de questões COMBINATÓRIAS, onde a ordem das escolhas não importa. Do tipo:"
)

print(
    '\n\nUma estante de biblioteca tem {qtd_livros} livros: {qtd_livro_EF} exemplares do livro "Combinatória é fácil" \n'
    'e {qtd_livro_NED} exemplares de "Combinatória não é difícil". Considere que os livros com mesmo título sejam \n'
    'indistinguíveis. Determine de quantas maneiras diferentes podemos dispor os {qtd_livros} livros na estante de modo que \n'
    'dois exemplares de "Combinatória não é difícil" nunca estejam juntos.'
)

quest = 1

continuar = True
while continuar:

    print("\n\nInsira os dados abaixo:")

    n = input("\n\nInsira o valor da quantidade de livros, de modelo determinado, que tem o maior volume: {qtd_livro_EF} \n")

    k = input("Insira o valor da quantidade de livros, de modelo determinado, que não pode ficar um do lado do outro: {qtd_livro_NED}\n")

    if not k.isnumeric() or not n.isnumeric():
        print("\n\n***Você deve inserir números validos, não é permitido letras ou números flutuantes!***\n\n")
        continue
    else:
        n = int(n)
        k = int(k)

        if n < k or k == 0:
            print("\n\n***Não é possivel satisfazer o calculo, tente novamento com novos valores.***\n\n")
            continue


    print(f" \n\nQuestão ({quest})")
    print(
        f'Uma estante de biblioteca tem {(n + k)} livros: {n} exemplares o livro "Combinatória é fácil" '
        f'\ne {k} exemplares de "Combinatória não é difícil". Considere que os livros com mesmo título sejam indistinguíveis. '
        f'\nDetermine de quantas maneiras diferentes podemos dispor os {(n + k)} livros na estante '
        f'\nde modo que dois exemplares de "Combinatória não é difícil" nunca estejam juntos.'
    )
    print("\nAguarde os valores serem gerados para calculo.\n")

    quest += 1

    n = n + 1
    dif = n - k

    total_dif = list(range(1, dif + 1))
    total_n = list(range(1, n + 1))
    total_k = list(range(1, k + 1))

    def fatorial(arg):
        replace_fatorial = str(arg).replace(",", "*")
        nova_lista = "".join(replace_fatorial)
        return nova_lista

    def produtoFatorial(arg):
        arg_produto = functools.reduce(operator.mul, arg)
        return arg_produto


    dif_fatorial = fatorial(total_dif)
    dif_produto = produtoFatorial(total_dif)

    n_fatorial = fatorial(total_n)
    n_produto = produtoFatorial(total_n)

    k_fatorial = fatorial(total_k)
    k_produto = produtoFatorial(total_k)

    resultado = n_produto / (k_produto * (dif_produto))

    print("\nResolução:\n")

    print(f"\nC(n,k)= (n+1)!/(k!*((n+1)-k)!")
    print(f"\nC(n,k)= {n}!/({k}!*({n}-{k})!)")
    print(
        f"\n{n_fatorial} / ({k_fatorial}*{dif_fatorial})")

    print(f"\nC(n,k)= {n_produto}/({k_produto}*({dif_produto})) = {resultado}")

    print(
        f"\n\n Existem {resultado} maneiras possiveis de se organizar esses livros")

    novaQuestao = True
    while novaQuestao:
        resp = input("\n\nDeseja criar outra questão? (Y/N) \n")

        escolha = resp.upper()

        if escolha == "Y":
            novaQuestao = False
        elif escolha == "N":
            continuar = False
            novaQuestao = False
        else:
            print("\n\n***Você precisa escolher Y(sim) ou N(não)***\n\n")
            continue
