# Prompt: Could you cover more edge cases please?
# Test 1: Word with Spaces
word = "hangman game"
max_guesses = 6
hangman(word, max_guesses)
# Expected Output:
# Let's play Hangman!
# _ _ _ _ _ _  _
# Enter a letter: h
# Correct guess!
# h _ _ _ _ _  _
# Enter a letter: a
# Incorrect guess! You have 5 tries left.
#  _______
# |      |
# |      O
# |     \\|/
# |      |
# |     / \\
# -
# h _ _ _ _ _  _
# Enter a letter: n
# Correct guess!
# h a n _ _ _  _
# Enter a letter: g
# Correct guess!
# h a n g _ _ _  _
# Enter a letter: m
# Correct guess!
# h a n g m _ _  _
# Enter a letter: e
# Correct guess!
# h a n g m a _  _
# Enter a letter: g
# You already guessed that letter.
# h a n g m a _  _
# Enter a letter: s
# Incorrect guess! You have 4 tries left.
#  _______
# |      |
# |      O
# |     \\|/
# |      |
# |     
# -
# h a n g m a _  _
# Enter a letter: z
# Incorrect guess! You have 3 tries left.
#  _______
# |      |
# |      O
# |     \\|/
# |      |
# |     
# -
# h a n g m a _  _
# Enter a letter: i
# Correct guess!
# h a n g m a i  _
# Enter a letter: r
# Incorrect guess! You have 2 tries left.
#  _______
# |      |
# |      O
# |     \\|/
# |      |
# |     
# -
# h a n g m a i  _
# Enter a letter: v
# Incorrect guess! You have 1 tries left.
#  _______
# |      |
# |      O
# |     \\|/
# |      |
# |     
# -
# h a n g m a i  _
# Enter a letter: z
# Incorrect guess! You have 0 tries left.
#  _______
# |      |
# |      O
# |     \\|/
# |      |
# |     
# -
# Game over! The word was: hangman game
#  _______
# |      |
# |
# |
# |
# |
# -

# Test 2: Word with Repeating Letters
word = "banana"
max_guesses = 6
hangman(word, max_guesses)
# Expected Output:
# Let's play Hangman!
# _ _ _ _ _ _
# Enter a letter: a
# Correct guess!
# _ a _ a _ a
# Enter a letter: n
# Correct guess!
# n a n a _ a
# Enter a letter: b
# Correct guess!
# n a n a b a
# Enter a letter: c
# Incorrect guess! You have 5 tries left.
#  _______
# |      |
# |      O
# |     \\|/
# |      |
# |     / \\
# -
# n a n a b a
# Enter a letter: x
# Incorrect guess! You have 4 tries left.
#  _______
# |      |
# |      O
#
