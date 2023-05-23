# Prompt: Can you write some example tests for the hangman you gave me earlier?
# Test 1: Correct Guesses
word = "hangman"
max_guesses = 6
hangman(word, max_guesses)
# Expected Output:
# Let's play Hangman!
# _ _ _ _ _ _ _
# Enter a letter: h
# Correct guess!
# h _ _ _ _ _ _
# Enter a letter: a
# Correct guess!
# h a _ _ _ a _
# Enter a letter: n
# Correct guess!
# h a n _ _ a _
# Enter a letter: g
# Correct guess!
# h a n g _ a _
# Enter a letter: m
# Correct guess!
# h a n g m a _
# Enter a letter: n
# You already guessed that letter.
# h a n g m a _
# Enter a letter: o
# Incorrect guess! You have 5 tries left.
#  _______
# |      |
# |      O
# |     \\|/
# |      |
# |     / \\
# -
# h a n g m a _
# Enter a letter: z
# Incorrect guess! You have 4 tries left.
#  _______
# |      |
# |      O
# |     \\|/
# |      |
# |     / 
# -
# h a n g m a _
# Enter a letter: n
# You already guessed that letter.
# h a n g m a _
# Enter a letter: t
# Incorrect guess! You have 3 tries left.
#  _______
# |      |
# |      O
# |     \\|/
# |      |
# |     
# -
# h a n g m a _
# Enter a letter: i
# Correct guess!
# h a n g m a _
# Enter a letter: r
# Incorrect guess! You have 2 tries left.
#  _______
# |      |
# |      O
# |     \\|/
# |      |
# |     
# -
# h a n g m a _
# Enter a letter: v
# Incorrect guess! You have 1 tries left.
#  _______
# |      |
# |      O
# |     \\|/
# |      |
# |     
# -
# h a n g m a _
# Enter a letter: z
# Incorrect guess! You have 0 tries left.
#  _______
# |      |
# |      O
# |     \\|/
# |      |
# |     
# -
# Game over! The word was: hangman
#  _______
# |      |
# |
# |
# |
# |
# -

# Test 2: Incorrect Guesses
word = "hello"
max_guesses = 4
hangman(word, max_guesses)
# Expected Output:
# Let's play Hangman!
# _ _ _ _ _
# Enter a letter: a
# Incorrect guess! You have 3 tries left.
#  _______
# |      |
# |      O
# |     \\|/
# |      |
# |     
# -
# _ _ _ _ _
# Enter a letter: b
# Incorrect guess! You have 2 tries left.
#  _______
# |      |
# |      O
# |     \\|/
# |      |
# |     
# -
# _ _ _ _ _
# Enter a letter: c
# Incorrect guess! You have 1 tries left.
#  _______
# |      |
# |      O
# |     \\|/
# |      |
# |     
# -
# _ _ _ _ _
# Enter a letter: d
# Incorrect guess! You have 0 tries left.
#  _______
# |      |
# |      O
# |     \\|/
# |      |
# |     
# -
# Game over! The word was: hello
#  _______
# |      |
# |
# |
# |
# |
# -


# Test 3: Winning the Game
word = "python"
max_guesses = 6
hangman(word, max_guesses)
# Expected Output:
# Let's play Hangman!
# _ _ _ _ _ _
# Enter a letter: p
# Correct guess!
# p _ _ _ _ _
# Enter a letter: y
# Correct guess!
# p y _ _ _ _
# Enter a letter: t
# Correct guess!
# p y t _ _ _
# Enter a letter: h
# Correct guess!
# p y t h _ _
# Enter a letter: o
# Correct guess!
# p y t h o _
# Enter a letter: n
# Correct guess!
# p y t h o n
# Congratulations! You won!

