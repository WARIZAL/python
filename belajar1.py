apple_price=2
money=10
input_count=input("mau brapa apel ? :")
count=int(input_count)
total_price=apple_price*count

print('anda akan membeli'+str(count)+'apel')
print('harga total adalah'+str(total_price)+'dolar')

if mony > total_price:
    print('anda telah membeli'+str(count)+'apel')
    print('uang anda tinggal'+str(mony-total_price)+'dolar')
elif money==total_price:
    print('anda telah membeli'+str(count)+'apel')
    print('dompet anda sekarang  kosong')
else:
    print('uang anda tidak mencukupi')
    print('anda tidak dapat membeli apel sebanyak itu')




    