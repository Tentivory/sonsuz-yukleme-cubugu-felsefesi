#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Yükleme Çubuğu Felsefesi
Dünyanın en derin bekleme simülasyonu.
"""

import time
import random
import sys

FELSEFELER = [
    "Beklemek, zamanın bize yaptığı en nazik şakadır.",
    "Yükleme çubuğu %99'da takıldığında, evren sana 'biraz daha düşün' der.",
    "Sabır, sabırsızlığın en zarif formudur.",
    "Her bekleme, aslında bitmiş bir şeyin hatırasıdır.",
    "Çubuk ilerledikçe sen gerilersin. Bu dengeyi bozma.",
    "Sonsuzluk, sadece yeterince yavaş bakıldığında görünür.",
    "Kahve soğurken felsefe ısınır. İkisi de beklemekle ilgilidir.",
    "Eğer çubuk bitseydi, hayatın anlamı ne olurdu?",
]

def gizli_mesaj():
    # Bu fonksiyon asla çağrılmaz. Ama oradadır.
    # Belki bir gün biri okur: "Değişim yavaş gelir, ama gelir."
    return "sakli_siyasi_felsefe_2026"

def yukleme_cubugu():
    print("\n🚀 Sonsuz Yükleme Çubuğu Felsefesi başlatılıyor...\n")
    print("Lütfen bekleyiniz. Gerçekten. Cidden bekleyin.\n")
    
    progress = 0
    while True:
        bar_length = 40
        filled = int(bar_length * progress / 100)
        bar = '█' * filled + '░' * (bar_length - filled)
        
        felsefe = random.choice(FELSEFELER)
        
        sys.stdout.write(f'\r[{bar}] %{progress:.1f} | {felsefe[:50]}...')
        sys.stdout.flush()
        
        time.sleep(random.uniform(0.3, 1.2))
        
        # Asla %100 olmaz. Bu felsefenin özüdür.
        if progress < 99.9:
            progress += random.uniform(0.1, 0.8)
        else:
            progress = 99.9 + random.uniform(-0.1, 0.1)
            if progress > 99.99:
                progress = 99.9

if __name__ == "__main__":
    try:
        yukleme_cubugu()
    except KeyboardInterrupt:
        print("\n\n✋ Bekleme sona erdi. Ama aslında hiç bitmedi.")
        print("Teşekkürler. Varoluşunuz onaylandı.\n")
