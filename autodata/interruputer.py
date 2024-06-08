from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from .prompt import rewrite_examples

model1 = ChatOpenAI(openai_api_key="your-api-key", model="gpt-4-turbo")

rewrite_prompt = PromptTemplate(
    input_variables=["triple", "subject", "relation", "response"], template='''
You are an expert in knowledge graphs. A triple is in the form of (subject, relation, answer).
Given a fact triple {triple}.
You should evaluate whether there are a new_subject which can also perfectly match the relation """{relation}""".
If not, output false and stop generation.
If there are, you should construct a new triple consisting of (new subject, """{relation}""", new answer) with the relation unchanged.
Specifically, you should use a new subject new_subject, which also has the property stated in the relation "{relation}", to replace "{subject}".
The relation must not be altered.
The new answer must be rigorously correct.
{response}''',
)

class Interrupter:
    def __init__(self, triple, subject, relation):
        self.triple = triple
        self.subject = subject
        self.relation = relation

    def interrupt(self):
        prompt = FewShotPromptTemplate(
            examples=rewrite_examples,
            example_prompt=rewrite_prompt,
            suffix='''
    You are an expert in knowledge graphs. A triple is in the form of (subject, relation, answer).
    Given a fact triple {triple}.
    You should evaluate whether there are a new_subject which can also perfectly match the relation """{relation}""".
    If not, output false and stop generation.
    If there are, you should construct a new triple consisting of (new subject, """{relation}""", new answer) with the relation unchanged.
    Specifically, you should use a new subject new_subject, which also has the property stated in the relation "{relation}", to replace "{subject}".
    The relation must not be altered.
    The new answer must be rigorously correct.''',
            input_variables=["triple"],
        )
        chain = prompt | model1 | StrOutputParser()

        return chain.invoke({"triple": self.triple, "subject": self.subject, "relation": self.relation})

# if __name__ == "__main__":
#     interrupter = Interrupter("(USA, president, Biden)", "USA", "president")
#     print(interrupter.interrupt())
