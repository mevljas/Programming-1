import random
import math
import time

import risar
from PyQt5.QtWidgets import QMessageBox

hitrost = 5


class Zoga:
    def __init__(self, barva):
        self.moving = True
        self.r = 10
        self.x = random.randint(2 * self.r, risar.maxX - 2 * self.r)
        self.y = random.randint(2 * self.r, risar.maxY - 2 * self.r)
        if not barva:
            self.barva = risar.nakljucna_barva()
        else:
            self.barva = risar.bela
        self.krog = risar.krog(self.x, self.y, self.r, self.barva)
        self.vx = random.uniform(-5, 5)
        self.vy = math.sqrt(hitrost ** 2 - self.vx ** 2)
        self.explosion = False
        self.already_exploded = False

    def move(self, vx, vy):
        if not vx and not vy:
            self.x += self.vx
            self.y += self.vy
        else:
            self.x = vx + self.r / 2
            self.y = vy + self.r / 2
        self.krog.setPos(self.x, self.y)
        self.collision_wall()

    def collision_wall(self):
        if self.x + self.r >= risar.maxX or self.x - self.r <= 0:
            self.vx *= (-1)
        if self.y + self.r >= risar.maxY or self.y - self.r <= 0:
            self.vy *= (-1)

    def collision_ball(self, other):
        # return (self.x - other.x) ** 2 + (self.y - other.y) ** 2 <= (self.r + other.r) ** 2
        x = self.x
        x2 = other.x
        y = self.y
        y2 = other.y
        r = self.r
        r2 = other.r
        if (x + 2 * r >= x2 - r2 and x <= x2 + r2) or (x - 2 * r <= x2 + r2 and x >= x2 - r):
            if (y + 2 * r >= y2 - r2 and y <= y2 + r2) or (y - 2 * r <= y2 + r2 and y + r >= y2):
                return True
        return False

    def explode(self):
        self.moving = False
        self.explosion = True
        self.krog.setRect(-30, -30, 60, 60)
        c = self.krog.pen().color().lighter()
        c.setAlpha(192)
        self.krog.setBrush(c)
        self.start_time = time.time()
        global stevilo_eksplodiranih_zog
        global stevilo_vseh_eksplodiranih_zog
        stevilo_eksplodiranih_zog += 1
        stevilo_vseh_eksplodiranih_zog += 1

    def explosion_timer(self):
        if time.time() - self.start_time > 4:
            self.krog.hide()
            self.explosion = False
            global stevilo_eksplodiranih_zog
            stevilo_eksplodiranih_zog -= 1
            self.already_exploded = True
            eksplodirane_zoge.pop(0)


stevilo_eksplodiranih_zog = 0
stevilo_vseh_eksplodiranih_zog = 0
eksplodirane_zoge = []


class Stopnja:
    def __init__(self, stevilo_zog):
        self.zoge = [Zoga(None) for i in range(stevilo_zog)]
        self.zoga_miske = Zoga(risar.bela)
        self.zoga_miske.moving = False
        self.zoga_miske.krog.setRect(-30, -30, 60, 60)
        self.klik = False
        self.nedotaknjena = True
        risar.klik = False
        global stevilo_eksplodiranih_zog
        global stevilo_vseh_eksplodiranih_zog
        stevilo_eksplodiranih_zog = 0
        stevilo_vseh_eksplodiranih_zog = 0
        eksplodirane_zoge.clear()

    def run(self):
        while self.nedotaknjena or stevilo_eksplodiranih_zog > 0:
            self.x, self.y = risar.miska
            if risar.klik and not self.klik:
                self.klik = True
                risar.klik = False
                self.klik_time = time.time()
            elif self.klik:
                if time.time() - self.klik_time > 4:
                    self.nedotaknjena = False
                    self.zoga_miske.krog.hide()
                    self.zoga_miske.already_exploded = True
            else:
                self.zoga_miske.move(self.x, self.y)
            for self.zoga in self.zoge:
                if self.zoga.moving:
                    self.zoga.move(None, None)
                else:
                    if self.zoga.explosion:
                        self.zoga.explosion_timer()
                if self.klik and not self.zoga.explosion and not self.zoga.already_exploded \
                        and not self.zoga_miske.already_exploded and self.zoga.collision_ball(self.zoga_miske):
                    self.zoga.explode()
                    self.nedotaknjena = False
                    eksplodirane_zoge.append(self.zoga)
                if not self.zoga.explosion and not self.zoga.already_exploded:
                    for eksplodirana_zoga in eksplodirane_zoge:
                        if self.zoga.collision_ball(eksplodirana_zoga):
                            self.zoga.explode()
                            eksplodirane_zoge.append(self.zoga)
                            break
            risar.cakaj(0.02)
        risar.pobrisi()


stevilka_stopnje = 1
stevilo_zog = 5
min_stevilo_eksplodiranih_zog = 1
while stevilka_stopnje <= 10:
    QMessageBox.information(None, f"Stopnja {stevilka_stopnje}",
                            f'Razstreli  {min_stevilo_eksplodiranih_zog} od {stevilo_zog} žog.')
    trenutna_stopnja = Stopnja(stevilo_zog)
    trenutna_stopnja.run()
    if stevilo_vseh_eksplodiranih_zog >= min_stevilo_eksplodiranih_zog:
        QMessageBox.information(None, f"Stopnja {stevilka_stopnje} uspešna",
                                f'Uspelo ti je razstreliti {stevilo_vseh_eksplodiranih_zog} od {stevilo_zog} žog.')
        stevilka_stopnje += 1
        min_stevilo_eksplodiranih_zog += int(stevilka_stopnje / 2)
        stevilo_zog += 2
        if stevilka_stopnje == 8:
            stevilo_zog += 4
    else:
        QMessageBox.information(None, f"Stopnja {stevilka_stopnje} neuspešna",
                                f'Uspelo ti je razstreliti le {stevilo_vseh_eksplodiranih_zog} od {stevilo_zog} žog.\nPremalo!')
