data = input("give input").strip()
x=data.find(" ")
print(data[x:].strip()+ " " + data[:x])