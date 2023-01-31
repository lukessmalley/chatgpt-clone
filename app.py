import os
import openai
import gradio as gr

#if you have OpenAI API key as an environment variable, enable the below
#openai.api_key = os.getenv("OPENAI_API_KEY")

#if you have OpenAI API key as a string, enable the below
openai.api_key = ""

#start_sequence = "\nEugene:"
#restart_sequence = "\nStudent: "

prompt = "Summarize this for a second-grade student:\n\nJupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. Jupiter is one of the brightest objects visible to the naked eye in the night sky, and has been known to ancient civilizations since before recorded history. It is named after the Roman god Jupiter.[19] When viewed from Earth, Jupiter can be bright enough for its reflected light to cast visible shadows,[20] and is on average the third-brightest natural object in the night sky after the Moon and Venus."


def openai_create(prompt):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    return response.choices[0].text



def chatgpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, history


block = gr.Blocks()


with block:
    gr.Markdown("""<h1><center>Hello, I'm Eugene!</center></h1>
    """)
    chatbot = gr.Chatbot(label='Eugene',show_label=True) # get the chatbot
    message = gr.Textbox(label='Type your message here:',placeholder=prompt) # input textbox where we can type, includes a placeholder for the initial prompt.
    state = gr.State()
    submit = gr.Button("SEND") # the send button
    submit.click(chatgpt_clone, inputs=[message, state], outputs=[chatbot, state]) # when the button is clicked we call the function with the given inputs and outputs.

block.launch(debug = True
            #,share=True
            )
