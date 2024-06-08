from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.output_parsers import CommaSeparatedListOutputParser

model2 = ChatOpenAI(openai_api_key="your-api-key", model="gpt-3.5-turbo")
subject_parser = CommaSeparatedListOutputParser()

class SubjectGenerator:
    def __init__(self, field, thing, subject_number):
        self.field = field
        self.thing = thing
        self.subject_number = subject_number

    def generate(self):
        prompt = PromptTemplate(
            template=
                "You are an expert in {field}."
                "Provide {subject_number} different {thing} in this field."
                "These {thing} should be extremely specific." 
                "Just output the name.\n{format_instructions}",
            input_variables=["field", "thing","subject_number"],
            partial_variables={"format_instructions": subject_parser.get_format_instructions()}
        )
        chain = prompt | model2 | subject_parser

        return chain.invoke({"field": self.field, "thing": self.thing, "subject_number": self.subject_number})

# if __name__ == "__main__":
#     subject_genrator = SubjectGenerator("history", "historical events", 1)
#     print(subject_genrator.generate())
