from hf_model import query_model

def writer_agent(plan):
    prompt = f"""
    You are an academic writer.

    Write a COMPLETE and DETAILED explanation.

    Make sure you explain ALL sections from the outline below.

    Outline:
    {plan}
    """
    return query_model(prompt)