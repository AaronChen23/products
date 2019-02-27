import os
products = []

if os.path.isfile("products.csv"):
	print("有找到檔案嘞")
	with open("products.csv", "r") as f:
		for line in f:
			if "name,price" in line :
				continue
			print(line.strip().split(","))

else:
	print("找不到檔案")

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

with open("products.csv", "w") as f:
	#f.write("商品" + "," + "價格" + "\n")
	f.write("name,price\n")
	for p in products:
		f.write(p[0] + "," + p[1] + "\n")




