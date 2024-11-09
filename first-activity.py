with open('the_essay.txt' , 'w') as file:
    file.write("Hi! I am the computer")
file.close()

with open('the_essay.txt' ,  'r') as file:
    data = file.readlines()
    print("Words in this file are....")
    for line in data:
        word = line.split()
        print(word)
file.close()