class Solution:
    def interpret(self, command: str) -> str:
        temp = ""
        for i in range(len(command) - 1):
            if command[i] == "(" and command[i+1] == ')':
                temp+='o'
            else:
                temp+=command[i]
        temp+=command[-1]
        res = ""
        for t in temp:
            if t != '(' and t != ')':
                res+=t
        return res