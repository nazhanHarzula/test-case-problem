# Test Case Problem

1. Calculate Mean and Median
Input
Array of integers which will contain many parts. Each part is sorted by
ascending order.
Task
Calculate mean and median for each part
Input Example
[3, 4, 6, 17, 25, 21, 23]
Expected Output
[
{
mean: 11,
median: 6
},
{
mean: 22,
median: 22
}
]
Explanation
[3, 4, 6, 17, 25, 21, 23]
The input can be separated into 2 parts which are (3, 4, 6, 17, 25) and (21, 23)
because each part should be sorted by ascending order, and 21 is less than 25. Mean of (3, 4, 6, 17, 25) is 11 and the median is 6. Mean of (21, 23) is 22 and the median is 22.
2. Convert Currency
Input
Array of objects. Each object has 2 keys, amount and currency.
Task
Read the doc of Frankfurter API (https://www.frankfurter.app/docs/)
Convert all the inputs into amount in USD.
Input Example
[
{ “amount”: 15000.0, “currency”: “IDR” },
{ “amount”: 3.1, “currency”: “EUR” }
]
Expected Output
[ 1, 2.3 ]
3. Hitung berapa lembar uang
Anda sedang berbelanja sebuah barang, tapi penjual hanya memperbolehkan
Anda untuk membayar dengan jumlah lembar uang yang sesuai dengan
permintaannya. Buatlah sebuah function untuk menentukan pecahan mata
uang yang dibutuhkan untuk membayar barang tersebut. (Menggunakan
pecahan uang kertas Rupiah)
Input
harga_barang, jumlah_lembar
0 < harga barang < 100000
0 < jumlah_lembar < 10
Input Example 1
17000, 1
Expected Output
[20000]
Explanation
Untuk memenuhi transaksi sejumlah 17000 dengan 1 lembar uang, maka
pecahan mata uang terdekat yang dapat digunakan adalah pecahan 20000.
4. Perpustakaan
Anda ditugaskan untuk merancang sebuah web-app untuk sebuah
perpustakaan. Aplikasi ini harus dapat mencari dan menampilkan buku yang
tersedia di perpustakaan, serta dapat mencatat transaksi peminjaman dan
pengembalian buku.
Buatlah Database Schema dan Application Architecture Diagram untuk
aplikasi tersebut!
