triple_generation_examples = [
{
        "subject": "ethanol",
        "question": "What is the primary product of complete combustion of ethanol?",
        "answer": "Carbon Dioxide and Water",
        "response": '''
To extract a triple from the given question-answer (QA) pair:

Question: "What is the primary product of complete combustion of ethanol?"
Answer: "Carbon Dioxide and Water"

We can identify the following components for the triple:

Subject: Ethanol
Object: Carbon Dioxide and Water
Relation: Produces as primary product of complete combustion

Thus, the triple would be:
(ethanol, produces as primary product of complete combustion, Carbon Dioxide and Water)
This triple captures all essential information from the QA pair, linking "ethanol" through the process of "complete combustion" to the products "Carbon Dioxide and Water".

Output:\n
(ethanol, produces as primary product of complete combustion, Carbon Dioxide and Water)
'''
},
]

two_hop_question_generation_examples = [
    {
        "triples": "(insulin, is produced by the organ in the human body, pancreas), (pancreas, produce primary digestive enzyme, Amylase)",
        "answer": '''
Given the factual triples you've provided:

1. (insulin, is produced by the organ in the human body, pancreas)
2. (pancreas, produce primary digestive enzyme, Amylase)

A question asking about "E" (Amylase) from "A" (insulin), without mentioning "C" (pancreas) and "E" (Amylase), using "B" (is produced by the organ in the human body) and "D" (produce primary digestive enzyme) would be:\n
Which primary digestive enzyme is produced by the same organ in the human body that also produces insulin?
'''},
]

rewrite_examples = [
#     {
#         "triples": "(USA, president, Biden)",
#         "subject": "USA",
#         "answer": '''
# (USA, president, Trump)'''},
]
