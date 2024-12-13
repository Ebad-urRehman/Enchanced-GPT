def date_formatted(date):
    return f"<p style='text-align: right;'>{date}</p>"

def heading_formatted(heading):
    return  f"<h1 style='text-align: center;'>{heading}</h1>"

styles = {'textAreaStyle' :  f"""
<style>
.stTextArea{{
        position: fixed;
        bottom: 0;
        z-index: 3;
        line-height: 9.6;
        padding-bottom: 9rem;
        caret-color: rgb(250, 250, 250);
        color: rgb(250, 250, 250);
        border:0px solid white;
        border-right: 2px solid #000
        padding: 0px;
        max-height: 100px;
        }}
            
    </style>
"""}

def user_guide1():
    return '''📑User Guide:\n
🌡🔼 Temperature  1 means more ⚛ Creativity(predict more) in responses\n
🌡⏬Temperature 0 means more 🎯 accuracy(accurate information) in responses\n
More number of tokens means larger prompts(questions) and responses(answers by bot)\n
You can also change role in sidebar 👈\n'''

def user_guide2():
    return """Custom Roles:\n
Storyteller Role:\n
Usage Example: "Switch to storyteller mode. Tell me a mystical adventure tale."\n
Teacher Role:\n
Usage Example: "Act as a teacher. Explain the theory of relativity in simple terms."\n
Usage Example: "Switch to programmer mode. Can you help me debug this Python code?"\n
"""

def chat_default_text():
    return f"""👋 Aslam u Alaikum!\n
🛑 I am Enhanced GPT\n
💻 Write a Text and get an Answer\n
🔈 Give a custom Role to Enhanced GPT to behave accordingly\n
🧾🔁 You can Found old responses in History tab\n
"""

