#llm brain


from langchain_openai import ChatOpenAI

# initialize llm as Agent
llm = ChatOpenAI(
    model='',
    temperature=0
)

# example
response = llm.invoke(
    'search the golden medal list of olympic in 2024 between U.S and China, ' \
    'then compare the number of medals between the two country'
)

print(response.content)
