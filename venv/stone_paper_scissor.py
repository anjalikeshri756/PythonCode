# computer takes some random option
# user have to choose one option
# if both user have selected same--its draw
# user1 stone->user2-paper--->user2 won
# user1 paper-user2 scissor---->user2 won
# user1 scissor user2 stone----user2 won
comp_input=input("Select option between stone, paper, scissor:")
user_input=input("user plz Select option between stone, paper, scissor: ")

if (comp_input=='stone' and user_input=='paper')or (comp_input=='paper' and user_input=='scissor') or (comp_input=='scissor' and user_input=='stone'):
    print("user_input won")
elif(comp_input=='paper' and user_input=='stone')or (comp_input=='scissor' and user_input=='paper') or (comp_input=='stone' and user_input=='scissor'):
    print("comp_input won")
else:
    print("its a draw")