a = 'N321-CIAFBI3'
b = 'F3-FI12I'
c = 'FBI-12'
d = 'OVO-JE-CIA'
e = 'KRIJUMCAR1'
inp_uts = [a,b,c,d,e]
for i in range(len(inp_uts)):
    if isinstance(inp_uts[i], str):
        for j in range(len(inp_uts[i])):
            if inp_uts[i][j] == 'F':
                if inp_uts[i][j] + inp_uts[i][j+1] + inp_uts[i][j+2] == 'FBI':
                    print(i)
                elif inp_uts[i][j] + inp_uts[i][j+1] + inp_uts[i][j+2] != 'FBI':
                    continue
                else:
                    print('HE GOT AWAY!')
'''for i in range(len(inp_uts)):
    if isinstance(inp_uts[i], str):
        for j in inp_uts[i]:
            if inp_uts[i][j] == 'F':
                if inp_uts[i][j] + inp_uts[i][j+1] + inp_uts[i][j+2] == 'FBI':
                    print(i)
                else:
                    print('HE GOT AWAY!')'''

      
