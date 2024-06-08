from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from prompt import triple_generation_examples

model2 = ChatOpenAI(openai_api_key="your-api-key", model="gpt-3.5-turbo")

triple_generation_prompt = PromptTemplate(
        input_variables=["subject", "question", "answer", "response"], template='''
    You are an expert in knowledge graphs.
    Given a QA pair:\n
    Question: {question} 
    Answer: {answer}\n
    You should extract a triple consisting of ("""{subject}""", relation, """{answer}""") from the QA pair..
    The relation must include any other information, except "{subject}" and "{answer}", in the QA pair.
    Output the extracted triple at last.
    {response}''',
    )

class TripleExtractor:
    def __init__(self, subject, question, answer):
        self.subject = subject
        self.question = question
        self.answer = answer

    def extract(self):
        prompt = FewShotPromptTemplate(
            examples=triple_generation_examples,
            example_prompt=triple_generation_prompt,
            suffix='''
    You are an expert in knowledge graphs.
    Given a QA pair:\n
    Question: {question} 
    Answer: {answer}\n
    You should extract a triple consisting of ("""{subject}""", relation, """{answer}""") from the QA pair.
    The relation must include any other information except the "{subject}" and the "{answer}" in the QA pair.
    Output the extracted triple at last.''',
            input_variables=["subject", "question", "answer"],
        )
        chain = prompt | model2 | StrOutputParser()

        return chain.invoke({"subject": self.subject, "question": self.question,"answer": self.answer})
    
# if __name__ == "__main__":
#     {'question': 'What is the primary industrial source for synthesizing benzene?', 'answer': 'Crude oil'}
#     triple_extractor = TripleExtractor("Benzene", "What is the primary industrial source for synthesizing benzene?", "Crude oil")
#     print(triple_extractor.extract())




