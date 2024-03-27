
#Problem 2. Design a Non-Deterministic Finite Automaton (NFA) that recognizes a language of your choice. The NFA should be designed to effectively recognize the chosen language, Be creative in your choice of language and design an NFA that captures it. Highlight any non-deterministic choices in the NFA. (10 points)

import itertools #used to concatenate string at the end

def nfa(string):
    currstates = {"q0"} 
    endstate = "q3"
    path = []
    for char in string:
        nextstates = []  
        for state in currstates:
            if char == "a":
                if state == "q0":
                    nextstates.append("q0")
                    nextstates.append("q1")  
                elif state == "q1":
                    nextstates.append("q3")

                elif state == "q2":
                    nextstates.append("q2")
                    nextstates.append("q3")
                
                elif state == "q3":
                    nextstates.append("q3")

            elif char == "b":
                if state == "q0":
                    nextstates.append("q0") 
                    nextstates.append("q2")

                elif state == "q2":
                    nextstates.append("q3")
                
                elif state == "q3":
                    nextstates.append("q3")


        currstates = nextstates  
        path.append(currstates)
    
    if endstate in currstates:
        print("This is a valid string")
        print("Path Taken:")
        return(list(itertools.chain.from_iterable(path)))
      
    else:
        return "This is an invalid string"  

test = "bbb"

#accepts strings greater than 2
 

print(nfa(test))