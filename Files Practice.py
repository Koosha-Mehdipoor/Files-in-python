myquiz = open('questions.txt','r')
lines = myquiz.readlines()
correct_answers = 0
questions = 0
for i in range(0,len(lines)):
    split = lines[i].split(sep ="=")
    print(split[0] + "=")
    inp = input("Please answer the question: ")
    if inp == split[1].split(sep ="\n")[0]:
        correct_answers += 1

    result = open("results.txt","a")
    result.write(inp + "\n")
    result.close()

#Your final score is n/m
print(f"Your final score is {correct_answers}/{len(lines)}")