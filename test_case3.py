import itertools

list_eligible_money = [1000, 10000, 20000]
dict_lembar_uang = {
    "17000, 1",
    "23000, 4",
    "20000, 2",
    "15000, 6",
}

for data in dict_lembar_uang:
    list_split = data.split(",")
    harga_barang = int(list_split[0])
    lembar_uang = int(list_split[1])
    
    if (harga_barang > 0 and harga_barang <= 100000) and (lembar_uang > 0 and lembar_uang <= 10):
        if lembar_uang <= 1:
            index_search = [value for value in list_eligible_money if value <= harga_barang]
            print(f"Output : {[list_eligible_money[len(index_search)]]} dan lembar ({lembar_uang}) serta jumlah harga barang ({harga_barang})")
        else:
            ten_thousand = (harga_barang // 10000) * 10000
            thousand = ((harga_barang - ten_thousand))
            
            list_eligible_ten_thousand = [value for value in list_eligible_money if value <= ten_thousand]
            list_eligible_thousand = [value for value in list_eligible_money if value <= thousand]
            list_put_ten_thousand = []
            list_put_thousand = []
            
            # Posibilities of ten thousand
            for L in range(0, len(list_eligible_ten_thousand)+1):
                for subset in itertools.combinations(list_eligible_ten_thousand, L):
                    if sum(list(subset)) == ten_thousand:
                        list_put_ten_thousand.append(list(subset))
            
            count = 0
            for vals in list_eligible_ten_thousand:
                while sum([vals] * count) != ten_thousand:
                    count+=1
                list_put_ten_thousand.append([vals] * count)    
                count = 0
            
            # Posibilities of thousand
            for L in range(0, len(list_eligible_thousand)+1):
                for subset in itertools.combinations(list_eligible_thousand, L):
                    if sum(list(subset)) == thousand:
                        list_put_thousand.append(list(subset))
            
            count = 0
            for vals in list_eligible_thousand:
                while sum([vals] * count) != thousand:
                    count+=1
                list_put_thousand.append([vals] * count)
                count = 0
            
            output = []               
            for i in range(len(list_put_ten_thousand)):
                for j in range(len(list_put_thousand)):
                    if lembar_uang == (len(list_put_ten_thousand[i]) +len(list_put_thousand[j])):
                        if output != list_put_ten_thousand[i]+ list_put_thousand[j]:
                            output = list_put_ten_thousand[i]+ list_put_thousand[j]
            print(f"Output : {output} dan lembar ({lembar_uang}) serta jumlah harga barang ({harga_barang})")
    else:
        print("Melebihi maximum")
