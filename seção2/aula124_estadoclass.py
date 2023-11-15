class Camera:
    def __init__(self, nome, lente, filmando=False):
        self.nome = nome
        self.lente = lente
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print('Já está filmando.')
            return

        print(f'{self.nome} está filmando com sua lente de {self.lente}...')
        self.filmando = True

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode tirar foto enquanto filma!')
            return
        
        print(f'{self.nome} tirou uma foto!')



    # def trocar_lente(self):
    #     entrada = input('Deseja trocar de lente?')
    #     if entrada == 'sim':
    #         print(f'Agora você está com a lente {}.')
    #     elif entrada ==
    
c1 = Camera('Canon', '9mm')

c2 = Camera('Sony', '12mm')

c1.fotografar()
c1.filmar()        
print(c1.filmando)
print(c2.filmando)
c1.fotografar()
c1.filmar()