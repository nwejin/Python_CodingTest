cnt = 0
answer = ''

def dfs (queue, word):
    global cnt, answer

    if queue == word:
        answer = cnt
        return

    if len(queue) == 5:
        return

    alpha = ['A','E','I','O','U']
    for i in range(5):
        cnt += 1
        queue.append(alpha[i])
        dfs(queue, word)
        queue.pop()
    return

def solution(word):
    word = list(word)
    queue = []
    dfs(queue,word)
    return  answer