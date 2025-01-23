import time
q= ["What is the capital of Italy?","Which country has highest GDP?","Who is the captain of Indian cricket team in 2024?","Who is the PM of India?"]
a= ["Rome","USA","Rohit","Modi"]
op1= ["Milan","Pisa", "Torino", "Rome"]
op2 =["USA", "Germany", "China", "India"]
op3 =["Rohit","Dhoni","Kohli","Bumrah"]
op4 =["Modi","Rahul","Kejriwal","Amit"]
i=0
while i < 1:
    #print(len(q))
    print("Welcome to KBC program! Please read questions carefully and answer") 
    print("Now, Let's start!")
    time.sleep(2)  
    print("Your first Question is:\n" ,q[0])
    opa1=input(f"Select your options are :{op1} \n")
    if(a[0]==opa1):
        print(".....Congrats! you won 100$.....\n")
    else:
        print("Sorry! your Answer is wrong and you won nothing")
        break
    time.sleep(2)
    print("Your Second Question is:\n" ,q[1])

    opa2=input(f"Select your options are :{op2} \n")
    if(a[1]==opa2):
        print("............... Congrats! you won 200$ ..............\n")
        time.sleep(2)
    else:
        print("Sorry! your Answer is wrong and you'll receive 100$")
        time.sleep(2)
        break

    time.sleep(2)
    print("Your Third Question is:\n" ,q[2])
    opa3=input(f"Select your options are :{op3}\n")

    if(a[2]==opa3):
        print("........Congrats! you won 500$............\n")
    else:
        print("Sorry! your Answer is wrong and you'll receive 200$")
        time.sleep(2)
        break

    time.sleep(2)
    print("Your Last Question is for 1000$:\n" ,q[3])
    opa4=input(f"Your options are :{op4}\n")

    if(a[3]==opa4):
        print(".........Congrats on your win! you won 1000$............")
        print("Enjoy 1000$ :) Claps,Claps...")
        time.sleep(3)
        print("Game ends here!")
        
    else:
        print("Sorry! your question is wrong and  and you'll receive 500$")
        print("You played well!")
        time.sleep(2)
        break
    i=i+1