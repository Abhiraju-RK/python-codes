#find even number in the list 1

u=[4,5,2,8,40,27,32]
find_even=[even for even in u if even%2 == 0]
print(find_even)


# sum of all element 2

my_list=[1,2,3,4]
sum_list=sum(my_list)
print(sum_list)

# given num reverse 3

given_num=input("enter number :")
reverse_num=given_num[::-1]
print(reverse_num)

# item startswith ca 4

item_input=["cat","bat","candle","fan"]
item_startswith=[item for item in item_input if item.startswith("ca")]
print(item_startswith)

# find palindrome words in a list 5

given_words=['level','noon','madam','python','world']
to_palin=[words for words in given_words if words==words[::-1]]
print(to_palin)


# find length of list of string 6

string_input=['apple','banana','cherry']
length_string=[len(fruit) for fruit in string_input]
print(length_string)

# print pattern 7

for i in range(1,6):
    print("* " *i)

for x in range(5,0,-1):
    print("* "*x)

# find all indices of largest number 8

numbers = [3, 5, 7, 2, 7, 5]
large_num = max(numbers)
total = [i for i, num in enumerate(numbers) if num == large_num]
print(total)

#list adding

input_list = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
input_list[2][1][2].extend(["h", "i", "j"])
print(input_list)






