from hf_model import query_model

def planner_agent(user_query):
    prompt = f"""
    You are a planning agent.
    Break the question into structured numbered sections.

    Question: {user_query}

    Output format:
    1.
    2.
    3.
    """

    response = query_model(prompt)
    return response