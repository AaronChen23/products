products = []

while True:
	name = input("請輸入你買的商品名稱: ")
	if name == "q":
		break
	price = input("請輸入你買的商品價格: ")

	p =[name, price]
	products.append(p)
print(products)

for item in products:
	print("你買的", item[0], "是", item[1], "元")



