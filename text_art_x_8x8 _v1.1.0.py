# EN:

# Name: text_art_x_8x8_v1.1.py

# Version: v1.1

# Author: Yusuf Kemal Erkılıç

# Date: 02.11.2024 (dd/mm/yyyy)

# Purpose:
# This Python script prints the letters of the English and Turkish alphabets, as well as common punctuation,
# symbols, and mathematical operators, in an 8x8 pixel format using the character(s) entered by the user.

# Description:
# The characters to be printed on the screen in 8x8 pixel format can be interpreted as a picture.
# Each character is 2-dimensional.
# Therefore a 2-dimensional matrix is created for each supported character.
# This matrix consists of 8 lists of 8 elements each.
# Each list is an 8-bit data set that can take the value 0 or 1
# Since the matrix consists of 8 lists, we have a 64-bit data set for each character.
# The lists specify the rows in order from top to bottom.
# The first list is the top row and the last list is the bottom row.
# Each element in the lists specifies a column in order.
# The first element of each list specifies the first column from the left and the last element specifies the first column from the right.
# The elements of each list take the value 1 or 0 depending on whether the character's image intersects in that column of that row.
# 1 if it does, 0 if it does not.
# According to this logic, all characters to be supported are encoded in a 2D matrix.
# In order to ensure the juxtaposition of characters, the first lists of the matrix in which each character of the text entered from the user is
# encoded are processed sequentially, and if the element is 1, the pixel character(s) received from the user is printed on the screen,
# if the element is 0, the space character is printed on the screen as many times as the total length of the pixel character(s) received from the user.
# After processing each list, two spaces are left to create a space between characters.
# No line is skipped during this time.
# After outputting the screen according to the first list of the matrix for each character of the text entered by the user,
# skip the line and continue with the second lists of the same matrices.
# In this way, all lists are finished in order.



# TR:

# İsim: text_art_x_8x8_v1.1.py

# Sürüm: v1.1

# Yazar: Yusuf Kemal Erkılıç

# Tarih: 02.11.2024 (gg/aa/yyyy)

# Amaç:
# Bu Python scripti, İngilizce ve Türkçe alfabedeki karakterleri, yaygın noktalama işaretlerini,
# sembolleri ve matematiksel operatörleri 8x8 piksel formatında kullanıcının girdiği karakter(ler)i kullanarak yazdırmaktadır.

# Açıklama:
# Ekrana 8x8 pixel formatında yazdırılacak karakterler bir resim gibi yorumlanabilir.
# Her bir karakter 2 boyutludur.
# Bu sebepten desteklenen her karakter başına 2 boyutlu bir matris oluşturulur. 
# Bu matris her biri 8 elemandan oluşan 8 listeden ibarettir.
# Her bir liste 0 ya da 1 değerini alabilen 8 bitlik bir veri kümesidir.
# Matris 8 adet listeden oluştuğundan dolayı her bir karakter için elimizde 64 bitlik bir veri seti bulunur.
# Listeler sırasına göre yukarıdan aşağıya doğru satırları belirtir.
# İlk liste en üstteki satırı ve son liste en alttaki satırı belirtir.
# Listelerdeki her bir eleman ise sırasına göre bir sütunu belirtir.
# Her bir listenin ilk elemanı soldan ilk sütunu, son elemanı ise sağdan ilk sütunu belirtir.
# Her bir listenin elemanları o satırın o sütununda karakterin resminin kesişip kesişmediğine göre 1 ya da 0 değerini alır.
# Kesişiyorsa 1, kesişmiyorsa 0.
# Bu mantığa göre desteklenecek bütün karakterler 2 boyutlu matris biçiminde kodlanır.
# Karakterlerin yan yana durmasını sağlamak için ise kullanıcıdan girilen metnin her bir karakterinin kodlandığı matrisin ilk listeleri sırasıyla işlenir
# ve eğer eleman 1 ise kullanıcı tarafından girilen piksel karakter(ler)i, 0 ise piksel karakterinin uzunluğu kadar boşluk karakteri ekrana yazdırılır.
# Karakterler arasında boşluk oluşturmak için, her bir listenin işlenmesi sonrasında  iki adet boşluk bırakılır.
# Bu süre zarfında satır atlanmaz.
# Kullanıcı tarafından girilen metnin her bir karakterine ait matrisin ilk listesine göre ekran çıktısı alındıktan sonra satır atlanır
# ve aynı matrislerin ikinci listelerinden devam edilir.
# Bu şekilde bütün listeler sırasıyla bitirilir.



# EN: The 8x8 pixel format of each character is defined in a 2D matrix and assigned to the relevant variable.

# TR: Her karakterinin 8x8 pixel formatı 2 boyutlu matriste tanımlanıyor ve ilgili değişkene atanıyor.

space=[
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],  
[0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0]]

A=[
[0,0,0,1,1,0,0,0],
[0,0,1,0,0,1,0,0],
[0,1,0,0,0,0,1,0],
[1,0,0,0,0,0,0,1],
[1,1,1,1,1,1,1,1],
[1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,1]]

B=[
[1,1,1,1,1,1,0,0],
[1,0,0,0,0,0,1,0],
[1,0,0,0,0,0,1,0],
[1,1,1,1,1,1,1,0],
[1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,1],
[1,1,1,1,1,1,1,0]]

C=[
[0,0,1,1,1,1,1,0],
[0,1,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0],
[0,1,0,0,0,0,0,1],
[0,0,1,1,1,1,1,0]]

Ç=[
[0,0,1,1,1,1,1,0],
[0,1,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0],
[0,1,0,0,0,0,0,1],
[0,0,1,1,1,1,1,0],
[0,0,0,0,0,0,0,0],
[0,0,0,1,1,0,0,0]]

D=[
[1,1,1,1,1,1,0,0],
[1,0,0,0,0,0,1,0],
[1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,1,0],
[1,1,1,1,1,1,0,0]]

E=[
[1,1,1,1,1,1,1,1],
[1,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0],
[1,1,1,1,1,0,0,0],
[1,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0],
[1,1,1,1,1,1,1,1]]

F=[
[1,1,1,1,1,1,1,1],
[1,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0],
[1,1,1,1,1,0,0,0],
[1,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0]]

G=[
[0,0,1,1,1,1,1,0],
[0,1,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0],
[1,0,0,0,1,1,1,1],
[1,0,0,0,0,0,0,1],
[0,1,0,0,0,0,0,1],
[0,0,1,1,1,1,1,0]]

Ğ=[
[0,0,0,1,1,1,0,0],
[0,0,0,0,0,0,0,0],
[0,0,1,1,1,1,1,0],
[0,1,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0],
[1,0,0,0,1,1,1,1],
[0,1,0,0,0,0,0,1],
[0,0,1,1,1,1,1,0]]

H=[
[1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,1],
[1,1,1,1,1,1,1,1],
[1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,1]]

I=[
[0,0,1,1,1,1,0,0],
[0,0,0,1,1,0,0,0],
[0,0,0,1,1,0,0,0],
[0,0,0,1,1,0,0,0],
[0,0,0,1,1,0,0,0],
[0,0,0,1,1,0,0,0],
[0,0,0,1,1,0,0,0],
[0,0,1,1,1,1,0,0]]

İ=[
[0,0,0,1,1,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,1,1,1,1,0,0],
[0,0,0,1,1,0,0,0],
[0,0,0,1,1,0,0,0],
[0,0,0,1,1,0,0,0],
[0,0,0,1,1,0,0,0],
[0,0,1,1,1,1,0,0]]

J=[
[0,0,0,0,0,1,1,1],
[0,0,0,0,0,0,0,1],
[0,0,0,0,0,0,0,1],
[0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,1],
[0,1,0,0,0,0,1,0],
[0,0,1,1,1,1,0,0]]

K=[
[0,1,0,0,0,1,0,0],
[0,1,0,0,1,0,0,0],
[0,1,0,1,0,0,0,0],
[0,1,1,0,0,0,0,0],
[0,1,1,0,0,0,0,0],
[0,1,0,1,0,0,0,0],
[0,1,0,0,1,0,0,0],
[0,1,0,0,0,1,0,0]]

L=[
[1,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0],
[1,1,1,1,1,1,1,1]]

M=[
[1,0,0,0,0,0,0,1],
[1,1,0,0,0,0,1,1],
[1,0,1,0,0,1,0,1],
[1,0,0,1,1,0,0,1],
[1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,1]]

N=[
[1,0,0,0,0,0,0,1],
[1,1,0,0,0,0,0,1],
[1,0,1,0,0,0,0,1],
[1,0,0,1,0,0,0,1],
[1,0,0,0,1,0,0,1],
[1,0,0,0,0,1,0,1],
[1,0,0,0,0,0,1,1],
[1,0,0,0,0,0,0,1]]

O=[
[0,0,1,1,1,1,0,0],
[0,1,0,0,0,0,1,0],
[1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,1],
[0,1,0,0,0,0,1,0],
[0,0,1,1,1,1,0,0]]

Ö=[
[0,0,1,0,0,1,0,0],
[0,0,0,0,0,0,0,0],
[0,0,1,1,1,1,0,0],
[0,1,0,0,0,0,1,0],
[1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,1],
[0,1,0,0,0,0,1,0],
[0,0,1,1,1,1,0,0]]

P=[
[1,1,1,1,1,1,1,0],
[1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,1],
[1,1,1,1,1,1,1,0],
[1,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0]]

Q=[
[0,0,1,1,1,1,0,0],
[0,1,0,0,0,0,1,0],
[1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,1],
[1,0,0,0,0,1,0,1],
[0,1,0,0,0,0,1,0],
[0,0,1,1,1,1,0,1]]

R=[
[1,1,1,1,1,1,1,0],
[1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,1],
[1,1,1,1,1,1,1,0],
[1,0,0,0,0,1,0,0],
[1,0,0,0,0,0,1,0],
[1,0,0,0,0,0,0,1]]

S=[
[0,0,1,1,1,1,1,1],
[0,1,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0],
[0,1,1,1,1,1,0,0],
[0,0,0,0,0,0,1,0],
[0,0,0,0,0,0,0,1],
[0,0,0,0,0,0,1,0],
[1,1,1,1,1,1,0,0]]

Ş=[
[0,1,1,1,1,1,1,1],
[1,0,0,0,0,0,0,0],
[0,1,1,1,1,1,1,0],  
[0,0,0,0,0,0,0,1],
[0,0,0,0,0,0,0,1],
[1,1,1,1,1,1,1,0],
[0,0,0,0,0,0,0,0],
[0,0,0,1,1,0,0,0]]

T=[
[1,1,1,1,1,1,1,1],
[0,0,0,1,1,0,0,0],
[0,0,0,1,1,0,0,0],
[0,0,0,1,1,0,0,0],
[0,0,0,1,1,0,0,0],
[0,0,0,1,1,0,0,0],
[0,0,0,1,1,0,0,0],
[0,0,0,1,1,0,0,0]]

U=[
[1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,1],
[0,1,0,0,0,0,1,0],
[0,0,1,1,1,1,0,0]]

Ü=[
[1,0,0,0,0,0,0,1],
[0,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,1],
[0,1,0,0,0,0,1,0],
[0,0,1,1,1,1,0,0]]

V=[
[1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,1],
[0,1,0,0,0,0,1,0],
[0,0,1,0,0,1,0,0],
[0,0,0,1,1,0,0,0]]

W=[
[1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,1],
[1,0,0,1,1,0,0,1],
[1,0,1,0,0,1,0,1],
[0,1,0,0,0,0,1,0]]

X=[
[1,0,0,0,0,0,0,1],
[0,1,0,0,0,0,1,0],
[0,0,1,0,0,1,0,0],
[0,0,0,1,1,0,0,0],
[0,0,0,1,1,0,0,0],
[0,0,1,0,0,1,0,0],
[0,1,0,0,0,0,1,0],
[1,0,0,0,0,0,0,1]]

x=[
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,1,0,0,1,0,0],
[0,0,0,1,1,0,0,0],
[0,0,0,1,1,0,0,0],
[0,0,1,0,0,1,0,0]]

Y=[
[1,0,0,0,0,0,0,1],
[0,1,0,0,0,0,1,0],
[0,0,1,0,0,1,0,0],
[0,0,0,1,1,0,0,0],
[0,0,0,1,1,0,0,0],
[0,0,0,1,1,0,0,0],
[0,0,0,1,1,0,0,0],
[0,0,0,1,1,0,0,0]]

Z=[
[1,1,1,1,1,1,1,1],
[0,0,0,0,0,0,1,0],
[0,0,0,0,0,1,0,0],
[0,0,0,0,1,0,0,0],
[0,0,0,1,0,0,0,0],
[0,0,1,0,0,0,0,0],
[0,1,0,0,0,0,0,0],
[1,1,1,1,1,1,1,1]]

a=[
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,1,1,1,1,0,0],
[0,0,0,0,0,0,1,0],
[0,0,1,1,1,1,1,0],
[0,1,0,0,0,0,1,0],
[0,0,1,1,1,1,1,0]]

b=[
[1,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0],
[1,0,1,1,1,1,0,0],
[1,1,0,0,0,0,1,0],
[1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,1],
[0,1,1,1,1,1,1,0]]

c=[
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,1,1,1,1,0],
[0,0,1,0,0,0,0,1],
[0,1,0,0,0,0,0,0],
[0,0,1,0,0,0,0,1],
[0,0,0,1,1,1,1,0]]

ç=[
[0,0,0,0,0,0,0,0],
[0,0,0,1,1,1,1,0],
[0,0,1,0,0,0,0,1],
[0,1,0,0,0,0,0,0],
[0,0,1,0,0,0,0,1],
[0,0,0,1,1,1,1,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,1,1,0,0]]

d=[
[0,0,0,0,0,0,0,1],
[0,0,0,0,0,0,0,1],
[0,0,0,0,0,0,0,1],
[0,0,1,1,1,1,0,1],
[1,1,0,0,0,0,1,1],
[1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,1],
[0,1,1,1,1,1,1,0]]

e=[
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,1,1,1,1,0,0],
[0,1,0,0,0,0,1,0],
[0,1,1,1,1,1,1,0],
[0,1,0,0,0,0,0,0],
[0,0,1,1,1,1,0,0]]

f=[
[0,0,0,0,0,0,0,0],
[0,0,0,0,1,1,1,0],
[0,0,0,1,0,0,0,0],
[0,0,0,1,0,0,0,0],
[0,0,1,1,1,0,0,0],
[0,0,0,1,0,0,0,0],
[0,0,0,1,0,0,0,0],
[0,0,0,1,0,0,0,0]]

g=[
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,1,1,1,0,0,0],
[0,1,0,0,0,1,0,0],
[0,0,1,1,1,1,0,0],
[0,0,0,0,0,1,0,0],
[0,1,0,0,0,1,0,0],
[0,0,1,1,1,0,0,0]]

ğ=[
[0,0,1,1,1,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,1,1,1,0,0,0],
[0,1,0,0,0,1,0,0],
[0,0,1,1,1,1,0,0],
[0,0,0,0,0,1,0,0],
[0,1,0,0,0,1,0,0],
[0,0,1,1,1,0,0,0]]

h=[
[1,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0],
[1,0,1,1,1,1,0,0],
[1,1,0,0,0,0,1,0],
[1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,1]]

ı=[
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,1,1,0,0,0,0],
[0,0,0,1,0,0,0,0],
[0,0,0,1,0,0,0,0],
[0,0,0,1,0,0,0,0],
[0,0,1,1,1,0,0,0]]

i=[
[0,0,0,0,0,0,0,0],
[0,0,0,1,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,1,1,0,0,0,0],
[0,0,0,1,0,0,0,0],
[0,0,0,1,0,0,0,0],
[0,0,0,1,0,0,0,0],
[0,0,1,1,1,0,0,0]]

j=[
[0,0,0,0,0,0,0,0],
[0,0,0,0,1,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,1,1,0,0,0],
[0,0,0,0,1,0,0,0],
[0,0,0,0,1,0,0,0],
[0,0,1,0,1,0,0,0],
[0,0,0,1,0,0,0,0]]

k=[
[0,0,1,0,0,0,0,0],
[0,0,1,0,0,0,0,0],
[0,0,1,0,0,1,0,0],
[0,0,1,0,1,0,0,0],
[0,0,1,1,0,0,0,0],
[0,0,1,1,0,0,0,0],
[0,0,1,0,1,0,0,0],
[0,0,1,0,0,1,0,0]]

l=[
[0,0,1,1,0,0,0,0],
[0,0,0,1,0,0,0,0],
[0,0,0,1,0,0,0,0],
[0,0,0,1,0,0,0,0],
[0,0,0,1,0,0,0,0],
[0,0,0,1,0,0,0,0],
[0,0,0,1,0,0,0,0],
[0,0,1,1,1,0,0,0]]

m=[
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,1,1,0,1,0,0,0],
[0,1,0,1,0,1,0,0],
[0,1,0,1,0,1,0,0],
[0,1,0,1,0,1,0,0]]

n=[
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,1,1,1,0,0,0,0],
[0,1,0,0,1,0,0,0],
[0,1,0,0,1,0,0,0],
[0,1,0,0,1,0,0,0]]

o=[
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,1,1,1,0,0,0],
[0,1,0,0,0,1,0,0],
[0,1,0,0,0,1,0,0],
[0,1,0,0,0,1,0,0],
[0,0,1,1,1,0,0,0]]

ö=[
[0,0,0,0,0,0,0,0],
[0,0,1,0,1,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,1,1,1,0,0,0],
[0,1,0,0,0,1,0,0],
[0,1,0,0,0,1,0,0],
[0,1,0,0,0,1,0,0],
[0,0,1,1,1,0,0,0]]

p=[
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,1,1,0,0,0,0],
[0,0,1,0,1,0,0,0],
[0,0,1,1,0,0,0,0],
[0,0,1,0,0,0,0,0],
[0,0,1,0,0,0,0,0],
[0,0,1,0,0,0,0,0]]

q=[
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,1,1,0,0,0],
[0,0,1,0,1,0,0,0],
[0,0,0,1,1,0,0,0],
[0,0,0,0,1,0,0,0],
[0,0,0,0,1,0,0,0],
[0,0,0,0,1,0,0,0]]

r=[
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,1,0,0,0,0],
[0,0,1,0,1,0,0,0],
[0,0,1,0,0,0,0,0],
[0,0,1,0,0,0,0,0]]

s=[
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,1,1,1,0,0,0],
[0,1,0,0,0,0,0,0],
[0,0,1,1,1,0,0,0],
[0,0,0,0,0,1,0,0],
[0,0,1,1,1,0,0,0]]

ş=[
[0,0,0,0,0,0,0,0],
[0,0,1,1,1,0,0,0],
[0,1,0,0,0,0,0,0],
[0,0,1,1,1,0,0,0],
[0,0,0,0,0,1,0,0],
[0,0,1,1,1,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,1,0,0,0,0]]

t=[
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,1,0,0,0,0],
[0,0,1,1,1,0,0,0],
[0,0,0,1,0,0,0,0],
[0,0,0,1,0,1,0,0],
[0,0,0,0,1,0,0,0]]

u=[
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,1,0,0,1,0,0],
[0,0,1,0,0,1,0,0],
[0,0,1,0,0,1,0,0],
[0,0,0,1,1,1,0,0]]

ü=[
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,1,0,0,1,0,0],
[0,0,0,0,0,0,0,0],
[0,0,1,0,0,1,0,0],
[0,0,1,0,0,1,0,0],
[0,0,1,0,0,1,0,0],
[0,0,0,1,1,1,0,0]]

v=[
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,1,0,1,0,0,0],
[0,0,1,0,1,0,0,0],
[0,0,0,1,0,0,0,0]]

w=[
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,1,0,0,0,1,0,0],
[0,1,0,1,0,1,0,0],
[0,0,1,0,1,0,0,0]]

x=[
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,1,0,1,0,0,0],
[0,0,0,1,0,0,0,0],
[0,0,1,0,1,0,0,0]]

y=[
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,1,0,1,0,0,0],
[0,0,1,0,1,0,0,0],
[0,0,0,1,1,0,0,0],
[0,0,0,0,1,0,0,0],
[0,0,1,0,1,0,0,0],
[0,0,0,1,0,0,0,0]]

z=[
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,1,1,1,1,0,0],
[0,0,0,0,1,0,0,0],
[0,0,0,1,0,0,0,0],
[0,0,1,1,1,1,0,0]]

one=[
[0,0,0,1,0,0,0,0],
[0,0,1,1,0,0,0,0],
[0,1,0,1,0,0,0,0],
[0,0,0,1,0,0,0,0],  
[0,0,0,1,0,0,0,0],  
[0,0,0,1,0,0,0,0],
[0,0,0,1,0,0,0,0],
[0,1,1,1,1,1,0,0]]

two=[
[0,0,1,1,1,1,0,0],
[0,1,0,0,0,0,1,0],
[0,1,0,0,0,1,0,0],
[0,0,0,0,1,0,0,0],  
[0,0,0,1,0,0,0,0],  
[0,0,1,0,0,0,0,0],
[0,1,0,0,0,0,0,0],
[1,1,1,1,1,1,1,1]]

three=[
[0,0,1,1,1,1,1,0],
[0,1,0,0,0,0,0,1],
[1,0,0,0,0,0,1,0],
[0,0,0,1,1,1,0,0], 
[0,0,0,0,0,0,1,0], 
[1,0,0,0,0,0,0,1],
[0,1,0,0,0,0,1,0],
[0,0,1,1,1,1,0,0]]

four=[
[0,0,0,0,1,0,0,0],
[0,0,0,1,1,0,0,0],
[0,0,1,0,1,0,0,0],
[0,1,0,0,1,0,0,0],
[1,1,1,1,1,1,1,0],
[0,0,0,0,1,0,0,0],
[0,0,0,0,1,0,0,0],
[0,0,0,0,1,0,0,0]]

five=[
[1,1,1,1,1,1,1,1],
[1,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0],
[1,1,1,1,1,1,1,0],
[0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,1],
[0,1,0,0,0,0,1,0],
[0,0,1,1,1,1,0,0]]

six=[
[0,0,1,1,1,0,0,0],
[0,1,0,0,0,1,0,0],
[0,1,0,0,0,0,0,0],
[0,1,1,1,1,0,0,0],  
[0,1,0,0,0,1,0,0],  
[0,1,0,0,0,1,0,0],
[0,1,0,0,0,1,0,0],
[0,0,1,1,1,0,0,0]]

seven=[
[0,0,0,0,0,0,0,0],
[0,1,1,1,1,1,1,0],
[0,0,0,0,0,0,1,0],
[0,0,0,0,0,1,0,0], 
[0,0,1,1,1,1,1,0], 
[0,0,0,1,0,0,0,0],
[0,0,1,0,0,0,0,0],
[0,1,0,0,0,0,0,0]]

eight=[
[0,0,1,1,1,1,0,0],
[0,1,0,0,0,0,1,0],
[0,1,0,0,0,0,1,0],
[0,0,1,1,1,1,0,0], 
[0,1,0,0,0,0,1,0], 
[0,1,0,0,0,0,1,0],
[0,1,0,0,0,0,1,0],
[0,0,1,1,1,1,0,0]]

nine=[
[0,0,1,1,1,1,0,0],
[0,1,0,0,0,0,1,0],
[0,1,0,0,0,0,1,0],
[0,0,1,1,1,1,1,0],
[0,0,0,0,0,0,1,0],
[0,0,0,0,0,0,1,0],
[0,1,0,0,0,0,1,0],
[0,0,1,1,1,1,0,0]]

zero=[
[0,0,0,1,1,0,0,0],
[0,0,1,0,0,1,0,0],
[0,1,0,0,0,0,1,0],
[0,1,0,0,0,0,1,0],
[0,1,0,0,0,0,1,0],
[0,1,0,0,0,0,1,0],
[0,0,1,0,0,1,0,0],
[0,0,0,1,1,0,0,0]]

dot=[
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],  
[0,0,0,0,0,0,0,0],  
[0,0,0,0,0,0,0,0],
[0,0,0,1,1,0,0,0],
[0,0,0,1,1,0,0,0]]

comma=[
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0], 
[0,0,0,1,1,0,0,0],
[0,0,0,0,1,0,0,0],
[0,0,0,1,0,0,0,0]]

question=[
[0,1,1,1,1,1,0,0],
[1,0,0,0,0,0,1,0],
[0,0,0,0,0,0,1,0],
[0,0,0,0,0,1,0,0],
[0,0,0,0,1,0,0,0],
[0,0,0,0,1,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,1,1,0,0,0]]

at=[
[0,0,0,0,0,0,0,0],
[0,1,1,1,1,1,0,0],
[1,0,0,0,0,0,1,0], 
[1,0,1,1,1,0,1,0], 
[1,0,1,0,1,0,1,0],
[1,0,1,1,1,1,1,0],
[1,0,0,0,0,0,0,0],
[0,1,1,1,1,1,1,0]]

semicolon=[
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,1,1,0,0,0],
[0,0,0,1,1,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,1,1,0,0,0],
[0,0,0,0,1,0,0,0],
[0,0,0,1,0,0,0,0]]

exclamation=[
[0,0,0,1,1,0,0,0],
[0,0,0,1,1,0,0,0],
[0,0,0,1,1,0,0,0],
[0,0,0,1,1,0,0,0],
[0,0,0,1,1,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,1,1,0,0,0],
[0,0,0,1,1,0,0,0]]

asterisk=[
[0,0,1,0,0,1,0,0],
[0,0,0,1,1,0,0,0],
[1,1,1,1,1,1,1,1],
[0,0,0,1,1,0,0,0],
[0,0,1,0,0,1,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],]

apostrophe=[
[0,0,0,1,1,0,0,0],
[0,0,0,1,1,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0]]

doubleQuotes=[
[0,1,1,0,0,1,1,0],
[0,1,1,0,0,1,1,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0]]

slash=[
[0,0,0,0,0,0,0,1],
[0,0,0,0,0,0,1,0],
[0,0,0,0,0,1,0,0],
[0,0,0,0,1,0,0,0], 
[0,0,0,1,0,0,0,0], 
[0,0,1,0,0,0,0,0],
[0,1,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0]]

backslash=[
[1,0,0,0,0,0,0,0],
[0,1,0,0,0,0,0,0],
[0,0,1,0,0,0,0,0],
[0,0,0,1,0,0,0,0],
[0,0,0,0,1,0,0,0],
[0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,1,0],
[0,0,0,0,0,0,0,1]]

plus=[
[0,0,0,1,1,0,0,0],
[0,0,0,1,1,0,0,0],
[0,0,0,1,1,0,0,0],
[1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1],
[0,0,0,1,1,0,0,0],
[0,0,0,1,1,0,0,0],
[0,0,0,1,1,0,0,0]]

minus=[
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0]]

hashtag=[
[0,0,0,0,0,0,0,0],
[0,0,1,0,1,0,1,0],
[0,1,1,1,1,1,1,1],
[0,0,1,0,1,0,1,0],
[0,1,1,1,1,1,1,1],
[0,0,1,0,1,0,1,0],
[0,1,1,1,1,1,1,1],
[0,0,1,0,1,0,1,0]]

percentage=[
[1,1,1,0,0,0,0,1],
[1,0,1,0,0,0,1,0],
[1,1,1,0,0,1,0,0],
[0,0,0,0,1,0,0,0],
[0,0,0,1,0,0,0,0],
[0,0,1,0,0,1,1,1],
[0,1,0,0,0,1,0,1],
[1,0,0,0,0,1,1,1]]

ampersand=[
[0,0,1,1,1,1,0,0],
[0,1,0,0,0,0,1,0],
[0,1,0,0,0,0,1,0],
[0,0,1,1,1,1,0,0],
[0,1,0,1,0,0,0,0],
[0,1,0,0,1,0,1,0],
[0,0,1,0,0,1,0,0],
[0,0,0,1,1,0,1,0]]

equal=[
[0,0,0,0,0,0,0,0],
[1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1],
[0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0], 
[1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1],
[0,0,0,0,0,0,0,0]]

underscore=[
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[1,1,1,1,1,1,1,1]]

colon=[
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,1,1,0,0,0],
[0,0,0,1,1,0,0,0], 
[0,0,0,0,0,0,0,0], 
[0,0,0,1,1,0,0,0],
[0,0,0,1,1,0,0,0],
[0,0,0,0,0,0,0,0]]

dollar=[
[0,0,0,0,0,0,0,0],
[0,0,1,0,0,1,0,0],
[0,1,1,1,1,1,1,1],
[1,0,1,0,0,1,0,0],
[0,1,1,1,1,1,1,0],
[0,0,1,0,0,1,0,1],
[1,1,1,1,1,1,1,0],
[0,0,1,0,0,1,0,0]]

euro=[
[0,0,0,1,1,1,0,0],
[0,0,1,0,0,0,1,0],
[0,1,0,0,0,0,0,1],
[1,1,1,1,1,0,0,0],
[0,1,0,0,0,0,0,0],
[1,1,1,1,1,0,0,1],
[0,0,1,0,0,0,1,0],
[0,0,0,1,1,1,0,0]]

pound=[
[0,0,0,1,1,1,0,0],
[0,0,1,0,0,0,1,0],
[0,1,0,0,0,0,0,1],
[1,1,1,1,1,0,0,0], 
[0,1,0,0,0,0,0,0], 
[0,1,0,0,0,0,0,0],
[0,1,0,0,0,0,0,0],
[1,1,1,1,1,1,1,1]]

openParanthesis=[
[0,0,0,0,1,0,0,0],
[0,0,0,1,0,0,0,0],
[0,0,1,0,0,0,0,0],
[0,0,1,0,0,0,0,0],
[0,0,1,0,0,0,0,0],
[0,0,1,0,0,0,0,0],
[0,0,0,1,0,0,0,0],
[0,0,0,0,1,0,0,0]]

closeParanthesis=[
[0,0,0,1,0,0,0,0],
[0,0,0,0,1,0,0,0],
[0,0,0,0,0,1,0,0],
[0,0,0,0,0,1,0,0],
[0,0,0,0,0,1,0,0],
[0,0,0,0,0,1,0,0],
[0,0,0,0,1,0,0,0],
[0,0,0,1,0,0,0,0]]

openBracket=[
[0,0,1,1,1,0,0,0],
[0,0,1,0,0,0,0,0],
[0,0,1,0,0,0,0,0],
[0,0,1,0,0,0,0,0],
[0,0,1,0,0,0,0,0],
[0,0,1,0,0,0,0,0],
[0,0,1,0,0,0,0,0],
[0,0,1,1,1,0,0,0]]

closeBracket=[
[0,0,0,1,1,1,0,0],
[0,0,0,0,0,1,0,0],
[0,0,0,0,0,1,0,0],
[0,0,0,0,0,1,0,0],
[0,0,0,0,0,1,0,0],
[0,0,0,0,0,1,0,0],
[0,0,0,0,0,1,0,0],
[0,0,0,1,1,1,0,0]]

openBraces=[
[0,0,1,1,0,0,0,0],
[0,0,0,0,1,0,0,0],
[0,0,0,0,1,0,0,0],
[0,0,0,0,1,0,0,0],
[0,0,0,0,0,1,0,0],
[0,0,0,0,1,0,0,0],
[0,0,0,0,1,0,0,0],
[0,0,1,1,0,0,0,0]]

closeBraces=[
[0,0,0,0,1,1,0,0],
[0,0,0,1,0,0,0,0],
[0,0,0,1,0,0,0,0],
[0,0,0,1,0,0,0,0],
[0,0,1,0,0,0,0,0],
[0,0,0,1,0,0,0,0],
[0,0,0,1,0,0,0,0],
[0,0,0,0,1,1,0,0]]

graterThan=[
[0,0,0,0,0,0,0,0],
[1,1,0,0,0,0,0,0],
[0,0,1,1,0,0,0,0],
[0,0,0,0,1,1,0,0],
[0,0,0,0,0,0,1,1],
[0,0,0,0,1,1,0,0],
[0,0,1,1,0,0,0,0],
[1,1,0,0,0,0,0,0]]

lessThan=[
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,1,1],
[0,0,0,0,1,1,0,0],
[0,0,1,1,0,0,0,0],
[1,1,0,0,0,0,0,0],
[0,0,1,1,0,0,0,0],
[0,0,0,0,1,1,0,0],
[0,0,0,0,0,0,1,1]]

pipe=[
[0,0,0,1,1,0,0,0],
[0,0,0,1,1,0,0,0],
[0,0,0,1,1,0,0,0],
[0,0,0,1,1,0,0,0],
[0,0,0,1,1,0,0,0],
[0,0,0,1,1,0,0,0],
[0,0,0,1,1,0,0,0],
[0,0,0,1,1,0,0,0]]

circumflex=[
[0,0,0,1,1,0,0,0],
[0,0,1,0,0,1,0,0],
[0,1,0,0,0,0,1,0],
[1,0,0,0,0,0,0,1],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0]]



word=input("Please enter the word: ")   # EN: The user is asked to enter a word and the word is assigned to the variable named 'word'.

                                        # TR: Kullanıcıdan bir kelime girmesi istenir ve girilen kelime 'word' adlı değişkene atanır.

while word[-1]==" ":                    # EN: If the user enters a space character at the end of the word, the space character is removed.

                                        # TR: Kullanıcı kelimenin sonuna boşluk karakteri girerse, boşluk karakteri kaldırılır.

    word=word[:-1]

while not word:                         # EN: If the user does not enter any characters for the word, the user is asked to enter again.

                                        # TR: Eğer kullanıcı kelime için hiçbir karakter girmemişse, kullanıcıdan tekrar girmesi istenir.

    word=input("Please enter the word (cannot be empty): ")

while word.isspace():                  # EN: If the user enters only space character(s) for the word, the user is asked to enter again.

                                        # TR: Eğer kullanıcı kelime için yalnızca boşluk karakter(ler)i girerse, kullanıcıdan tekrar girmesi istenir.

    word=input("Please enter the word (it cannot contain only whitespace characters): ")

pixel=input("Please enter the pixel character(s): ")    # EN: The user is asked to enter the pixels that are the building blocks of the word
                                                        # to be written in text_art_x_8x8 format. Up to 3 characters are supported.
                                                        # None of these characters can be a space character.

                                                        # TR: Kullanıcıdan text_art_x_8x8 formatında yazılacak kelimenin yapı taşları olan
                                                        # piksel karakter(ler)ini girmesi istenir. En fazla 3 karakter desteklenir.
                                                        # Bu karakterlerden hiçbiri boşluk karakteri olamaz.

while pixel[-1]==" ":                                                               # EN: If the user enters a space character at the end of the pixel character(s),
                                                                                    # the space character is removed.

                                                                                    # TR: Kullanıcı piksel karakter(ler)i için sona boşluk karakteri girerse,
                                                                                    # boşluk karakteri kaldırılır.

    pixel=pixel[:-1]

while len(pixel)>3:                                                                # EN: If the user enters more than three characters
                                                                                    # for the pixel character(s),
                                                                                    # the user is asked to enter again.

                                                                                    # TR: Eğer kullanıcı piksel karakter(ler)i için
                                                                                    # üçten fazla karakter girerse,
                                                                                    # kullanıcıdan tekrar girmesi istenir.
    pixel=input("Please enter the pixel character(s) (maximum 3 character): ")

while " " in pixel:                                                                # EN: If the user's pixel character input includes a space character,
                                                                                    # the user is asked to enter again.

                                                                                    # TR: Kullanıcının piksel karakter(ler)i girişi bir boşluk karakteri
                                                                                    # içeriyorsa, kullanıcıdan piksel karakter(ler)i tekrar girmesi istenir.

    pixel=input("Please enter the pixel character(s) (without space): ")

while not pixel:                                                                    # EN: If the user does not enter any characters for the pixel character(s),
                                                                                    # the user is asked to enter again.

                                                                                    # TR: Kullanıcı piksel karakter(ler)i için hiçbir karakter girmemişse,
                                                                                    # kullanıcıdan tekrar girmesi istenir.

    pixel=input("Please enter the pixel character(s) (cannot be empty): ")

while pixel.isspace():                                                              # EN: If the user enters only space character(s) for
                                                                                    # the pixel character(s), the user is asked to enter again.

                                                                                    # TR: Eğer kullanıcı piksel karakter(ler)i için yalnızca
                                                                                    # boşluk karakter(ler)i girerse, kullanıcıdan tekrar girmesi istenir.

    pixel=input("Please enter the pixel character(s) (it cannot contain only whitespace characters): ")

for line in range(8):                   # EN: This for loop allows us to treat the lists of each matrix as rows.

                                        # TR: Bu for döngüsü, her bir matrisin listelerini satır şeklinde ele almamızı sağlar.

    for letter in word:                 # EN: This for loop is used to print the lists of the matrix associated with each character, 
                                        # determined by the previous for loop.

                                        # TR: Bu for döngüsü, her bir karakter ile ilgili matrisin bir üstteki for döngüsü ile belirlenen
                                        # listelerini yazdırmak için kullanılır.

        # EN: Each character in the variable 'word' is associated with the matrix using conditional expressions.
        # The matrix associated with each character reads the corresponding list of the matrix
        # according to the row numbers determined by the outermost for loop.
        # Below the conditional expressions, a result is printed according to each element of the lists.
        # If the element is 1, a pixel is printed, otherwise a space character equal to the length of the pixel character is printed.
        # If the end of the line is reached, three space characters is printed to create a space between two characters.
        # During this time, no lines are skipped and each character or the word is printed side by side.

        # TR: 'word' değişkenindeki her karakter, koşullu ifadeler kullanılarak matris ile ilişkilendirilir.
        # Her karakterle ilişkilendirilen matris, en dıştaki for döngüsü tarafından belirlenen satır numaralarına göre matrisin ilgili listesini okur.
        # Koşullu ifadelerin altında, listelerin her bir elemanına göre bir sonuç yazdırılır.
        # Eleman 1 ise bir piksel yazdırılır, aksi takdirde piksel karakterinin uzunluğuna eşit bir boşluk karakteri yazdırılır.
        # Satırın sonuna ulaşılırsa, iki karakter arasında boşluk oluşturmak için iki boşluk karakteri yazdırılır.
        # Bu süre zarfında hiçbir satır atlanmaz ve her karakter veya kelime yan yana yazdırılır.

        if letter=="A":
            for column in range(8):
                if A[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")
                if column==8:    
                       print("  ",end="")
        if letter=="a":
            for column in range(8):
                if a[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")
                if column==8:    
                       print("  ",end="")

        if letter=="B":
            for column in range(8):
                if B[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")
    
        if letter=="b":
            for column in range(8):
                if b[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")
    
        if letter=="C":
            for column in range(8):
                if C[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")
    
        if letter=="c":
            for column in range(8):
                if c[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")
    
        if letter=="Ç":
            for column in range(8):
                if Ç[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")
    
        if letter=="ç":
            for column in range(8):
                if ç[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")
    
        if letter=="D":
            for column in range(8):
                if D[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")
    
        if letter=="d":
            for column in range(8):
                if d[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")
    
        if letter=="E":
            for column in range(8):
                if E[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")
    
        if letter=="e":
            for column in range(8):
                if e[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")
    
        if letter=="F":
            for column in range(8):
                if F[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")
    
        if letter=="f":
            for column in range(8):
                if f[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")
    
        if letter=="G":
            for column in range(8):
                if G[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="g":
            for column in range(8):
                if g[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")
    
        if letter=="Ğ":
            for column in range(8):
                if Ğ[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="ğ":
            for column in range(8):
                if ğ[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="H":
            for column in range(8):
                if H[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="h":
            for column in range(8):
                if h[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="I":
            for column in range(8):
                if I[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="ı":
            for column in range(8):
                if ı[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="İ":
            for column in range(8):
                if İ[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="i":
            for column in range(8):
                if i[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="J":
            for column in range(8):
                if J[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="j":
            for column in range(8):
                if j[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="K":
            for column in range(8):
                if K[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="k":
            for column in range(8):
                if k[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="L":
            for column in range(8):
                if L[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="l":
            for column in range(8):
                if l[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="M":
            for column in range(8):
                if M[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="m":
            for column in range(8):
                if m[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="N":
            for column in range(8):
                if N[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="n":
            for column in range(8):
                if n[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="O":
            for column in range(8):
                if O[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="o":
            for column in range(8):
                if o[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="Ö":
            for column in range(8):
                if Ö[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="ö":
            for column in range(8):
                if ö[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="P":
            for column in range(8):
                if P[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="p":
            for column in range(8):
                if p[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="Q":
            for column in range(8):
                if Q[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="q":
            for column in range(8):
                if q[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="R":
            for column in range(8):
                if R[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="r":
            for column in range(8):
                if r[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="S":
            for column in range(8):
                if S[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="s":
            for column in range(8):
                if s[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="Ş":
            for column in range(8):
                if Ş[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="ş":
            for column in range(8):
                if ş[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="T":
            for column in range(8):
                if T[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="t":
            for column in range(8):
                if t[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="U":
            for column in range(8):
                if U[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="u":
            for column in range(8):
                if u[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="Ü":
            for column in range(8):
                if Ü[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="ü":
            for column in range(8):
                if ü[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="V":
            for column in range(8):
                if V[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="v":
            for column in range(8):
                if v[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="W":
            for column in range(8):
                if W[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="w":
            for column in range(8):
                if w[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="X":
            for column in range(8):
                if X[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="x":
            for column in range(8):
                if x[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")
        if letter=="Y":
            for column in range(8):
                if Y[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="y":
            for column in range(8):
                if y[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="Z":
            for column in range(8):
                if Z[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="z":
            for column in range(8):
                if z[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="1":
            for column in range(8):
                if one[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="2":
            for column in range(8):
                if two[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="3":
            for column in range(8):
                if three[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="4":
            for column in range(8):
                if four[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="5":
            for column in range(8):
                if five[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="6":
            for column in range(8):
                if six[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="7":
            for column in range(8):
                if seven[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="8":
            for column in range(8):
                if eight[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")


        if letter=="9":
            for column in range(8):
                if nine[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="0":
            for column in range(8):
                if zero[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter==".":
            for column in range(8):
                if dot[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter==",":
            for column in range(8):
                if comma[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="?":
            for column in range(8):
                if question[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="@":
                for column in range(8):
                    if at[line][column]==1:
                        print(pixel,end="")
                    else:
                        for variable in range(len(pixel)):
                            print(" ",end="")

        if letter==";":
            for column in range(8):
                if semicolon[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="!":
            for column in range(8):
                if exclamation[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="*":
            for column in range(8):
                if asterisk[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="'":
            for column in range(8):
                if apostrophe[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="\"":
            for column in range(8):
                if doubleQuotes[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="/":
            for column in range(8):
                if slash[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="\\":
            for column in range(8):
                if backslash[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="+":
            for column in range(8):
                if plus[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="-":
            for column in range(8):
                if minus[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="#":
            for column in range(8):
                if hashtag[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="%":
            for column in range(8):
                if percentage[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="&":
            for column in range(8):
                if ampersand[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="=":
            for column in range(8):
                if equal[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="_":
            for column in range(8):
                if underscore[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter==":":
            for column in range(8):
                if colon[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="$":
            for column in range(8):
                if dollar[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="€":
            for column in range(8):
                if euro[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="£":
            for column in range(8):
                if pound[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="(":
            for column in range(8):
                if openParanthesis[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter==")":
            for column in range(8):
                if closeParanthesis[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="[":
            for column in range(8):
                if openBracket[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="]":
            for column in range(8):
                if closeBracket[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="{":
            for column in range(8):
                if openBraces[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="}":
            for column in range(8):
                if closeBraces[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter==">":
            for column in range(8):
                if graterThan[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="<":
            for column in range(8):
                if lessThan[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="|":
            for column in range(8):
                if pipe[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")

        if letter=="^":
            for column in range(8):
                if circumflex[line][column]==1:
                    print(pixel,end="")
                else:
                    for variable in range(len(pixel)):
                        print(" ",end="")
        print("   ",end="")                     # EN: Three space characters is printed to create a space between two characters
                                                # after the lists of a matrix are printed.
                                                # During this time, no lines are skipped.

                                                # TR: Bir matrixin listeleri yazdırıldıktan sonra
                                                # iki karakter arasında boşluk oluşturmak için üç boşluk karakteri yazdırılır.
                                                # Bu süre zarfında alt satıra geçilmez.

    print("")                                   # EN: After printing all the characters in the word assigned to the variable 'word'
                                                # according to the lists of that loop in the corresponding matrices, move to the next line.

                                                # TR: 'word' adlı değişkene atanan kelimedeki bütün karakterlerin ilgili matrislerdeki
                                                # o döngüye ait listelere göre yazdırıldıktan sonra, bir alt satıra geçilir.

input()                                         # EN: The program waits for the user to press ENTER key to close the program.
    
                                                # TR: Program kapanmak için kullanıcının ENTER tuşuna basmasını bekler.