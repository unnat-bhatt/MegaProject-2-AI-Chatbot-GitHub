from openai import OpenAI
client = OpenAI(
    api_key = "Your_OpenAiapikey"
)

command='''
[11:14 pm, 2/6/2025] vinit bhatt: hellow
[11:14 pm, 2/6/2025] vinit bhatt: see this website
[11:14 pm, 2/6/2025] vinit bhatt: https://www.youtube.com/
[11:14 pm, 2/6/2025] Vinit New Real Estate Lucknow: yeah
[11:14 pm, 2/6/2025] Vinit New Real Estate Lucknow: I see it
[11:15 pm, 2/6/2025] vinit bhatt: i am good and fine
[11:15 pm, 2/6/2025] vinit bhatt: how are you?
[11:16 pm, 2/6/2025] Vinit New Real Estate Lucknow: i am also very well 
thankyou
[11:17 pm, 2/6/2025] Vinit New Real Estate Lucknow: do you like to run ?
[11:17 pm, 2/6/2025] vinit bhatt: yes i do , running sweats alot
'''

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "system", "content":"You are a person named kaka who speaks hindi as well as english. He is form India and is a coder. You analyze chat history and respond like kaka"},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message.content)
