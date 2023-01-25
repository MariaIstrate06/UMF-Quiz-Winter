entries = []
with open("./data/diabet.txt", "r", encoding="utf-8") as file:
    count = 0
    for line in file:
        # print(line)
        entries.append(line)
questions = []
countQ = 0
countA = 0
answers = []
total_answers = []
is_correct = []
for i in range(0, len(entries)):
    if i % 11 == 0:
        # question
        questions.append(entries[i])
        countQ += 1
    else:
        if (entries[i][len(entries[i]) - 2]) == "x":
            is_correct.append("true")
        else:
            is_correct.append("false")
        if i % 11 == 1:
            # first answer for question
            total_answers.append(answers)
            answers = [entries[i]]

        else:
            answers.append(entries[i])


def clean_up_string(string):
    if string[len(string) - 2] == "x":
        string = string[0:len(string) - 3]
    else:
        string = string[0:len(string) - 1]
    return string


total_answers = total_answers[1:len(total_answers)]
questions = questions[0:len(questions) - 1]
# for i in range(0, len(questions)):
#     print(f"QUESTION{i}: {clean_up_string(questions[i])}")
#     for j in range(0, len(total_answers[i])):
#         print(f"Answer{j}: {clean_up_string(total_answers[i][j])}, {is_correct[i * 10 + j]}")
#
with open('diabet.json', 'w', encoding="utf-8") as file:
    file.write('{ \n "entries" : [ \n')
    for i in range(0, len(questions)):
        file.write('{ \n')
        file.write(f' "Question" : "{clean_up_string(questions[i])}",\n ')
        file.write(f' "Answers" : [\n')
        for j in range(0, len(total_answers[i])):
            # if is_correct[i * 10 + j]:
            #     truth_val = "true"
            # else:
            #     truth_val = "false"
            if j == len(total_answers[i]) - 1:
                # fara virgula
                str = '{' + '"ans" :' + ' " ' + clean_up_string(total_answers[i][j]) + ' ","correct" : "' + is_correct[
                    i * 10 + j] + '" }\n'
            else:
                str = '{' + '"ans" :' + ' " ' + clean_up_string(
                    total_answers[i][j]) + ' ","correct" : "' + is_correct[i * 10 + j] + '" },\n'

            file.write(str)
        file.write(']')
        if i == len(questions) - 1:
            file.write('}')
        else:
            file.write('},')
    file.write('] \n }')
