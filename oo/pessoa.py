class Pessoa:
    def __init__(self, nome=None, idade=53):
        self.nome = nome
        self.idade = idade
    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa('André')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Vladimir'
    print(p.nome)
    print(p.idade)
