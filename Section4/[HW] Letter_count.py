chars =  input("Enter the sentence you want to count here: ").lower()
order_list = []
for i in range(ord("a"), ord("z") + 1):
    order_list.append(chr(i))

alpha_counts ={}
first_counts = {}
for letter in chars:
    first_counts[letter] = first_counts.get(letter, 0) + 1

for i in order_list:
     for key in first_counts.keys():
         if i == key:
            alpha_counts[i] = first_counts[i]
for letter, number in alpha_counts.items():
    print("{0} {1}".format(letter, number))

