from groq_call import call_llama, call_gpt

def battle(prompt):
    response_a = call_gpt(prompt)
    response_b = call_llama(prompt)
    return response_a, response_b