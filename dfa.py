
#Problem 1. Design a Deterministic Finite State Automaton (DFA) that recognizes a language of your choice, but the DFA must have at least four states to recognize the language effectively. You have the freedom to select the language you want the DFA to recognize but ensure that there are at least four states in the DFA. (10 points)

def dfa(string):
    currstate = "q0"
    endstate = "q3"
    path = []
    for char in string:
        if char == "a": #checks if the next string will be a if not it will check b
            if currstate == "q0":
                currstate = "q0"
                path.append(currstate)
            elif currstate == "q1":
                currstate = "q1"
                path.append(currstate)
            elif currstate == "q2":
                currstate = "q2"
                path.append(currstate)
            elif currstate == "q3":
                currstate = "q3"
                path.append(currstate)
        elif char == "b":
            if currstate == "q0":
                currstate = "q1"
                path.append(currstate)
            elif currstate == "q1":
                currstate = "q2"
                path.append(currstate)
            elif currstate == "q2":
                currstate = "q3"
                path.append(currstate)
            elif currstate == "q3":
                currstate = "q3"
                path.append(currstate)
        else:
            return "This is an invalid string"
   # return currstate == endstate
 
    if currstate == endstate:
        print("This is a valid string")
        print("Path Taken:")
        return path

    else:
        return "This is an invalid string"  

test = "baaab"

# accept strings of length 5 or greater 
    #that end with the sequence 'a*b' . 

print(dfa(test))