

import openai


def opposite(content):
    prefix = "Summarize the opposite of this:\n\n"
    prompt = prefix + content
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=64,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    text = ""
    if response.choices:
        text = response.choices[0].text
    return text

def summarize(content):
    suffix = "\n\nTl;dr"
    prompt = content + suffix
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=1
    )
    text = ""
    if response.choices:
        text = response.choices[0].text
    return text

def analogy(content):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"""
        Create an analogy for this phrase:
        
        {content}
        """,
        temperature=0.5,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    text = ""
    if response.choices:
        text = response.choices[0].text
    return text