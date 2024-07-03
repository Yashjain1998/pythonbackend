from transformers import pipeline

# Load pre-trained BERT model for question answering
nlp_model = pipeline("question-answering", model="deepset/roberta-base-squad2")

def interpret_query(query):
    context = "Provide context or corpus related to health queries here."
    result = nlp_model(question=query, context=context)
    return result['answer']
