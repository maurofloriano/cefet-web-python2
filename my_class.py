class Autor:
    def __init__(self, primeiro_nome, ultimo_nome, data_nascimento, nome_do_meio=""):
        self.primeiro_nome = primeiro_nome
        self.ultimo_nome = ultimo_nome
        self.data_nascimento = data_nascimento
        self.nome_do_meio = nome_do_meio
    
    @property
    def nome_como_citado(self):
        return f'{self.ultimo_nome.upper()}, {self.primeiro_nome[0].upper()}'
    
    def __str__(self):
        return f'Autor: {self.nome_como_citado}'

class Livro:
    def __init__(self, titulo, ano, autores=[]):
        self.titulo = titulo
        self.ano = ano
        self.autores = autores
    
    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, val):
        if not val:
            raise ValueError("Titulo não pode ser vázio")
        self._titulo = val

    def __str__(self):
        return f'Livro: {self.titulo}'

class Biblioteca:
    def __init__(self, livros):
        self.livros = livros

    @property
    def livros_por_autor(self):
        livro_autor = {}
        for livro in self.livros:
            for autor in livro.autores:
                if not livro_autor.get(autor.nome_como_citado):
                    livro_autor[autor.nome_como_citado] = []
                livro_autor[autor.nome_como_citado].append(livro._titulo)
        return livro_autor

    def __str__(self):
        return 'Biblioteca: '