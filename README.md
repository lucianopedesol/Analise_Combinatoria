# Analise_Combinatoria
 
 Questão base utilizada para criar o algoritimo.
 
 
Uma estante de biblioteca tem 16 livros: 11 exemplares o livro "Combinatória é fácil" e 5 exemplares de "Combinatória não é difícil". Considere que os livros com mesmo título sejam indistinguíveis. Determine de quantas maneiras diferentes podemos dispor os 16 livros na estante de modo que dois exemplares de "Combinatória não é difícil" nunca estejam juntos.

Solução:
Colocando os 11 livros de “Combinatória é fácil” primeiramente deixando um espaço entre eles, temos: 

___[]CF[]CF[]CF[]CF[]CF[]CF[]CF[]CF[]CF[]CF[]CF[]___

Há 12 espaços vazios onde os livros “Combinatória não é difícil” podem entrar sem ficarem juntos. O problemas se resume a escolher 5 lugares dentre os 12 disponíveis: 


C(n,k) = n!/(k!(n-k)!)

C(12, 5) = 12!/(5!(12-5)!) = 792 formas


Codigo para solução dos calculos:
https://github.com/lucianopedesol/Analise_Combinatoria/blob/master/estatistica.py
