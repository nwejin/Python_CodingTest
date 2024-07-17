def solution(id_pw, db):
    answer = 'fail'

    for j in range(len(db)):
        # print(db[j])
        if db[j][0] == id_pw[0] and db[j][1] == id_pw[1]:
            answer = 'login'
            break
        elif id_pw[0] == db[j][0] and id_pw[1] != db[j][1]:
            answer = 'wrong pw'

    return answer

print(solution(["meosseugi", "1234"],[["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]] ))