from autodata import SubjectGenerator, QA_Generator, TripleExtractor, Interrupter, TwoHopQuestionGenerator
# sk-proj-nKP9Oa4IjMdT80dnT4N3T3BlbkFJCTDePQs5s2dqeW5lyC8B

def subject_generation(field, thing, subject_number):
    subject_generator = SubjectGenerator(field, thing, subject_number)

    return subject_generator.generate()

def QA_generation(subject, question_type):
    qa_generator = QA_Generator(subject, question_type)

    return qa_generator.generate()

def triple_extraction(subject, question, answer):
    triple_extractor = TripleExtractor(subject, question, answer)

    return triple_extractor.extract()

def interrupt(triple, subject, relation):
    interrupter = Interrupter(triple, subject, relation)

    return interrupter.interrupt()

def two_hop_question_generation(firstTriple, secondTriple):
    two_hop_question_generator = TwoHopQuestionGenerator(firstTriple, secondTriple)

    return two_hop_question_generator.generate()

def return_element(triple, index):
    # Remove the parentheses from the string
    clean_string = triple.strip('()')

    # Split the string into a list of elements
    elements = clean_string.split(',')

    return elements[index] 

def main(first_subject, question_type):
    first_QA = QA_generation(first_subject, question_type)
    first_question = first_QA["question"]
    first_answer = first_QA["answer"]
    first_triple = triple_extraction(first_subject, first_question, first_answer)
    first_relation = return_element(first_triple, 1)

    second_QA = QA_generation(first_answer)
    second_question = second_QA["question"]
    second_answer = second_QA["answer"]
    second_triple = triple_extraction(first_answer, second_question, second_answer).split("\n")[-1]
    second_relation = return_element(second_triple, 1)

    interrupted_triple = interrupt(second_triple, first_answer, second_relation).split("\n")[-1]
    single_hop_target_new = return_element(interrupted_triple, 0)
    two_hop_target_new = return_element(interrupted_triple, 2)

    two_hop_question = two_hop_question_generation(first_triple, second_triple)

    return {"single_hop_prompt": first_question, "entity": first_subject, "relation": first_relation, "two_hop_question": two_hop_question, 
            "target_true": {"single_hop_target_true": first_answer, "two_hop_target_true": second_answer},
            "target_new": {"single_hop_target_new":  single_hop_target_new, "two_hop_target_new": two_hop_target_new}}

    

if __name__ == "__main__":
    field = "history" # replace this with the field of knowledge, e.g. "history", "biology"
    thing = "events" # replace this with the type of subjects, e.g. "events", "chemical compounds"
    subject_number = 1 # replace this with the number of subjects to generate
    question_type = "replace this with the type of question" # e.g. "scientific"

    first_subjects = subject_generation(field, thing, subject_number)
    for first_subject in first_subjects:
        print(main(first_subject, question_type))
