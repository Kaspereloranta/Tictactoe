""" TIE-02101 OHJELMOINTI 1: Johdatus Ohjelmointiin
    Tehtävä 13.10 Graafinen käyttöliittymä Tkinterillä
    Kasper Eloranta, kasper.eloranta@tuni.fi

    Ristinollapeli, jota pelataan 3x3 pelialustalla ja pelaajia on kaksi.
      Pelissä ideana on saada pelialustaan kolmen suora omia pelimerkkejä
    ennen vastapelaajaa. Kolmen suora voidaan saada vaaka- tai pystyriveille
    sekä myös viistoon vas.alanurkasta oik.ylänurkkaan tai vas.ylänurkasta
    oik.alanurkkaan.
      Käyttöliittymässä 3x3 pelialusta koostuu yhdeksästä
    Button -komponentista. Pelin alkaessa kaikissa yhdeksässä napissa on
    oletuksena tyhjä kuva. Painamalla tällaista nappia, muuttuu napin kuvake
    sen mukaiseksi kumman pelaajan vuoro painamishetkellä on. Pelaajan yksi
    pelimerkki/pelikuvake on risti, ja pelaajan kaksi nolla. Mikäli jo kerran
    painettua nappia yritetään samalla pelikierroksella painaa uudestaan,
    mitään ei tapahdu vaan kuva pysyy ennallaan. Kun jompikumpi pelaajista
    saa kolmen suoran, ohjelma luo "We have a winner!" -nimisen ponnahdusik-
    kunan, jossa kerrotaan kuka on voittanut. Pelin päättyessä tasapeliin
    ohjelma luo "Draw!" -nimisen ponnahdusikkunan, jossa kerrotaan pelin
    päättyneen tasapeliin. Ponnahdusikkunoissa "Ok" -napin painalluksen
    jälkeen ponnahdusikkuna sulkeutuu ja uusi pelikierros alkaa.
      Käyttöliittymän yläosassa on kaksi Label-komponenttia. Toisessa lukee
    teksti "Turn:" ja toisessa on kuva vuorossa olevan pelaajan pelimerkistä.
    Tämä kuva vaihtuu aina vuoron vaihtuessa, jolloin pelaajat näkevät
    käyttöliittymästä suoraan kumman vuoro on.
      Pelialustan oikealla puolella on myös muutamat Label-komponentit.
    Ylimmässä Labelissa lukee "TOTAL WINS:" ja tämän alapuolella olevissa
    Labeleissa pidetään kirjaa kummankin pelaajan voitetuista kierroksista
    yhteensä.
      Pelialustan alapuolella on vielä kolme Button -komponenttia. Ensimmäises-
    sä napissa lukee "Quit". Painamalla tätä nappia käyttöliittymäikkuna
    sulkeutuu ja ohjelman suoritus päättyy. Keskimmäisessä lukee teksti
    "New game". Tätä nappia painamalla voidaan keskeneräinen pelikierros
    aloittaa alusta, jos siltä tuntuu.
      Kolmannessa napissa lukee teksti "Reset". Tämä nappi toimii lähes samoin
    kuin "New game" nappi, mutta tämän lisäksi nappulaa painettaessa ohjelma
    nollaa pelaajien tiedot aiemmin kertyneistä voitoista. Resetillä voidaan
    siis aloittaa pelit täysin puhtaalta pöydältä ilman, että ohjelmaa
    tarvitsee sulkea ja käynnistää uudestaan.
      Tähtäsin tällä projektilla skaalautuvaan käyttöliittymään.
    """


from tkinter import *
from tkinter import messagebox


PICS = ["empty.gif", "cross.gif" , "zero.gif"]
SIZE = 3
PLAYERS = 2

class TicTacToe:

    """ Luokka TicTacToe, jonka avulla luodaan graafinen käyttöliittymä
    ristinollapelille, jonka säännöt ja sen sisältämien komponenttien toiminta
    on kuvattu kommenteissa tämän kooditiedoston alussa."""

    def __init__(self):

        """ Rakentaja-metodi, joka luo graafisen käyttöliittymän ulkoasun
        kaikki komponentit ja asettaa ne paikalleen käyttöliittymään. """

        self.__window = Tk()
        self.__window.title("Tic-Tac-Toe")
        self.__turn = 1
        self.__buttons_in_use = [True] * SIZE**2

        self.__pics = []
        for picture in PICS:
            pic = PhotoImage(file=picture)
            self.__pics.append(pic)
        self.__buttonimage = [self.__pics[0]] * SIZE**2

        self.__buttons = []
        k = 0
        for i in range(SIZE):
            for n in range(SIZE):

                if k == 0:
                    new_button = Button(self.__window, image=self.__pics[0],
                                 state=NORMAL,command = self.press_button_0)
                    new_button.grid(row = i+1, column = n)
                    self.__buttons.append(new_button)

                if k == 1:
                    new_button = Button(self.__window, image=self.__pics[0],
                                        state=NORMAL,
                                        command=self.press_button_1)
                    new_button.grid(row=i + 1, column=n)
                    self.__buttons.append(new_button)

                if k == 2:
                    new_button = Button(self.__window, image=self.__pics[0],
                                        state=NORMAL,
                                        command=self.press_button_2)
                    new_button.grid(row=i + 1, column=n)
                    self.__buttons.append(new_button)

                if k == 3:
                    new_button = Button(self.__window, image=self.__pics[0],
                                        state=NORMAL,
                                        command=self.press_button_3)
                    new_button.grid(row=i + 1, column=n)
                    self.__buttons.append(new_button)

                if k == 4:
                    new_button = Button(self.__window, image=self.__pics[0],
                                        state=NORMAL,
                                        command=self.press_button_4)
                    new_button.grid(row=i + 1, column=n)
                    self.__buttons.append(new_button)

                if k == 5:
                    new_button = Button(self.__window, image=self.__pics[0],
                                        state=NORMAL,
                                        command=self.press_button_5)
                    new_button.grid(row=i + 1, column=n)
                    self.__buttons.append(new_button)

                if k == 6:
                    new_button = Button(self.__window, image=self.__pics[0],
                                        state=NORMAL,
                                        command=self.press_button_6)
                    new_button.grid(row=i + 1, column=n)
                    self.__buttons.append(new_button)

                if k == 7:
                    new_button = Button(self.__window, image=self.__pics[0],
                                        state=NORMAL,
                                        command=self.press_button_7)
                    new_button.grid(row=i + 1, column=n)
                    self.__buttons.append(new_button)

                if k == 8:
                    new_button = Button(self.__window, image=self.__pics[0],
                                        state=NORMAL,
                                        command=self.press_button_8)
                    new_button.grid(row=i + 1, column=n)
                    self.__buttons.append(new_button)

                k += 1

        self.__wins = [0] * PLAYERS
        self.__totalwins = []
        self.__winlabels = []

        for i in range(PLAYERS):
            wincount = Label(self.__window, text="Player {:.0f}".format(i+1))
            wins = Label(self.__window, text = 0)
            wincount.grid(row = SIZE//2+1 + i, column = SIZE)
            wins.grid(row = SIZE//2+1 + i , column = SIZE + 1 )
            self.__winlabels.append(wincount)
            self.__totalwins.append(wins)

        self.__wincounter = Label(self.__window,text = "TOTAL WINS:" )
        self.__turnlabel = Label(self.__window, text = "Turn:")
        self.__turnmark = Label(self.__window, image=self.__pics[self.__turn])
        self.__resetbutton = Button(self.__window,text="Reset",
                                    command = self.reset)
        self.__newgamebutton = Button(self.__window, text="New game",
                                      command = self.new_game)
        self.__quitbutton = Button(self.__window, text= "Quit" ,
                                   command = self.quit)

        self.__wincounter.grid(row = SIZE // 2, column = SIZE)
        self.__turnlabel.grid(row=0, column=SIZE // 2 - 1)
        self.__turnmark.grid(row=0, column=SIZE // 2)
        self.__resetbutton.grid(row=SIZE + 2, column=(SIZE + 2) // 2)
        self.__newgamebutton.grid(row = SIZE+2, column=(SIZE+2)//2-1)
        self.__quitbutton.grid(row = SIZE + 2 , column = 0)

    def start(self):

        """ Metodi start, joka käynnistää graafisen käyttöliittymän."""

        self.__window.mainloop()

    def quit(self):

        """ Metodi quit, joka sulkee käynnistetyn graafisen käyttöliitymän."""

        self.__window.quit()

    def new_game(self):

        """ Metodi new_game, jota self.__newgamebutton kutsuu tätä nappia
        painettaessa. Metodi tyhjentää ja nollaa pelialustan, mutta säilyttää
        tiedon pelaajien aikaisemmista voitetuista peleistä. """

        self.__buttons_in_use = [True] * SIZE ** 2
        self.__buttonimage = [self.__pics[0]] * SIZE ** 2
        self.__turn = 1
        self.__turnmark.configure(image=self.__pics[self.__turn])

        for i in self.__buttons:
            i.configure(image=self.__pics[0])

    def reset(self):

        """ Metodi reset, jota self.__resetbutton kutsuu ja joka alustaa pelin
        kokonaan uudelleen. Kutsuu aluksi luokan toista metodia new_game:a.
        Tämän lisäksi metodi nollaa tiedot pelaajien aikaisemmin voitettujen
        pelien määrästä."""

        self.new_game()
        self.__wins = [0] * PLAYERS

        for i in self.__totalwins:
            i.configure(text=0)

    def press_button(self , number):

        """ Metodi press_button, joka ottaa parametriaan painettavan napin
        numeron. Napit on numeroitu 0-8 numeroin siten, että ensimmäisen rivin
        vasemman puoleisen napin numero on 0, keskimmäisen 1, oikean puoleisen
        2 jne. Funktio tarkastaa ensin onko kyseinen nappi vielä käytettävissä,
        eli siis onko tätä nappia painettu jo aiemmin samalla kierroksella.
        Jos nappi on käytettävissä, funktio vaihtaa tämän napin kuvakkeeksi
        vuorossa olevan pelaajan pelimerkin kuvan ja poistaa napin käytössä
        olevien joukosta. Lopuksi funktio kutsuu metodia check_win, joka
        tarkastaa mahdollisen voiton. Jos peli ei ratkea, funktio vaihtaa
        vuoron toiselle pelaajalle. """

        if self.__buttons_in_use[number] == True:

            self.__buttons[number].configure(image=self.__pics[self.__turn])
            self.__buttonimage[number] = self.__pics[self.__turn]
            self.__buttons_in_use[number] = False

            if self.check_win() == False:

                if self.__turn == 1:
                    self.__turn = 2
                else:
                    self.__turn = 1

                self.__turnmark.configure(image=self.__pics[self.__turn])


    """ Seuraavat 9 metodia kutsuvat kaikki metodia press_button, mutta eri
    parametrin number -arvoilla. Parametrit ovat nyt nappien numeroita, ja 
    käyttöliittymässä pelinapit kutsuvat painettaessa seuraavia yhdeksää eri 
    metodia, kukin omaa lukuaan vastaavaa. """

    def press_button_0(self):
        self.press_button(0)

    def press_button_1(self):
        self.press_button(1)

    def press_button_2(self):
        self.press_button(2)

    def press_button_3(self):
        self.press_button(3)

    def press_button_4(self):
        self.press_button(4)

    def press_button_5(self):
        self.press_button(5)

    def press_button_6(self):
        self.press_button(6)

    def press_button_7(self):
        self.press_button(7)

    def press_button_8(self):
        self.press_button(8)

    def check_win(self):

        """ Metodi check_win, jota kutsutaan aina kun pelilaudalle lisätään
        uusi pelimerkki. Metodi tarkastaa onko peli mahdollisesti ratkennut
        eli onko siis pelilaudalle muodostunut haluttu kolmen jono samoista
        pelimerkeistä. Pelin ratketessa funktio luo "We have a winner!"
        -nimisen ponnahdusikkunan, jossa kerrotaan kumpi pelaajista on
        voittanut kyseisen kierroksen. Kun ponnahdusikkunassa painaa "Ok",
        metodin suoritus jatkuu. Lopuksi metodi lisää pelialustan oikealla
        puolella oleviin labeleihin tiedon voitetusta kierroksesta voittavalle
        pelaajalle. Tämän jälkeen metodi kutsuu metodia new.game, jolloin
        uusi pelikierros alkaa. Metodi antaa paluuarvonaan True tai False
        riippuen siitä onko voittaja selvillä. (Jos True, niin peli on
        ratkennut). Mahdollisessa tasapelitilanteessa, jossa pelilauta on
        siis täynnä, mutta voitto ei ratkea, metodi luo ponnahdusikkunan,
        jossa kerrotaan pelin päättyneen tasapeliin. Tämän jälkeen metodi
        kutsuu metodia new.game.
        """

        draw = False
        win = False
        LIST = [0, 1, 2]

        for i in LIST:

            if self.__buttonimage[3*i] != self.__pics[0] and \
                   self.__buttonimage[3*i] == self.__buttonimage[3*i+1] \
                    == self.__buttonimage[3*i+2]:

                win = True

            if self.__buttonimage[i] != self.__pics[0] and \
                    self.__buttonimage[i] == self.__buttonimage[i+3] \
                    == self.__buttonimage[i +6]:

                win = True

        if self.__buttonimage[0] != self.__pics[0] and self.__buttonimage[0]==\
            self.__buttonimage[4] == self.__buttonimage[8]:

            win = True

        if self.__buttonimage[2] != self.__pics[0] and self.__buttonimage[2]==\
            self.__buttonimage[4] == self.__buttonimage[6]:

            win = True

        if win != True and self.__buttons_in_use == [False] * SIZE**2:

            string = "The game ended with a draw!"
            messagebox.showinfo("Draw!",string)
            self.new_game()
            draw = True

        if win == True:

            string = "Player {:.0f} wins!".format(self.__turn)
            messagebox.showinfo("We have a winner!",string)
            self.__wins[self.__turn-1] += 1
            self.__totalwins[self.__turn-1].configure\
                (text=self.__wins[self.__turn-1])
            self.new_game()

        if win == False and draw == False:
            return False


def main():

    """ Ohjelman pääfunktio, joka suorittaa ohjelman kokonaisuudessaan."""

    ui = TicTacToe()
    ui.start()

main()
