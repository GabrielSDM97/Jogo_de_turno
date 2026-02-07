def som(mp3):
    """
    Player de música!

    Utilize dessa forma: som("arquivo.mp3")
    """
    import pygame
    from time import sleep
    pygame.mixer.init()
    pygame.mixer.music.load(mp3)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        sleep(0.1)
