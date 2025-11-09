# yoskOS

yoskOS, basit ve eğitici bir işletim sistemi uygulaması sağlamayı amaçlayan özel bir işletim sistemi projesidir.
## 2. Sürümde eklenenler
- Bitmap ile görsel yazdırma
- Renkli text `print_color("text",0X01);`
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
```bash
make
```

## Çalıştırma

Derleme tamamlandıktan sonra, yoskOS'u QEMU kullanarak çalıştırabilirsiniz:
```bash
qemu-system-i386 -cdrom yoskOS.iso
```

## Görüntüler
<img width="711" height="396" alt="image" src="https://github.com/user-attachments/assets/e6a8a2c4-0c0c-4880-8830-25dc1d8058b3" />
<img width="715" height="446" alt="image" src="https://github.com/user-attachments/assets/c75f6d90-65a4-4817-b6ef-3a876e37ea3d" />
