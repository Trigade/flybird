import pygame
import sys
from numpy import random
from modules.modules import Bird,Pipes,TopPipes,Point
from pygame import mixer

pygame.init()

def background_animations():
    pass

def add_pipe(x_konumu,points,pipes,hepsi):
    yeni_engel = Pipes(x_konumu)
    alfa = yeni_engel.rect.top - 200 
    beta = yeni_engel.rect.top - 75
    top_engel = TopPipes(x_konumu, alfa)
    score_trigger = Point(x_konumu, beta)
    points.add(score_trigger)
    pipes.add(yeni_engel)
    pipes.add(top_engel)
    hepsi.add(yeni_engel)
    hepsi.add(top_engel)
    hepsi.add(score_trigger)

def main():
    pygame.mixer.init()
    altin_sesi = pygame.mixer.Sound(r"audio\coin.wav")
    altin_sesi.set_volume(0.5)
    carpma_sesi = pygame.mixer.Sound(r"audio\hit.wav")
    carpma_sesi.set_volume(0.5)
    pygame.mixer.music.load(r"audio\bg.mp3")
    pygame.mixer.music.play(-1)
    GENISLIK = 600
    YUKSEKLIK = 600
    skor = 0
    ARALIK = 300
    ekran  = pygame.display.set_mode((GENISLIK,YUKSEKLIK))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Flappy")
    font = pygame.font.SysFont(" Arial ", 18)

    calistir = True
    oyun_bitti = False
    hepsi = pygame.sprite.Group()
    pipes = pygame.sprite.Group()
    top_pipes = pygame.sprite.Group()
    points = pygame.sprite.Group()

    bird = Bird(200)
    hepsi.add(bird)
    for i in range(3):
        add_pipe(GENISLIK + 200 + (i * ARALIK), points, pipes, hepsi)



    while calistir:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                calistir = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    calistir = False
                if event.key == pygame.K_UP:
                    bird.zipla()

        son_boru = max([p.rect.right for p in pipes] + [0])
        if son_boru < GENISLIK:
            add_pipe(GENISLIK + ARALIK, points, pipes, hepsi)

        if bird.rect.bottom >= YUKSEKLIK or bird.rect.top <= 0:
            carpma_sesi.play()
            calistir = False
            oyun_bitti = True

        if pygame.sprite.spritecollide(bird, pipes, False):
            carpma_sesi.play()
            calistir = False
            oyun_bitti = True
        if pygame.sprite.spritecollide(bird, points, True):
            skor += 10
            altin_sesi.play()

        hepsi.update()
        ekran.fill((135,209,245))
        hepsi.draw(ekran)
        yazi_yuzeyi = font.render(f"Skor:{skor}", True, (255, 255, 255))
        ekran.blit(yazi_yuzeyi, (20, 20))
        pygame.display.flip()
        clock.tick(60)

    while oyun_bitti:
        pygame.mixer.music.stop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                oyun_bitti = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    oyun_bitti = False
                if event.key == pygame.K_r:
                    main()

        ekran.fill((0, 0, 0))

        oyun_bitti_yazi = font.render("OYUN BİTTİ!", True, (255, 0, 0))
        yazi_rect = oyun_bitti_yazi.get_rect(center=(GENISLIK / 2, YUKSEKLIK / 2 - 50))
        ekran.blit(oyun_bitti_yazi, yazi_rect)

        skor_yazi = font.render(f"Final Skorunuz: {skor}", True, (255, 255, 255))
        skor_rect = skor_yazi.get_rect(center=(GENISLIK / 2, YUKSEKLIK / 2 + 20))
        ekran.blit(skor_yazi, skor_rect)

        restart_btn = font.render("Oyunu tekrar başlatmak için 'R' tuşuna basınız",True,(255,255,255))
        restart_btn_rect = skor_yazi.get_rect(center=(GENISLIK // 2 - 80 , YUKSEKLIK / 2 + 40))
        ekran.blit(restart_btn, restart_btn_rect)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()

pygame.quit()
sys.exit()