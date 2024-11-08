import random

positive_responses = ["*Yes*", "*Without a doubt*", "*Soon*"]
negative_responses = ["*No*", "*Probably not*"]
neutral_responses = ["*Maybe* 🤔", "*Could be... Could not to be...* 🤔", "*Perhaps* 🤔", "*You will find your answer soon enough* 🤔"]

def get_response(question):
    print(question.lower())
    question = question.lower()

    response = f"`{question}`\n\n**-~= "

    if "now" in question:
        response += random.choices(
            positive_responses + negative_responses,
        )[0]

    elif "hello there" == question:
        response += "Obi-Wan Kenobi 😉"

    else:
        response += random.choices(
            positive_responses + negative_responses + neutral_responses,
            weights=[2, 2, 1] * 3,
            k=1
        )[0]
    response += " =~-**"
    print(response)
    return(response)
