from openai import OpenAI
client = OpenAI(api_key="")

response = client.chat.completions.create(
  model="gpt-4.1",
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "hello what is a monkey"
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "A monkey is a primate in the simian group that is not an ape. They’re intelligent, mostly social mammals found in tropical forests, savannas, and mountains.\n\nKey points:\n- Classification: Two main groups\n  - New World monkeys (Americas): e.g., capuchins, howler and spider monkeys; often have prehensile (grasping) tails; nostrils face sideways.\n  - Old World monkeys (Africa/Asia): e.g., macaques, baboons, colobus; tails are not prehensile; nostrils face downward; some have cheek"
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Continue from the last token without repeating"
        }
      ]
    },
  ],
  response_format={
    "type": "text"
  },
  verbosity="medium",
)

print(response.choices[0].message.content)


# sample response 

# Monkeys are generally smaller than apes and often possess tails (though not all species do). They are highly social, living in groups known as troops or bands, and exhibit a range of behaviors including grooming, vocal communication, and playing. Their diet is usually omnivorous, consisting of fruits, leaves, insects, and sometimes small animals. Monkeys are widely studied in biology and psychology due to their intelligence and similarities to humans.