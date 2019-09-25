class Pessoa:
    def __init__(self, nome=None, idade=35): # se utilizar Alt+Enter o pycharm ja adiciona altomaticamente o atributo a Self
        self.idade = idade
        self.nome = nome #Atributo de passagem de parametros
    def cumprimentar(self):
        return f'Olá {id(self)}'
if __name__ == '__main__':
    p = Pessoa('Luciano', idade=40)
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome, p.idade)
    p.nome = 'willian' # passando o nome através da passagem de atributo nome
    print(p.nome)

