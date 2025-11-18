'''marks=[3,4,2,5,5,5,3,4,2,5,3]
print(marks[0])
print(marks[1])
print(sum(marks))
print(max(marks))
print(min(marks))





x = input("введи оценки через запятую= ").split
print(x)
st = []
for g in range(len(x)):
    st.append (int(x[g]))
result = ','.join(x)
pint = (sum(st)/len(st))
print(result, "| Средний балл ", pint)

a = [d for d in range (10)]
print(a) 
list_of_meal = [1,3,42,5,1,2,1000]
fruits = ['apple', 'banana', 'orange']
more_fruits = ['kiwi', 'mango']
fruits.extend(more_fruits)
print(fruits)
fruits.insert(1, 'pear')
print(fruits)
fruits.append('apple')
position = fruits.index('orange')
count_apple = fruits.count('apple')
fruits.sort(reverse=True)
fruits.remove('apple')
print(fruits)
o = int(input("vvedi visoty: "))
for f in range (o):
    print(" "*((o-1)-f) +"*"* (f*2+1))
g = input("введи слово на ангийском: ").split(" ")
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..'
}
for word in g:
    products_1 = []
    for letter in word.upper():
        if letter in morse_code_dict:
            products_1.append(morse_code_dict[letter])
    p = "".join(products_1)
    print(p) '''
print("apple")