# Create a bucket list for Summer!

print("Add to your bucket list for Senior Summer!!\n")

items = []

while True:
    item = input("Enter your item, type 'all set' to finish):  ")

    if item == "all set":
        break
    items.append(item)
    print(f"{item.lower ()} , sounds exciting!")

if items:
    print("\n Looking forward to these this summer! ")

    for item in items:
        print(f"~{item.title()}")
else: 
    print("Nothing set in the bucket yet ;)")