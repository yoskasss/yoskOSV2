# yoskOS

yoskOS, basit ve eğitici bir işletim sistemi uygulaması sağlamayı amaçlayan özel bir işletim sistemi projesidir.

## Proje Yapısı

- `apps/` - Kullanıcı uygulamaları
- `build/` - Derleme çıktı dizini
- `grub/` - GRUB önyükleyici yapılandırması
- `include/` - Başlık dosyaları
- `iso/` - ISO görüntüsü ile ilgili dosyalar
- `kernel/` - Çekirdek kaynak kodu
- `libs/` - Kütüphane dosyaları

## Derleme

yoskOS'u derlemek için ihtiyacınız olanlar:
- NASM (Netwide Assembler)
- GCC çapraz derleyici
- Make
- GRUB

Derlemek için aşağıdaki komutu çalıştırın:
yoskOS — Minimal i686 toy OS (MikuOS)
=====================================

Bu depo, basit bir i686 freestanding toy kernel ve kabuk uygulaması içerir. Amaç: küçük ve öğretici bir demo — terminal, basit dosya sistemi, notepad/uptime uygulamaları ve boot sırasında gömülü bir bitmap gösterme özelliği.

Önemli dosyalar
- `kernel/kernel.c` — kernel ve kabuk (terminal) kodu, grafik/text render fonksiyonları.
- `kernel/kernel_entry.asm` — multiboot header ve kernel giriş noktası.
- `kernel/my_bitmap.h` — gömülü bitmap verisi (örnek görsel).
- `grub/grub.cfg` — GRUB menü/ayarları (gfxmode, gfxpayload içerir).
- `Makefile` — derleme ve ISO üretim kuralları.
- `yoskOS.iso` — oluşturulmuş ISO (derleme sonrası).
- `kernel/*.orig` ve `kernel/*.bak` — otomatik oluşturulmuş yedekler (uygulama sırasında oluşturulduysa).
- `LICENSE`, `README.md` — lisans ve kullanım bilgileri.

Gereksinimler (Linux)
- i686-elf-gcc toolchain (cross-compiler).
- i686-elf-binutils (ld, objcopy vb.).
- grub-mkrescue / grub-pc-bin ve xorriso (ISO ve GRUB üretmek için).
- qemu-system-i386 (test etmek için).

Örnek Ubuntu/Debian kurulumu (örn):
```bash
sudo apt update
sudo apt install build-essential bison flex xorriso qemu-system-i386 grub-pc-bin grub-common mtools
# Cross-toolchain: dağıtıma bağlı olarak farklı paket isimleri olabilir; kendi i686-elf toolchain'inizi kullanabilirsiniz.
```

Derleme
Proje kökünde (ör. `/home/enes/Masaüstü/MikuOS`) çalıştır:
```bash
make
```
Bu `build/` dizinini oluşturur, `build/kernel.bin` linklenir ve `yoskOS.iso` üretilir.

QEMU ile çalıştırma (hızlı test):
```bash
qemu-system-i386 -cdrom yoskOS.iso -m 512
```
Bu komut QEMU penceresi açar; GRUB menüsünden `yoskOS` seçilip kernel boot edilir.

Görsel (bitmap) gösterimi
- Kernel kabuğunda `show_image` komutunu yazıp Enter'a bastığınızda gömülü bitmap (`kernel/my_bitmap.h`) Mode13 (320x200) üzerine çizilmeye çalışılır.
- GRUB yapılandırmasında `set gfxmode=320x200` ve `set gfxpayload=keep` ayarları mevcuttur; bu, QEMU/GRUB kombinasyonunda Mode13 tipi bir framebuffer sağlamaya yardımcı olur.
- Eğer GRUB multiboot framebuffer (linear framebuffer) sağlarsa, kernel bunu kullanmak üzere bazı sürümlerde destek eklenmiştir. Ancak bu repo hâliyle `show_image` Mode13 alanına (0xA0000) çizmeye öncelik verir — demo görüntüsünün görünmesi için uyumludur.

Yedekler ve geri alma
- Bu oturumda bazı dosyalar otomatik olarak yedeklendi: `kernel/kernel.c.orig`, `kernel/kernel_entry.asm.orig`, `grub/grub.cfg.orig` (ve `.bak` dosyaları). Bu dosyalar mevcut dosyaların tam kopyalarını içerir.
- Bir dosyayı orijinal yedeğe geri döndürmek için (örnek):
```bash
cp kernel/kernel.c.orig kernel/kernel.c
cp kernel/kernel_entry.asm.orig kernel/kernel_entry.asm
cp grub/grub.cfg.orig grub/grub.cfg
make clean
make
```
Not: Geri alma işleminden sonra tekrar `make` çalıştırın.

Neler dikkat edilmeli
- Kernel, GRUB tarafından korunmuş modda çalışır — BIOS kesmeleri (int $0x10 vb.) çağrıları korunmuş modda kullanılamaz; bu nedenle kodda bu tür çağrılar kaldırıldı/boş bırakıldı.
- Eğer QEMU/GRUB farklı bir framebuffer (ör. 80x25 16bpp text-like framebuffer) sağlarsa görüntü görünmeyebilir; böyle durumlarda multiboot framebuffer desteği veya Mode13 talebi (veya uygun GRUB gfxmode) ile denemeler yapılmalıdır.

Geliştirme ipuçları
- Değişiklik yapmadan önce `*.orig` veya `*.bak` yedeklerini kopyalayın.
- Bir sürüm kontrolü (git) kullanılması şiddetle tavsiye olunur; bu repo yerel dosya değişiklikleri için commit geçmişi sağlar ve geri almak daha kolay olur.

Katkı/İletişim
- Bu küçük proje öğretici amaçlıdır. Değişiklik yapmak ve denemek serbesttir. Eğer bir sorun çıkarsa bana adımları ve hata çıktısını verin, yardımcı olurum.

Lisans
- Projede `LICENSE` dosyası mevcuttur; lütfen oradaki lisans koşullarını inceleyin.

Kısa Özet
- `make` → `yoskOS.iso` oluşturur.
- `qemu-system-i386 -cdrom yoskOS.iso` ile test edilir.
- `show_image` komutu demo görselini ekrana çizer (Mode13 öncelikli).

İyi çalışmalar!
