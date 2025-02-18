from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/projects')
def project_directory():

    projects = {
        "2025": [
            {
                "id": "001",
                "name": "EYE_3Dmodel <span style='color: green;'>(ongoing)</span>",
                "tech": "ThreeJS,React,Vite",
                "description": "3D modelling for local ophtalmology clinic, using ThreeJS and React to create interactive 3D models of the eye for educational purposes."
            },
            {
                "id": "002",
                "name": "XLSX chatbot <span style='color: green;'>(ongoing)</span>",
                "tech": "Ai agents, FastAPI,React",
                "description": "Excel chatbot to perform data analysis and sql syntax"
            },
            {
                "id": "003",
                "name": "Resepi-GPT",
                "tech": "React,NextJS,OpenAI,Supabase",
                "description": "Resepi GPT is an AI-powered Malay recipe search engine that helps you find recipes based on ingredients you have"
            },
            {
                "id": "004",
                "name": "Stable Diffusion Puzzle",
                "tech": "HuggingFace, ControlNet, React",
                "description": "Generate a puzzle game using Stable Diffusion and ControlNet"
            }
        ],
        "2024": [
            {

                "id": "001",
                "name": "Football-Analysis",
                "tech": "OpenCV,YoloV8",
                "description": "An AI-powered football analysis tool using computer vision to track player movements and analyze game strategies."
            },
            {
                "id": "002",
                "name": "DamageTracker",
                "tech": "NN, DigitRecognizer",
                "description": "A neural network-based damage tracker for the game Genshin Impact, using digit recognition to automatically log and analyze player damage output."
            },
            {
                "id": "003",
                "name": "TikTOK-Analytics Tool",
                "tech": "Playwright,Flask",
                "description": "A web scraping and analytics tool for TikTok, providing insights into trending content and user engagement patterns."
            },
            {
                "id": "004",
                "name": "MedicalChat-Gen AI",
                "tech": "Pinecone,LangChain",
                "description": "An AI-powered medical chatbot using advanced language models to provide accurate and helpful medical information to users."
            },
            {
                "id": "005",
                "name": "YoutubeSummarize-AIagents",
                "tech": "CrewAI, AgentOps",
                "description": "An AI-driven YouTube video summarization tool that uses multiple AI agents to generate concise and accurate summaries of long-form content."
            },
            {
                "id": "006",
                "name": "Florence + SAM2",
                "tech": "Face Detection",
                "description": "Experimenting computer vision project to identify human faces in images, detect speakers and apply censorship to passerby faces"
            },
            {
                "id": "007",
                "name": "FruitNinja_ObjectDetection",
                "tech": "OpenCV,yolov4-tiny",
                "description": "Experimenting OpenCV and YoloV8 to detect and track fruits in a video game and added bot to play the game"
            }
            
        ]
    }
    return render_template('projects.html', projects=projects)


@app.route('/')
def index():
    current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return render_template('index.html', current_time=current_time)

if __name__ == '__main__':
    app.run(debug=False)
else:
    # This is needed for Vercel deployment
    app = app

