string = input("Введите два слова: ")

words = string.split()

words[0], words[1] = words[1], words[0]

output_string = ' '.join(words)
print("Результат:", output_string)


########################################################

input = input("Введите строку из слов: ")
word_count = input.count(" ") + 1
print("Количество слов в строке:", word_count)

#######################################################

text = "Прошедший 2020 год был непростым для многих"
new_text = text.replace("2020", "2022")
print(new_text)


################################################################
nums = []
while True:
    num = int(input())
    nums.append(num)
    if sum(nums) == 0:
        break

squares_sum = sum([num ** 2 for num in nums])

print(squares_sum)

##############################################
grades = input("Введите список оценок : ").split()
grades = [int(x) for x in grades]

fives = grades.count(5)
fours = grades.count(4)
threes = grades.count(3)
twos = grades.count(2)

avg_grade = sum(grades) / len(grades)

print(fives, fours, threes, twos)
print(avg_grade)
##############################################

grades = input("Введите оценки через пробел: ")
grades = grades.replace("2", "3")
print(grades)


