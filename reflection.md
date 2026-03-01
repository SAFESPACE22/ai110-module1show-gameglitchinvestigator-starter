# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it? It did not really look like a game. For some reason the game contained the Developer Debug Info. The Game was dark and the attempts were a bit off.
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  When finishing a game I could not start a new game. The hints were backwards, they kept suggesting lower when the number was actually higher.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? I used copilot during this project
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
The odd behaviour with alternating string/int secrets is the “glitch” the app’s title refers to – every second guess the secret is temporarily stringified, so they need the try/except to avoid a crash and still provide feedback.
  Secret is prepared as string for event and odd it stay and int.
   secret = str(st.session_state.secret)
        else:
            secret = st.session_state.secret

I used AI to identify what part of the code it was talking about and validated the code.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
I prompted AI to tell me all the issues within the code and it failed to miss one of the issues I noticed. From a logical standpoint the allowed attempts should decrease with each difficulty, however, this was never mentioned through the AI.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decided the bug was fixed when the issue in the GUI was resolved.
- Describe at least one test you ran (manual or using pytest)  
I used pytest to test my function. In pytest I tested the hinting error to validate its responses.
- Did AI help you design or understand any tests? How? Yes AI helped me design and understand the test of my function it called the function then tested each edge case to the function.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app. The secret kept changing in the original app becasue the data type flipped for every other turn. The even numbers turned into strings while the odd numbers remain integers.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  Streamlit works by executing the entire script from top to bottom every time the user interacts with the UI. Session state stashes the users value and prevents the app from continuosly refreshing everytime.
- What change did you make that finally gave the game a stable secret number?
  The issue was caused by converting the secret to a string on every even numbered guess. I removed that type flip so the secret is always stored and compared as an integer, along with that the game respect the difficulty of the game mode which stopped the “changing number” glitch and kept the secret stable.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
One habit I found useful that I will integrate into my workflow is using AI to help me create test cases for a function if I dont clearly understand the function very well. AI can help me create test cases and identify every edge case.
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  This was a testing habit.
- What is one thing you would do differently next time you work with AI on a coding task?
I could ask AI to break down its thinking process, so I can understand its decision process.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
AI generated code can be beneficial most of the time but the moment you lose a grasp of what is going on with the code changes it can be a real big headache. Understanding before making any changes to the codebase is so crucial to development.