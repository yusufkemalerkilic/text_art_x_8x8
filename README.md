# EN:
<pre>
X      X                XX         XX                     XX
X      X                 X          X                     XX
X      X                 X          X                     XX
XXXXXXXX     XXXX        X          X         XXX         XX
X      X    X    X       X          X        X   X        XX
X      X    XXXXXX       X          X        X   X
X      X    X            X          X        X   X        XX
X      X     XXXX       XXX        XXX        XXX         XX
</pre>
Name: text_art_x_8x8.py

Version: v1.0

Author: Yusuf Kemal Erkılıç

Date: 02.11.2024 (dd/mm/yyyy)

Purpose:
This Python script prints the letters of the English and Turkish alphabets, as well as common punctuation marks, symbols, and mathematical operators in an 8x8 pixel format using the 'X' character.

Description:
The characters to be printed on the screen in 8x8 pixel format can be interpreted as a picture. Each character is 2-dimensional. Therefore a 2-dimensional matrix is created for each supported character.
This matrix consists of 8 lists of 8 elements each. Each list is an 8-bit data set that can take the value 0 or 1. Since the matrix consists of 8 lists, we have a 64-bit data set for each character.
The lists specify the rows in order from top to bottom. The first list is the top row and the last list is the bottom row.
Each element in the lists specifies a column in order. The first element of each list specifies the first column from the left and the last element specifies the first column from the right.
The elements of each list take the value 1 or 0 depending on whether the character's image intersects in that column of that row. 1 if it does, 0 if it does not.
According to this logic, all characters to be supported are encoded in a 2D matrix.
In order to ensure that the characters are next to each other, the first lists of the matrix in which each character of the text entered from the user is encoded are process in order
and if the element is 1, the character X is printed on the screen and if it is 0, the space is printed on the screen.
After processing each list, two spaces are left to create a space between characters. No line is skipped during this time.
After outputting the screen according to the first list of the matrix for each character of the text entered by the user, skip the line and continue with the second lists of the same matrices.
In this way, all lists are finished in order.

**Attention!**  
If you feel that you are not getting the desired result after entering the word, try making the window full screen.
If that doesn't work, enter a shorter text. This problem is often caused by entering words that are too long to fit on your screen.


# TR:
<pre>
X      X                         X                     X                        XX
XX    XX                         X                     X                        XX
X X  X X                         X                     X                        XX
X  XX  X     XXXX                X XXXX       XXXX     X XXXX       XXXX        XX
X      X    X    X       X       XX    X          X    XX    X          X       XX
X      X    XXXXXX      X X      X      X     XXXXX    X      X     XXXXX
X      X    X           X        X      X    X    X    X      X    X    X       XX
X      X     XXXX       X        X      X     XXXXX     XXXXXX      XXXXX       XX
</pre>
İsim: text_art_x_8x8.py

Sürüm: v1.0

Yazar: Yusuf Kemal Erkılıç

Tarih: 02.11.2024 (gg/aa/yyyy)

Amaç:
Bu Python scripti, İngilizce ve Türkçe alfabedeki karakterleri, yaygın noktalama işaretlerini,
sembolleri ve matematiksel operatörleri 8x8 piksel formatında 'X' karakteri kullanarak yazdırmaktadır.

Açıklama:
Ekrana 8x8 pixel formatında yazdırılacak karakterler bir resim gibi yorumlanabilir. Her bir karakter 2 boyutludur.
Bu sebepten desteklenen her karakter başına 2 boyutlu bir matris oluşturulur. Bu matris her biri 8 elemandan oluşan 8 listeden ibarettir. Her bir liste 0 ya da 1 değerini alabilen 8 bitlik bir veri kümesidir.
Matris 8 adet listeden oluştuğundan dolayı her bir karakter için elimizde 64 bitlik bir veri seti bulunur. Listeler sırasına göre yukarıdan aşağıya doğru satırları belirtir.
İlk liste en üstteki satırı ve son liste en alttaki satırı belirtir. Listelerdeki her bir eleman ise sırasına göre bir sütunu belirtir.
Her bir listenin ilk elemanı soldan ilk sütunu, son elemanı ise sağdan ilk sütunu belirtir.
Her bir listenin elemanları o satırın o sütununda karakterin resminin kesişip kesişmediğine göre 1 ya da 0 değerini alır. Kesişiyorsa 1, kesişmiyorsa 0.
Bu mantığa göre desteklenecek bütün karakterler 2 boyutlu matris biçiminde kodlanır.
Karakterlerin yan yana durmasını sağlamak için ise kullanıcıdan girilen metnin her bir karakterinin kodlandığı matrisin ilk listeleri sırasıyla işlenir ve eğer eleman 1 ise X karakteri, 0 ise boşluk ekrana yazdırılır.
Karakterler arasında boşluk oluşturmak için, her bir listenin işlenmesi sonrasında  iki adet boşluk bırakılır. Bu süre zarfında satır atlanmaz.
Kullanıcı tarafından girilen metnin her bir karakterine ait matrisin ilk listesine göre ekran çıktısı alındıktan sonra satır atlanırve aynı matrislerin ikinci listelerinden devam edilir.
Bu şekilde bütün listeler sırasıyla bitirilir.

**Dikkat!**  
Kelimeyi girdikten sonra istediğiniz sonucu alamadığınızı düşünüyorsanız, pencereyi tam ekran yapmayı deneyin.
Bu işe yaramazsa, daha kısa bir metin girin. Bu sorun genellikle ekranınıza sığmayacak kadar uzun kelimelerin girilmesinden kaynaklanır.
