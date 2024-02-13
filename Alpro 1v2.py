harga_Awal = 650000
harga_kedua = 685000
gram_emas = 25
keuntungan_rupiah =(harga_kedua - harga_Awal)* gram_emas
keuntungan_persen =(keuntungan_rupiah / (harga_Awal *gram_emas))*100
TotalPertama = harga_kedua * gram_emas
print('Keuntungan Gerard sesudah membeli emas : Rp.', keuntungan_rupiah ,'dan',keuntungan_persen,'%')
print('Total uang keuntungan pertama : Rp.', TotalPertama)
harga_terakhir = 715000
gram_terbaru = 40

TotalTerakhir = harga_terakhir * gram_terbaru #gram dengan emas yang baru dibeli setelah keuntungan pertama 
KeuntunganRupiah_terakhir = (TotalTerakhir - TotalPertama)
persen_terakhir = (KeuntunganRupiah_terakhir/(harga_kedua*gram_terbaru))*100
print('Keuntungan Final Gerard sejak keuntungan pertama : Rp. ',KeuntunganRupiah_terakhir, 'dan',persen_terakhir,'%')
print('Total uang Terkini : Rp.',TotalTerakhir)