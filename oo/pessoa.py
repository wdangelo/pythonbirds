class Pessoa:
    olhos = 2  # atributo defalt ou atributo de classe
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
    del  luciano.filhos
    luciano.olhos = 1
    del luciano.olhos
    print(luciano.__dict__)#mostra os atributos de instancia do objeto
    print(renzo.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(renzo.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(renzo.olhos))

