class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35): # se utilizar Alt+Enter o pycharm ja adiciona altomaticamente o atributo a Self
        self.idade = idade
        self.nome = nome #Atributo de passagem de parametros
        self.filhos = list(filhos)#atributo complexo
    def cumprimentar(self):
        return f'Olá {id(self)}'
if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
    luciano = Pessoa(renzo, nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = 'Ramalho' #atributo dinamico
    print(luciano.__dict__)
    print(renzo.__dict__)

