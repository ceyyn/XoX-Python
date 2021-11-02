from os import system
red , vars, color = "\033[31m", "\033[0m","\033[92m"
class XOX:
    def __init__(self):
        self.Degiskenler()
        self.ilk_islemler()
    def Degiskenler(self):
        self.tahta = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

    def tahtayi_ciz(self):
        system("cls")
        print('  {}  |  {}  |  {}  '.format(self.tahta[1],self.tahta[2],self.tahta[3]))
        print('—————|—————|—————')
        print('  {}  |  {}  |  {}  '.format(self.tahta[4],self.tahta[5],self.tahta[6]))
        print('—————|—————|—————')
        print('  {}  |  {}  |  {}  '.format(self.tahta[7],self.tahta[8],self.tahta[9]))
    def Galibiyet(self):
        if self.tahta[1] == self.tahta[2] and self.tahta[2] == self.tahta[3] and self.tahta[1] != ' ':
            self.galibiyet = True
        elif self.tahta[4] == self.tahta[5] and self.tahta[5] == self.tahta[6] and self.tahta[4] != ' ':
            self.galibiyet = True
        elif self.tahta[7] == self.tahta[8] and self.tahta[8] == self.tahta[9] and self.tahta[7] != ' ':
            self.galibiyet = True
        
        elif self.tahta[1] == self.tahta[4] and self.tahta[4] == self.tahta[7] and self.tahta[1] != ' ':
            self.galibiyet = True
        elif self.tahta[2] == self.tahta[5] and self.tahta[5] == self.tahta[8] and self.tahta[2] != ' ':
            self.galibiyet = True
        elif self.tahta[3] == self.tahta[6] and self.tahta[6] == self.tahta[9] and self.tahta[3] != ' ':
            self.galibiyet = True
        
        elif self.tahta[1] == self.tahta[5] and self.tahta[5] == self.tahta[9] and self.tahta[1] != ' ':
            self.galibiyet = True
        elif self.tahta[3] == self.tahta[5] and self.tahta[5] == self.tahta[7] and self.tahta[3] != ' ':
            self.galibiyet = True
        
        elif self.tahta[1] != ' ' and self.tahta[2] != ' ' and self.tahta[3] != ' ' and self.tahta[4] != ' ' and self.tahta[5] != ' ' and self.tahta[6] != ' ' and self.tahta[7] != ' ' and self.tahta[8] != ' ' and self.tahta[9] != ' ':
            self.beraberlik = True
        else:
            self.galibiyet = False
            self.beraberlik = False
        if self.galibiyet == True or self.beraberlik == True:
            self.oyun_sonu = True
    def ilk_islemler(self):
        system('cls')
        print("———Welcome to The XOX Game———")
        P1 = input("[X] Enter the first Player's name : ").upper()
        P2 = input("[O] Enter the second Player's name : ").upper()
        print(red + f"———{P1}[X]———{P2}[O]———" + vars)
        self.oyuncu = 1
        self.oyun_sonu = False
        while self.oyun_sonu == False:

            self.tahtayi_ciz()
            
            if self.oyuncu % 2 == 0:
                print(f"Next Player {P2}")
            else:
                print(f"Next Player {P1}")
            self.soru = int(input("Please enter a number among 1-9 to mark it."))
            if self.oyuncu % 2 == 0:
                self.isaret = 'O'
            else:
                self.isaret = 'X'
            if self.tahta[self.soru] == ' ':
                    self.tahta[self.soru] = self.isaret
            else:
                self.oyuncu += 1
                system('cls')
                print("Nice Try."+red)
                if self.oyuncu % 2 == 0:
                    
                    print(f"{P2} [O] KAZANDI."+vars)
                else:
                    print(f"{P1} [X] KAZANDI."+vars)
                self.oyun_sonu = True
                break

            self.oyuncu +=1
            self.tahtayi_ciz()
            self.Galibiyet()


        if self.galibiyet == True:
            self.oyuncu -= 1

            if self.oyuncu % 2 == 0:    print(red + f"{P2} [O] KAZANDI." + vars)
            else:   print(red + f"{P1} [X] KAZANDI." + vars)

        elif self.beraberlik == True:
            print(red + "BERABERE." + vars)


XOX()

