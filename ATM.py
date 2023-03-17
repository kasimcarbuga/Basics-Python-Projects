import "dart:io"; //Kullanıcıdan veri almamızı sağlayacak kütüphane!

void main(List<String> args) {
  int bakiye = 1000;

  print("----------------------------------------");
  print("mr.code_engineer ATM'ye Hoşgeldiniz...");
  print("----------------------------------------");

  while (true) {
    print("Bakiyeninizi görüntülemek için 1'e basınız...");
    print("Para yatırmak için 2'ye basınız...");
    print("Para çekmek için 3'e basınız...");
    print("Çıkış yapmak için 4'e basınız...");

    print("Yapmak istediğiniz işlemi seçiniz: ");
    String secim = stdin.readLineSync()!;
    //Kullanıcıdan veri aldığımız yer.

    if (secim == "1") {
      print("Bakiyeniz: $bakiye");
    } else if (secim == "2") {
      print("Yatırmak istediğiniz tutarı giriniz: ");
      int yatirim = int.parse(stdin.readLineSync()!);
      //Kullanıcıdan veri alıp int'e dönüştürüyoruz.
      bakiye = bakiye + yatirim;
      print("Yeni bakiyeniz: $bakiye");
    } else if (secim == "3") {
      print("Çekmek istediğiniz miktarı giriniz: ");
      int cekim = int.parse(stdin.readLineSync()!);
      //Kullanıcıdan veri alıp int'e dönüştürüyoruz.
      bakiye = bakiye - cekim;
      print("Yeni bakiyeniz: $bakiye");
    } else if (secim == "4") {
      print("Çıkış Yapılıyor...");
      break;
    } else {
      print("Geçersiz İşlem!");
    }
    print("---------------------------------");
  }
}
