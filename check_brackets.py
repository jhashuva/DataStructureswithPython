def find_mismatch(text):
    opening_brackets = list()#empty list
    position = list()
    for i,pos in enumerate(text):
        if pos in "({[":
            opening_brackets.append(pos)
            position.append(i)
        if pos in ")}]":
            if len(opening_brackets)>0:
                if pos == ')' and opening_brackets[-1]=="(":
                    opening_brackets.pop()
                    position.pop()
                elif pos =="}" and opening_brackets[-1]=='{':
                    opening_brackets.pop()
                    position.pop()
                elif pos ==']' and opening_brackets[-1]=='[':
                    opening_brackets.pop()
                    position.pop()
                else:
                    #return i+1  #
                    return 0
            else:
                #return i+1
                return 0
    if len(opening_brackets)==0:
        #return 'Success'   #return 1
        return 1
    else:
        #return position[0]+1   #return 0
        return 0
def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)

if __name__=="__main__":
    main()