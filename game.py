from pygame import*

winw = 900
winh = 550
window = display.set_mode((winw,winh))


background = transform.scale(image.load('пинг понг (1).jpg'),(winw,winh))


FPS = time.Clock()



run = True
while  run:
    for i in event.get():
        if i.type == QUIT:
            run = False

    window.blit(background,(0,0))


    display.update()
    FPS.tick(60)
    