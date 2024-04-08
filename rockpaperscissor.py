import random
rock = ('''        _....._
      .;;'      '-.
    .;;: _         '.
   /;;:'(_)          \
  |;;:'_     _        |
  |;;:(_)   (_)       |
  |;;::.              |
   \;;::.            /
    ';;::.         .'
      '-;;:..  _.-'
jgs       ''')

paper = ('''______ ______
    _/      Y      \_
   // ~~ ~~ | ~~ ~  \\
  // ~ ~ ~~ | ~~~ ~~ \\      
 //________.|.________\\ ''')


scissor = ('''
/\                    /\
\ \                  / /
 \ \                / /
  \.\              /./
   \.\            /./
    \.\          /./
     \\\        ///
      \.\      /./
       \.\    /./
        \.\__/./
       _/)))(((\_
       \|)\##/(|/
       _|)/##\(|_
       \|)))(((|/
        /o/  \o\
       /o/    \o\
      /_/      \_\ ''')
choice_u = input("What do you choose? Rock,Paper,Sciossor")
tools = ["rock", "paper", "scissor"]
choice_c = random.choice(tools)
print(choice_c)
if choice_u == 'rock' and choice_c == 'scissor':
    print("You win the game")
elif choice_u == 'paper' and choice_c == 'rock':
    print("You win the game")
elif choice_u == 'scissor' and choice_c == 'paper':
    print("You win the game")
elif choice_u == 'scissor' and choice_c == 'scissor':
    print("No one win.It's a tie")
elif choice_u == 'paper' and choice_c == 'paper':
    print("No one win.It's a tie")
elif choice_u == 'rock' and choice_c == 'rock':
    print("No one win.It's a tie")
else:
    print("Computer win the game")
