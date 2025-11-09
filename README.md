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

## Projeye Yeni Resimler Ekleme
yoskOS, .h başlık dosyaları olarak formatlanmış piksel sanat görsellerini görüntüleyebilir. Bu süreci kolaylaştırmak için projede tkinter kütüphanesini kullanan bir Python piksel sanat editörü bulunmaktadır.


### 1. Python Piksel Sanat Editörünü Çalıştırma

Editörü çalıştırmak için Python 3 ve tkinter kütüphanesinin (genellikle Python ile birlikte gelir) kurulu olması gerekir.
```bash
 python image_editor.py
```
### 2. Resim Oluşturma ve Kaydetme
Açılan pencerede 64x64 boyutundaki tuval üzerinde çizim yapın.


"Renk Seç" butonu ile paletten renk seçin.


Çiziminiz bittiğinde "Farklı Kaydet (.h)" butonuna tıklayın.


**ÇOK ÖNEMLİ:** Dosyayı projenin include/ dizinine, sıralı bir numara ile kaydedin. Örneğin, projenizde 1.h ve 2.h zaten varsa, yeni dosyanızı 3.h olarak kaydedin.


Editör, dosyayı kaydederken dosya adını kullanarak C tarafında benzersiz değişken adları (image_3_data, BITMAP_WIDTH_3 vb.) oluşturacaktır.


### 3. Resmi İşletim Sistemine Entegre Etme

Yeni bir .h dosyası oluşturduktan sonra, onu işletim sistemine tanıtmak için iki küçük değişiklik yapmanız gerekir:


**a)** kernel/images.c Dosyasını Güncelleyin:

Yeni başlık dosyanızı #include listesine ve available_images dizisine ekleyin.
```bash
// kernel/images.c

#include "images.h"
#include "1.h"
#include "2.h"
#include "3.h" // <-- YENİ SATIR

const Image available_images[] = {
    { image_1_data, BITMAP_WIDTH_1, BITMAP_HEIGHT_1 },
    { image_2_data, BITMAP_WIDTH_2, BITMAP_HEIGHT_2 },
    { image_3_data, BITMAP_WIDTH_3, BITMAP_HEIGHT_3 }, // <-- YENİ SATIR
};

// ...
```
### 4. Yeniden Derleme
Tüm bu adımlardan sonra projeyi yeniden derleyin:


Artık işletim sistemini çalıştırıp show komutunu yazdığınızda, yeni eklediğiniz resim de seçenekler arasında görünecektir.
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

<img width="719" height="401" alt="image" src="https://github.com/user-attachments/assets/93fd8ec5-03ae-4c5b-b02f-adaae6397bbb" />
<img width="713" height="472" alt="image" src="https://github.com/user-attachments/assets/99f3b8a0-8e09-4ae3-b335-2b6ac1bff7c3" />
