from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field

model1 = ChatOpenAI(openai_api_key="your-api-key", model="gpt-4-turbo")

class QA(BaseModel):
    question: str = Field(description="The question which has unique answer")
    answer: str = Field(description="The unique answer to the question")
QA_parser = JsonOutputParser(pydantic_object=QA)

class QA_Generator:
    def __init__(self, subject, question_type):
        self.subject = subject
        self.question_type = question_type # question_type describes the type of question to be generated, e.g. "scientific" and "political".

    def generate(self):
        prompt = PromptTemplate(
        input_variables=["subject", "question_type"], template='''
    You are a powerful generator of {question_type} questions and answers.
    You should use """{subject}""" as a part of the question (not the answer), to generate a {question_type} question and its unique answer.
    The answer to the question must be unique and should not be longer than three words.
    The relationship between the question's subject and its answer should not be an equivalence relation, such as "chemical formula" or "common name".
    {format_instructions}
    ''',
        partial_variables={"format_instructions": QA_parser.get_format_instructions()}
    )
        chain = prompt | model1 | QA_parser

        return chain.invoke({"subject": self.subject, "question_type": self.question_type})

# if __name__ == "__main__":
#     QA_genrator = QA_Generator("Benzene", "scientific")
#     print(QA_genrator.generate())
