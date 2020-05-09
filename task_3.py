"""
Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
Если введённое слово не найдено в этом списке, оно помечается как "ошибка".

Попробуем написать подобную систему.

На вход программе первой строкой передаётся количество dd известных нам слов, после чего на dd строках указываются эти слова. Затем передаётся количество ll строк текста для проверки, после чего ll строк текста.

Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.
------------------------
Sample Input:
4
champions
we
are
Stepik
3
We are the champignons
We Are The Champions
Stepic
------------------------
Sample Output:
stepic
champignons
the
"""

# d = int(input())
d = 4
# ws = set()
# for i in range(d):
#     ws.add(input())
# ws = {input().lower() for i in range(d)}
ws = {"champions", "we", "are", "stepik"}
# l = int(input())
l = 3
# ls = {input().lower() for i in range(l)}
ls = {"we are the champignons", "we are the champions", "stepic"}
r = set()
for s in ls:
    a = set(s.split(" "))
    for c in a:
        if c not in ws:
            r.add(c)

for s in r:
    print(s)
