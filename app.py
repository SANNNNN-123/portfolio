from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/projects')
def project_directory():

    projects = {
        "2025": [
            {
                "id": "001",
                "name": "EYE_3Dmodel",
                "tech": "ThreeJS,React,Vite",
                "description": "3D modelling for local ophtalmology clinic, using ThreeJS and React to create interactive 3D models of the eye for educational purposes."
            },
            {
                "id": "002",
                "name": "Anime Connections",
                "tech": "AI Agents",
                "description": "Developed a multi-agent system to create a puzzle game inspired by The New York Times' Connections, featuring three specialized agents: Puzzle-Creator, Puzzle-Editor, and Puzzle-Debate."
            },
            {
                "id": "003",
                "name": "Resepi-GPT",
                "tech": "React,NextJS,OpenAI,Supabase",
                "description": "Resepi GPT is an AI-powered Malay recipe search engine that helps you find recipes based on ingredients you have"
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
                "name": "DamageTracker-Genshin",
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

