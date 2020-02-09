from PIL import Image, ImageDraw, ImageFont
import time


dr='drake'
yo='yoda'
pi='pika'

print('Choose meme (drake, pika, yoda)')                 #wybór szablonu
x=input()


print('give your text now')             #tekst mema
y=input()

if x == dr:
    print ('next')
    z=input()

if x == dr:                                                     #DRAKE
 img = Image.open('images\drake.jpg')                #plik
 draw = ImageDraw.Draw(img)
 font = ImageFont.truetype("arial.ttf", 12, )       #czcionka,rozmiar
 draw.text((500, 500), z ,(0,0,0),font=font, algin="center")
 draw.text((500, 50), y ,(0,0,0),font=font, algin="center")# koordy, text ,kolor,czcionka
 img.save('goodmemes\meme.jpg')                        # zapis ,nazwa
 img = Image.open('goodmemes\meme.jpg').show()
 print('素晴らしいミーム')

if x == yo:                                                      #YODA
 img = Image.open('images\yoda.jpg')                #plik
 draw = ImageDraw.Draw(img)
 font = ImageFont.truetype("arial.ttf", 12, )       #czcionka,rozmiar
 draw.text((380, 370), y  ,(0,0,0),font=font, algin="center")   # koordy, text ,kolor,czcionka
 img.save('goodmemes\meme.jpg')                        # zapis ,nazwa
 img = Image.open('goodmemes\meme.jpg').show()
 print('your meme')

 if x == pi:                                                          #PIKA
     img = Image.open('images\pika.png')  # plik
     draw = ImageDraw.Draw(img)
     font = ImageFont.truetype("arial.ttf", 12, )  # czcionka,rozmiar
     draw.text((380, 370), y , (0, 0, 0), font=font,
               algin="center")  # koordy, text ,kolor,czcionka
     img.save('goodmemes\meme.jpg')  # zapis ,nazwa
     img = Image.open('goodmemes\meme.jpg').show()
     print('hehe, funny :3')
time.sleep(2)
print('thanks for using!!!')
time.sleep(2)