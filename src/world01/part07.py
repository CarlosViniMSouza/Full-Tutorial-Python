class IfStatement:
    choose = "student" # 'student', or 'proof', or 'collaborator'

    if (choose == "student"):
        print("\nYou are a student")
    elif (choose == "proof"):
        print("\nYou are a proof")
    elif (choose == "collaborator"):
        print("\nYou are a collaborator")
    else:
        print("Error!")

    # output: You are a student
