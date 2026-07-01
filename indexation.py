notes = [
    [10,15,12,14],
    [0,15,12,14],
    [0,15,12,14],
    [0,15,12,14]
]
col = len(notes[0])
lig = len(notes)
posmax = 2
# for i in range(lig):
#     print(f'ligne {i+1} : {notes[i]}')
    # for j in range(col):
    #     print(notes[i][j], end=' ')
    # print()

for m in range(len(notes[posmax])):
    print(f'note {m+1} : {notes[posmax][m]}')