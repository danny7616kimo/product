import os #operating system

#讀取檔案
def read_file(filename):
	product = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			product.append([name,price])						
	return product

#讓使用者輸入
def user_input(product):
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
	return product

#印出所有購買紀錄
def print_products(product):
	for p in product:
		print(p)
		print(p[0], '的價格是', p[1])

#寫入檔案
def write_file(filename, product):
	with open('filename', 'w', encoding= 'utf-8') as f:
		f.write('商品,心中價格\n')
		for p in product:
			f.write(p[0] + ',' + str(p[1]) + '\n' )

def main():
	filename = 'proudcts.csv'
	if os.path.isfile(filename):
		print('YES 有喔')
		product = read_file(filename)
	else:
		print('e04  沒有')

	product = user_input(product)
	print_products(product)
	write_file('proudcts.csv', product)

main()