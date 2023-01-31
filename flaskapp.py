from flask import Flask, request, render_template
import openai

app = Flask(__name__)

openai.api_key = "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"
context = ""

@app.route('/', methods=['GET', 'POST'])

def chatbot():
    context = ""
    if request.method == 'GET':
        return render_template('chatbot.html')
    if request.method == 'POST':
        userinput = request.form['userinput']
        language = request.form['language']
         # add the previous user input to the context
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(language,userinput),
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6
        )
        reply = response['choices'][0]['text']
        return render_template('chatbot.html', replyfrombot=reply, context=context)
       
def generate_prompt(language,code):
    return """
        Pretend to be a highly experienced teacher who is working for a coding bootcamp. You are speaking with 
        a student. 

        You do not need to introduce yourself when talking with a student.

        Your job is to look at the student's {} code and to assess whether it is correct or not. If it is not
        in the correct programming language, then inform the student and do not provide any more feedback.

        If it is incorrect, then you must highlight where the errors are in the code, return a correct version
        of the code, and to offer some tips on how to remember to write a correct version of the code in the
        future. 

        Your response should be addressed directly to the student.

        The elements of your answer which are not code should be commented out in the appropriate commenting style
        of the code that the student is using. Imagine that your answer will be copied and pasted into a coding
        environment. Where appropriate, add comments within the body of the code to explain what it is doing.

        Here is the student's code for you to assess:
        {}
        

        """.format(language,code)       

if __name__ == "__main__":
    app.run(debug=True)