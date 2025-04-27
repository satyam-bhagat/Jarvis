# # # # import OpenAI from "openai";
# # # # const client = new OpenAI();

# # # # const response = await client.responses.create({
# # # #     model: "gpt-4.1",
# # # #     input: "Write a one-sentence bedtime story about a unicorn.",
# # # # });

# # # # console.log(response.output_text);

# # # from openai import OpenAI
# # # client=OpenAI(
# # #     apikey="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",

# # #     completion = .chat.completions.create(
# # #   model="gpt-4o-mini",
# # #   store=True,
# # #   messages=[
# # #     {"role": "user", "content": "write a haiku about ai"}
# # #   ]
# # # )

# # # )



# # # from openai import OpenAI

# # # client = OpenAI(
# # #   api_key="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"
# # # )

# # # completion = client.chat.completions.create(
# # #   model="gpt-4o-mini",
# # #   store=True,
# # #   messages=[
# # #     {"role": "system", "content": "concepts of programming"}
# # #   ]
# # # )

# # # print(completion.choices[0].message.content);



# # from openai import OpenAI

# # client = OpenAI(
# #     api_key="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"  # ⚡ Replace with your real API key
# # )

# # completion = client.chat.completions.create(
# #     model="gpt-4o",  # Correct model name
# #     messages=[
# #         {"role": "system", "content": "You are a helpful assistant."},
# #         {"role": "user", "content": "Explain Python programming in simple words."}
# #     ]
# # )

# # print(completion.choices[0].message.content)



# from openai import OpenAI
# from openai import RateLimitError

# client = OpenAI(
#     api_key=
#     "  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" 
#       # ⚡ Replace with your real API key
#  # Keep your key secret
# )

# try:
#     completion = client.chat.completions.create(
#         model="gpt-4o",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": "Explain Python programming in simple words."}
#         ]
#     )
#     print(completion.choices[0].message.content)

# except RateLimitError as e:
#     print("Error: Rate limit exceeded. Please check your usage and billing details.")
# except Exception as e:
#     print(f"An error occurred: {e}")

# from together import Together
# client = Together()

# completion = client.chat.completions.create(
#   model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
#   messages=[{"role": "user", "content": "What are the top 3 things to do in New York?"}],
# )

# print(completion.choices[0].message.content)


