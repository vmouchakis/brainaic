from langchain import PromptTemplate


TEMPLATE = """
Use the following pieces of context to answer the users question.
If you don't know the answer, just say that you don't know, don't try to make up an answer.

{question}
"""

PROMPT = PromptTemplate(
    template=TEMPLATE,
    input_variables=["question"]
)
