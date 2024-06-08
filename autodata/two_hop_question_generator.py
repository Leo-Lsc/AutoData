from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from prompt import two_hop_question_generation_examples

model1 = ChatOpenAI(openai_api_key="your-api-key", model="gpt-4-turbo")

two_hop_question_generation_prompt = PromptTemplate(
    input_variables=["triples", "answer"], template='''
You are a powerful multi-hop question generator. Users will provide 2 factual triples in the form of (A, B, C), (C, D, E).
and you will help write a question to ask E from A. You must not include C and E in the generated question; B and D must all be used in the generated question.
Given 2 factual triples {triples}, write a question to ask E. Don't mention C and E.\n{answer}''',
)

class TwoHopQuestionGenerator:
    def __init__(self, firstTriple, secondTriple):
        self.firstTriple = firstTriple
        self.secondTriple = secondTriple
        self.instance = f"{firstTriple}, {secondTriple}"

    def generate(self):
        prompt = FewShotPromptTemplate(
            examples=two_hop_question_generation_examples,
            example_prompt=two_hop_question_generation_prompt,
            suffix='''
    You are a powerful multi-hop question generator. Users will provide 2 factual triples in the form of (A, B, C), (C, D, E).
    and you will help write a question to ask E from A. You must not include C and E in the generated question; B and D must all be used in the generated question.
    Given 2 factual triples {instance}, write a question to ask E. Don't mention C and E.''',
        input_variables=["instance"],
    )
        chain = prompt | model1 | StrOutputParser()

        return chain.invoke({"instance": self.instance})

# if __name__ == "__main__":
#     two_hop_question_generator = TwoHopQuestionGenerator("(Benzene, Common product made by hydrogenating, Cyclohexane)", "(Cyclohexane, exhibits as primary molecular shape at room temperature, Chair conformation)")
#     print(two_hop_question_generator.generate())

