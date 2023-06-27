with open("dados.txt", "w") as arquivo:

    arquivo.write("Counter-Strike é melhor do que Valorant.")
    arquivo.write("O correto é 'bolacha'.")



""" 1. with open("dados.txt", "w") as arquivo:: Aqui, estamos usando a palavra-chave reservada with, uma construção em Python que garante que o arquivo seja fechado corretamente após o seu uso. Estamos abrindo o arquivo chamado "dados.txt" em modo de escrita ("w"), que permite escrever no arquivo. Se o arquivo não existir, ele será criado. A variável arquivo é associada ao arquivo aberto. Veja que usamos esse with de um jeito bem parecido com o if/elif/else, for ou while.

        1.arquivo.write("Counter-Strike é melhor do que Valorant."): Nesta linha, estamos chamando o método write() na variável arquivo. Isso permite escrever o conteúdo especificado entre parênteses no arquivo aberto. No caso, estamos escrevendo a string "Counter-Strike é melhor do que Valorant." no arquivo.

        2.arquivo.write("O correto é 'bolacha'."): Na próxima linha, chamamos novamente o método write() para adicionar mais uma frase ao arquivo. Aqui, estamos escrevendo a frase "O correto é 'bolacha'.".

        3.O bloco with é encerrado e, automaticamente, o arquivo é fechado. Isso é importante para garantir que os recursos do sistema operacional associados ao arquivo sejam liberados corretamente, e que não apareça algum tipo de mensagem dizendo que você não poderia modificar o seu arquivo porque ele estaria em uso. """