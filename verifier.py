from hf_model import query_model

def verifier_agent(answer, original_query):
    prompt = f"""
    Question: {original_query}
    Answer: {answer}

    Check if the answer is complete.
    Write PASS or FAIL at the end.
    """

    return query_model(prompt)