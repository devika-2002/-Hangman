import random    
print ("Welcome to the game, Hangman!")
words=['study','start','learn','music','ready']
hangman_graphics=[
    '_',
    '__',
    '__\n |',
    '__\n |\n O',
    '__\n |\n O\n/|',
    '__\n |\n O\n/|\ ',
    '__\n |\n O\n/|\ \n/',
    '__\n |\n O\n/|\ \n/ \ '
]
number_mistakes=0
letters__guessed=[]
number_mistakes_allowed=len(hangman_graphics)
word=random.choice(words)
letters__word=list(word)
print()
print("The word letters:-",format(len(letters__word)))

while number_mistakes<number_mistakes_allowed:
  print()
  print("Guessed left:-",format(number_mistakes_allowed-number_mistakes))
  letter_user=input("Enter a letter:")
  while letter_user in letters__guessed :
    print()
    print("you have already entered this letter,enter another one ")
    letter_user=input("Enter a letter:-")
  if letter_user not in letters__word:
       number_mistakes+=1
  print()
  print("Word:-",end="")
  for letter in letters__word:
      if letter_user==letter:
          letters__guessed.append(letter_user)
  for letter in letters__word:
    if letter in letters__guessed:
        print(letter+' ',end='')
    else:
        print('_',end='')
  print()
  if number_mistakes:
    print(hangman_graphics[number_mistakes-1])
  print()
  print('------------------------')
  
  if len(letters__guessed)==len(letters__word):
    print()
    print('Congratulations, you won!')
    break

if number_mistakes==number_mistakes_allowed:
   print()
   print("sorry you loss the game try agan!")
   

   