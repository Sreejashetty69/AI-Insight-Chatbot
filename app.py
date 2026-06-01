from flask import Flask, request, jsonify, render_template_string
from pyngrok import ngrok
from threading import Thread

app = Flask(__name__)

responses = {

    "hello": "Hi! How can I help you today?",
    "hi": "Hello! Welcome to AI Chatbot.",
    "how are you": "I am doing great. Thanks for asking!",

    "what is ai": "Artificial Intelligence enables machines to perform tasks that normally require human intelligence.",

    "what is generative ai": "Generative AI is a type of AI that can create new content such as text, images, code, audio, and videos.",

    "what is gen ai": "Generative AI is a type of AI that can create new content such as text, images, code, audio, and videos.",

    "what is machine learning": "Machine Learning is a branch of AI that allows systems to learn from data.",

    "what is deep learning": "Deep Learning is a subset of Machine Learning based on neural networks.",

    "what is llm": "LLM stands for Large Language Model. It is an AI model trained on massive amounts of text data to understand and generate human-like language.",

    "what is prompt engineering": "Prompt Engineering is the process of designing effective prompts to get accurate and useful responses from AI models.",

    "what is rag": "RAG stands for Retrieval-Augmented Generation. It combines information retrieval with language generation to provide more accurate and up-to-date responses.",

    "what is python": "Python is a popular programming language used in web development, AI, and automation.",

    "what is flask": "Flask is a lightweight Python web framework used to build web applications.",

    "what is html": "HTML is the standard language used to create web pages.",

    "what is css": "CSS is used to style and design web pages.",

    "what is javascript": "JavaScript makes web pages interactive and dynamic.",

    "what is database": "A database is an organized collection of data that can be stored and accessed electronically.",

    "what is sql": "SQL is a language used to manage and query databases.",

    "what is cloud computing": "Cloud Computing provides computing services such as storage and servers over the internet.",

    "what is aws": "AWS stands for Amazon Web Services, a leading cloud computing platform.",

    "what is data science": "Data Science combines statistics, programming, and domain knowledge to analyze data.",

    "bye": "Goodbye! Have a great day."
}

html = """
<!DOCTYPE html>
<html>
<head>
<title>AI Chatbot</title>

<style>

*{
margin:0;
padding:0;
box-sizing:border-box;
font-family:'Segoe UI',sans-serif;
}

body{
height:100vh;
background:linear-gradient(135deg,#667eea,#764ba2);
display:flex;
justify-content:center;
align-items:center;
}

.container{
width:850px;
height:650px;
background:white;
border-radius:20px;
overflow:hidden;
box-shadow:0 10px 30px rgba(0,0,0,0.3);
}

.header{
background:#4f46e5;
color:white;
padding:20px;
text-align:center;
}

.header h1{
font-size:32px;
}

.header p{
margin-top:5px;
font-size:14px;
}

#chat-box{
height:500px;
overflow-y:auto;
padding:20px;
background:#f8fafc;
}

.user{
text-align:right;
margin:15px 0;
}

.bot{
text-align:left;
margin:15px 0;
}

.user span{
display:inline-block;
background:#4f46e5;
color:white;
padding:12px 16px;
border-radius:20px 20px 0px 20px;
max-width:70%;
}

.bot span{
display:inline-block;
background:#e2e8f0;
color:#111827;
padding:12px 16px;
border-radius:20px 20px 20px 0px;
max-width:70%;
}

.input-area{
display:flex;
padding:15px;
border-top:1px solid #ddd;
background:white;
}

input{
flex:1;
padding:15px;
border:1px solid #ccc;
border-radius:12px;
font-size:16px;
outline:none;
}

button{
margin-left:10px;
padding:15px 25px;
background:#4f46e5;
color:white;
border:none;
border-radius:12px;
cursor:pointer;
font-size:16px;
}

button:hover{
background:#3730a3;
}

</style>

</head>

<body>

<div class="container">

<div class="header">
<h1>🤖 AI Chatbot</h1>
<p>Ask me about AI, Gen AI, ML, Deep Learning, LLM, RAG, Python, AWS and more</p>
</div>

<div id="chat-box">

<div class="bot">
<span>
👋 Welcome! I can answer questions about:
<br><br>
• AI<br>
• Generative AI<br>
• Machine Learning<br>
• Deep Learning<br>
• LLM<br>
• Prompt Engineering<br>
• RAG<br>
• Python<br>
• Flask<br>
• HTML<br>
• CSS<br>
• JavaScript<br>
• Database<br>
• SQL<br>
• Cloud Computing<br>
• AWS<br>
• Data Science
</span>
</div>

</div>

<div class="input-area">

<input
type="text"
id="message"
placeholder="Type your question..."
onkeypress="handleKey(event)"
>

<button onclick="sendMessage()">Send</button>

</div>

</div>

<script>

function handleKey(event){
if(event.key==="Enter"){
sendMessage();
}
}

function sendMessage(){

let msg=document.getElementById("message").value;

if(msg.trim()==""){
return;
}

fetch("/chat",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({
message:msg
})
})

.then(response=>response.json())

.then(data=>{

let chat=document.getElementById("chat-box");

chat.innerHTML +=
"<div class='user'><span>👤 " + msg + "</span></div>";

chat.innerHTML +=
"<div class='bot'><span>🤖 " + data.response + "</span></div>";

document.getElementById("message").value="";

chat.scrollTop=chat.scrollHeight;

});

}

</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html)

@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json["message"].lower().strip()

    response = responses.get(
        user_message,
        "🤖 Sorry, I don't have information about that topic. Try asking about AI, Gen AI, Machine Learning, Deep Learning, LLM, Prompt Engineering, RAG, Python, Flask, AWS, SQL, HTML, CSS, JavaScript, Cloud Computing or Data Science."
    )

    return jsonify({"response": response})

public_url = ngrok.connect(5000)

print("\\n===================================")
print("OPEN THIS URL IN YOUR BROWSER")
print(public_url)
print("===================================\\n")

def run():
    app.run(host="0.0.0.0", port=5000)

Thread(target=run).start()
