# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

Attempts: You are allowed double the number of attempts communicated. I expected the game to end once I reached the required limit but instead it only ended when I reached double the limit. 
Hints: The hints communicated opposite instructions in regards to the answer and submitted guess. For example answer: 59, guess: 56. In this scenerio I expected the hint to say go higher but instead I recieved the message to go lower. Similarly, with answer: 59, guess:60, I expected the hint to be go lower but instead I recieved the message to go higher.
Hints: The toggle button only works before each new guess. You can't toggle the hint on and off freely anytime.
'New Game' Button: I expect when I press New Game to be able to submit guesses again for this new game, however, I was not able to. This button only works while you are still in the middle of a game/have not used all your attempts and/or won the game.
Range: If I am on a specific level that specifies a range of 1 to 50, I expect that the answer will be in that range, however, that was not the case. Answers where generated that were greater than 50.
Range: The main page description of the game remains the same no matter what selected level I am on. For example the main page description remains Guess a number between 1 and 100 despite being on level Hard where the description in the side bar is Guess a number between 1 and 50. 

---

## 2. How did you use AI as a teammate?

I used Claude Code on this project.
An AI example that was correct was the location of the hard coded info box difficulty range display. I suggested to look at line 48. I verified this by reviwing that line 48 to see low, high previously stored from line 25: low, high = get_range_for_difficulty(difficulty) was not used. 
An AI example that was incorrect was testing this very bug. At first it suggested testing get_range_for_difficulty soley but that is not where the issue lies. get_range_for_difficulty worked, the info box displaying get_range_for_difficulty didn't. I verified this was incorrect by reviewing the intial bug to compare if this test covered the code in full.

---

## 3. Debugging and testing your fixes

I decided a bug was fixed if it passed a test I created and when I run the app, the feature is working as expected.
I ran def test_guess_too_high() using pytest. It tested if secret is 50 and guess is 60, hint should be "Too High". It showed me that my code is now working as expected where it correctly hints the direction a user should go. Previously the was inverted stating "Too Low".
AI helped my refactor this test since it was failing due to str vs tuple expection error. AI communicated how to resolve this issue. 

---

## 4. What did you learn about Streamlit and state?

The secret number kept changing in the app because with random.randint, it would generate a random number for that session. 
To explain reruns and session state I would communicate that when an action is made the backend is rerun like a webpage is refreshed. A state saves the variable so it isnt reset in a rerun. 
For me the secret number was always stable as it used session state. 

---

## 5. Looking ahead: your developer habits
One habit from this project that I want to reuse in the future is standardized commit messages and testing!
One thing I would do differently in working with AI is to ask for it to explain how a test will work in detail before providing a code snippet. 
This project changed the way I think about AI generated code because it showed me how often a solution may be overcomplicated out outside of scope/issue at hand.
