from my_class import Autor, Livro, Biblioteca

def main():
    autor1 = Autor('Silvana', 'dos Santos', '31/08/1966', nome_do_meio='Azambuja')
    autor2 = Autor('Mauro Floriano','dos Santos', '05/05/1994')
    autor3 = Autor('Deborah','Oliveira', '21/11/1994', nome_do_meio='Melo')

    try:
        livro1 = Livro(titulo='', ano=2015, autores=[autor2, autor3])
    except ValueError as e:
        print(f'Erro ao criar livro: {e}')
    livro2 = Livro(titulo='Livro 2', ano=2000, autores=[autor1, autor3])
    livro3 = Livro(titulo='Livro 3', ano=1999, autores=[autor1, autor2])
    livro4 = Livro(titulo='Livro 4', ano=1999, autores=[autor3, autor2, autor1])

    biblioteca = Biblioteca(livros=[livro2, livro3, livro4])

    print(autor1)
    print(autor2)
    print(autor3)
    print(livro2)
    print(livro3)
    print(livro4)
    print(biblioteca.livros_por_autor)


if __name__ == '__main__':
    main()