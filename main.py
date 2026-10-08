# yamn

from groq import Groq
# maher
client = Groq()
completion = client.chat.completions.create(
    model="qwen/qwen3.8-27b",
    messages=[
      {
        "role": "user",
        "content": ""
      }
    ],
    temperature=0.6,
    max_completion_tokens=2048,
    top_p=0.95,
    reasoning_effort="default",
    stream=True,
    stop=None
)
 # ai
# mimi max
for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
# first
# enter main page
# enter email or continue as quest


 #hi let's learn thing together 


#start tour



(print("start firs data page"))



#put first
# enter main page
# enter email or continue as quest
# in middle


# put continue button to sign or guest the color blue


#in the main page
#welcome to mini max AI


print("hi")

#in the AI but gallery but you have to sign in 




