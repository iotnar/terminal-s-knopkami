import pygame as pg
import sys
import pyttsx3
import pygame_widgets
tts = pyttsx3.init()
from pygame_widgets.button import Button


pg.mixer.pre_init
pg.init()
pg.mixer.music.load('elektro.wav')
pg.mixer.music.play()

zagruzka = pg.mixer.Sound('vkluchenie.wav')
#priv1 = pg.mixer.Sound('voxworker-voice-file.mp3')
priv2 = pg.mixer.Sound('fraza2.mp3')
priv3 = pg.mixer.Sound('fraza3.mp3')
klik = pg.mixer.Sound('klik.wav')

def count_lines(filename, chunk_size=1<<13):
    with open(filename) as file:
        return sum(chunk.count('\n')
                   for chunk in iter(lambda: file.read(chunk_size), ''))
j = count_lines('text2.txt')+1
text = ['']*j
i = 0
with open('text2.txt') as f :
    text = f.readlines()
    print(text)

tts.setProperty('voice', 'ru')
tts.setProperty('rate', 130)




#priv1 = pg.mixer.Sound('test.mp3')

pg.init()

screen_width = 840
screen_height = 566
screen = pg.display.set_mode([screen_width, screen_height])
zastavka = pg.image.load('zastavka2.jpg').convert()
screen.blit(zastavka, (0, 0))
pg.font.Font('ConsolaMono.ttf', 20)
button_image = pg.image.load('essentials-14.png')
button = Button(
    # Mandatory Parameters
    screen,  # Surface to place button on
    100,  # X-coordinate of top left corner
    460,  # Y-coordinate of top left corner
    80,  # Width
    80,  # Height

    # Optional Parameters
    image=button_image,
    text='',  # Text to display
    fontSize=25,  # Size of font
    margin=1,  # Minimum distance between text/image and edge of button
    inactiveColour=(77, 157, 75),  # Colour of button when not being interacted with
    hoverColour=(77, 187, 75),  # Colour of button when being hovered over
    pressedColour=(50, 157, 60),  # Colour of button when being clicked
    radius=5,  # Radius of border corners (leave empty for not curved)
    onClick=lambda: print('Click')  # Function to call when clicked on
)

pg.display.update()
clock = pg.time.Clock()
FPS = 120
#pg.time.wait(1000)
pg.font.init()
pg.font.get_fonts()

i = 0
x = 0
k = 0

def nadpis_text(x, y, i,  messeg):
    i = 0
    while i < int(len(messeg)):
        text1 = f.render(str(messeg1), False, (77, 157, 75))
        screen.blit(text1, (10, y))
        pg.display.update()
        klik.play(0, 0, 0).set_volume(0.05)
        #play_text_line(messeg[i])
        text = f.render(str(messeg[i]), True, (77, 157, 75))
        screen.blit(text, (150 + x, y))
        pg.display.update()
        pg.time.wait(60)
        i += 1
        x += 13


def play_text_line(messeg):
    tts.say(messeg)
    tts.runAndWait()

zagruzka.play(-1)

while True:
    for q in pg.event.get():
        if q.type == pg.QUIT:
            sys.exit()
    messeg1 = "18F000__//:"
    messeg = text[0]
    f = pg.font.Font('ConsolaMono.ttf', 18)
    while k < j :

        print(i , x )
        messeg = text[k]
        nadpis_text(x, 10+k*40, k, messeg)
        play_text_line(messeg)
        pg.time.wait(300)
        k += 1
    pygame_widgets.update(klik)
    pg.display.update()