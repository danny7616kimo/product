product = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:') 
	price = int(price)
	p = []
	p = [name, price]
	product.append(p)

print(product)

for p in product:
	print(p)
	print(p[0], '的價格是', p[1])


with open('proudcts.csv', 'w', encoding= 'utf-8') as f:
	f.write('商品,心中價格\n')
	for p in product:
		f.write(p[0] + ',' + str(p[1]) + '\n' )