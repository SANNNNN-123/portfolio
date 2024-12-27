from flask import Flask, render_template, url_for
from datetime import datetime

app = Flask(__name__)

@app.route('/projects')
def project_directory():

    projects = {
        "2024": [
            {
                "id": "001",
                "name": "Football-Analysis",
                "tech": "OpenCV,YoloV8",
                "image": url_for('static', filename='images/football.png'),
                "description": "An AI-powered football analysis tool using computer vision to track player movements and analyze game strategies."
            },
            {
                "id": "002",
                "name": "DamageTracker-Genshin",
                "tech": "NN, DigitRecognizer",
                "image": "https://placeholder.com/300x200",
                "description": "A neural network-based damage tracker for the game Genshin Impact, using digit recognition to automatically log and analyze player damage output."
            },
            {
                "id": "003",
                "name": "TikTOK-Analytics Tool",
                "tech": "Playwright,Flask",
                "image": "https://placeholder.com/300x200",
                "description": "A web scraping and analytics tool for TikTok, providing insights into trending content and user engagement patterns."
            },
            {
                "id": "004",
                "name": "MedicalChat-Gen AI",
                "tech": "Pinecone,LangChain",
                "image": "https://placeholder.com/300x200",
                "description": "An AI-powered medical chatbot using advanced language models to provide accurate and helpful medical information to users."
            },
            {
                "id": "005",
                "name": "YoutubeSummarize-AIagents",
                "tech": "CrewAI, AgentOps",
                "image": "https://placeholder.com/300x200",
                "description": "An AI-driven YouTube video summarization tool that uses multiple AI agents to generate concise and accurate summaries of long-form content."
            }
        ]
    }
    return render_template('projects.html', projects=projects)


@app.route('/')
def index():
    current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return render_template('index.html', current_time=current_time)

if __name__ == '__main__':
    app.run(debug=True)

