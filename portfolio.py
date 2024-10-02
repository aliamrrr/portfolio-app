from flask import Flask, render_template_string, url_for
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    # Obtenir la date actuelle
    current_date = datetime.now().strftime("%A, %b %d")  # Format : Sunday, Sept 29

    # Code HTML avec styles pour le header, footer, tech bar, et nouvelle section "About Me"
    html_code = f'''
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Portfolio</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap');

            body {{
                font-family: 'Roboto', sans-serif;
                margin: 0;
                padding: 0;
                background-color: #fff;
                color: #000;
                position: relative;
            }}
            .header {{
                padding: 20px;
                display: flex;
                justify-content: space-between;
                align-items: center;
                background-color: #fff;
                position: relative;
                z-index: 2;
            }}
            .header-left {{
                color: #000;
                font-size: 18px;
                margin-left: 70px;
            }}
            .header-right {{
                display: flex;
                gap: 10px;
                font-size: 18px;
                color: #000;
                margin-right: 70px;
            }}
            .header-right a {{
                color: #000;
                text-decoration: none;
                transition: color 0.3s;
            }}
            .header-right a:hover {{
                color: #007BFF;
            }}
            .separator {{
                margin: 0 5px;
            }}
            .intro-image {{
                display: block;
                margin: 20px auto 10px 50px;
                max-width: 80%;
                height: auto;
            }}
            .date {{
                margin-right: 70px;
                font-size: 18px;
            }}
            .internship-info {{
                text-align: left;
                margin-top: -110px;
                margin-left: 105px;
                font-size: 20px;
                font-weight: 300;
            }}
            .internship-looking {{
                text-align: left;
                margin-top: 10px;
                margin-left: 105px;
                font-size: 20px;
                font-weight: 300;
            }}
            .link {{ 
                text-decoration: underline;
                color: #000;
            }}
            .link:hover {{
                color: #007BFF;
            }}
            .work-section {{
                background: white;
                padding: 40px;
                text-align: center;
                margin-top: 95px;
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 30px;
            }}
            .image-container {{
                display: flex;
                flex-direction: column;
                align-items: center;
            }}
            .image-container img {{
                width: 300px;
                height: 300px;
                border-radius: 0%;
            }}
            .description {{
                text-align: left;
                margin-top: 30px;
                font-size: 16px;
            }}
            .description .line1 {{
                font-size: 15px;
                font-weight: 600;
                color: gray;
                margin-bottom: 10px;
                margin-right:100px;
            }}
            .description .line2 {{
                font-size: 22px;
                font-weight: 900;
                margin-bottom: 15px;
                margin-right:10px;
            }}
            .description .line3 {{
                font-size: 16px;
                font-weight: normal;
                margin-right:10px;
            }}
            .tech-bar {{
                position: relative;
                height: 80px;
                background-color: white;
                overflow: hidden;
                margin-top: 150px;
            }}
            .tech-icons {{
                display: flex;
                position: absolute;
                animation: move 20s linear infinite;  /* Vitesse ajustée */
            }}
            .tech-icons img {{
                width: 50px;
                height: 50px;
                margin: 0 40px;  /* Espace entre les icônes */
            }}
            @keyframes move {{
                0% {{ transform: translateX(100%); }}  /* Début à droite */
                100% {{ transform: translateX(-100%); }}  /* Sortie à gauche */
            }}
            .about-section {{
                padding: 60px 100px;
                background-color: white;
                display: flex;
                flex-direction: column;
                margin-top:50px;
                align-items: flex-start;
                gap: 40px;
            }}
            .about-section h2 {{
                font-size: 36px;
                font-weight: bold;
                margin: 0;
            }}
            hr.divider {{
            border: none;           /* Supprime la bordure par défaut */
            height: 1px;           /* Définit la hauteur de la ligne */
            background-color: #ccc; /* Couleur de la ligne */
            width: 100%;            /* Largeur de la ligne */
            margin-left: auto;     /* Centre la ligne horizontalement */
            margin-right: auto;    /* Centre la ligne horizontalement */
            margin-top: 30px;      /* Espace au-dessus de la ligne */
            margin-bottom: 30px;   /* Espace en dessous de la ligne */
        }}
            .what-and-lists {{
                display: flex;
                width: 100%;
                gap: 50px;
            }}
            .what-i-do {{
                font-size: 40px;
                font-weight: 300;
                flex: 1;
                align-self: center;
                margin-top: -200px;
            }}
            .more {{
                font-size: 40px;
                font-weight: 300;
                flex: 1;
                align-self: center;
                margin-top: -300px;
            }}
            .more-about-me {{
                font-size: 20px;
                font-weight: 300;
                flex: 1;
                align-self: center;
                margin-top: 50px;
            }}
            .lists {{
                display: flex;
                gap: 50px;
            }}
            .list {{
                list-style: none;
                padding: 0;
                font-size: 20px;
                font-weight: 300;
            }}
            .list li {{
                margin-bottom: 10px;
                position: relative;
                padding-left: 20px;
            }}
            .list li::before {{
                content: "•";
                position: absolute;
                left: 0;
                color: #007BFF;
            }}
            .footer {{
                text-align: left;
                padding: 20px 100px;
                background-color: white;
            }}
            .footer p {{
                margin: 5px 0;
                font-size: 14px;  /* Petit texte */
            }}
            .footer .large-text {{
                font-size: 36px;  /* Très grand texte */
                margin: 20px 0;
            }}
            /* New styles for the contact form */
            .contact-form {{
                background-color: #f8f8f8;
                padding: 40px;
                margin-top: 10px;
                border-radius: 20px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }}
            .contact-form h2 {{
                margin-left:20px;
                font-size: 28px;
                margin-bottom: 20px;
                color: #333;
                padding:40px;
            }}
            .form-group {{
                margin-bottom: 20px;
            }}
            .form-group label {{
                display: block;
                margin-bottom: 5px;
                font-weight: bold;
                color: #555;
                margin-left:60px;
            }}
            .form-group input,
            .form-group textarea {{
                width: 70%;
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 4px;
                font-size: 16px;
                margin-left:60px;
            }}
            .form-group textarea {{
                height: 150px;
            }}
            .submit-btn {{
                background-color: #007BFF;
                color: white;
                border: none;
                padding: 12px 20px;
                font-size: 18px;
                border-radius: 4px;
                cursor: pointer;
                transition: background-color 0.3s;
                margin-left:60px;
            }}
            .submit-btn:hover {{
                background-color: #0056b3;
            }}
            .footer .linkedin-icon {{
                width: 20px;
                height: 20px;
                cursor: pointer;
            }}
            @media (max-width: 768px) {{
                .about-section {{
                    padding: 40px 20px;
                }}
                .what-and-lists {{
                    flex-direction: column;
                    gap: 20px;
                }}
                .what-i-do {{
                    font-size: 30px;
                }}
                .lists {{
                    flex-direction: column;
                    gap: 20px;
                }}
                .work-section {{
                    padding: 20px;
                }}
                .footer {{
                    padding: 20px;
                }}
            }}
        </style>
    </head>
    <body>

        <div class="header">
            <div class="header-left">Amradouch Ali Anass</div>
            <div class="header-right">
                <a href="#work">Work</a>
                <span class="separator">|</span>
                <a href="https://drive.google.com/file/d/1bGwK0IjBfG8eKYlGkNTpQCjyz6No6oTP/view?usp=drive_link" target="_blank" rel="noopener noreferrer">Resume</a>
                <span class="separator">|</span>
                <a href="#about">About</a>
            </div>
            <div class="header-left date">{current_date}</div>
        </div>

        <img src="{url_for('static', filename='intro.png')}" alt="Introduction Image" class="intro-image"/>

        <div class="internship-info">
            Previously @<a href="https://www.atos.net" class="link"> Atos</a> Intern
        </div>
        <div class="internship-looking">
            Seeking a 6-month gap year internship, available worldwide, starting in April 2025.
        </div>


        <!-- Section Work -->
        <div class="work-section" id="work">
            <div class="image-container">
                <img src="{url_for('static', filename='atos.gif')}" alt="Image 1"/>
                <div class="description">
                    <div class="line1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp01 | AI ENGINEER • INTERNSHIP</div>
                    <div class="line2">&nbsp;&nbsp;&nbsp;Atos Group</div>
                    <div class="line3">
                    <ul>
                    <li>Integrated a deep learning model on the Jetson Nano for intelligent transport, achieving 14x faster inference through optimization.</li>
                    <li>Developed pipelines for real-time data transmission to an ITS platform.</li>
                    <li>Created a Flask web app to monitor computer vision use cases.</li>
                    </ul>
                    </div>
                </div>
            </div>
            <div class="image-container">
                <img src="{url_for('static', filename='airbus.gif')}" alt="Image 2"/>
                <div class="description">
                    <div class="line1">02 | DIGITAL CHALLENGE WINNER </div>
                    <div class="line2">Airbus</div>
                    <div class="line3">
                    <ul>
                    <li>Attended training sessions with top Airbus coaches.</li>
                    <li>Proposed an NLP-based solution for managing informal company data.</li>
                    </ul>
                    </div>
                </div>
            </div>
            <div class="image-container">
                <img src="{url_for('static', filename='digital.gif')}" alt="Image 3"/>
                <div class="description">
                    <div class="line1">03 | DATA ANALYST • PROJECT</div>
                    <div class="line2">Digital Escapade</div>
                    <div class="line3">
                    <ul>
                    <li>Processed and extracted key data from the company's database.</li>
                    <li>Designed solutions to improve escape games, including a machine learning-based clue classification system.</li>
                    <li>Presented results via an interactive web app.</li>
                    </ul>
                    </div>
                </div>
            </div>
            <!-- L'image 4 a été supprimée -->
        </div>

        <!-- Technology Bar -->
        <div class="tech-bar">
            <div class="tech-icons">
                <img src="{url_for('static', filename='icons/python.png')}" alt="Python"/>
                <img src="{url_for('static', filename='icons/sql.png')}" alt="SQL"/>
                <img src="{url_for('static', filename='icons/r.png')}" alt="R"/>
                <img src="{url_for('static', filename='icons/tableau.png')}" alt="Tableau"/>
                <img src="{url_for('static', filename='icons/pytorch.png')}" alt="PyTorch"/>
                <img src="{url_for('static', filename='icons/tensorflow.png')}" alt="TensorFlow"/>
                <img src="{url_for('static', filename='icons/docker.png')}" alt="Docker"/>
                <img src="{url_for('static', filename='icons/gitlab.png')}" alt="GitLab"/>
                <img src="{url_for('static', filename='icons/matlab.jpg')}" alt="MATLAB"/>
                <img src="{url_for('static', filename='icons/java.png')}" alt="Java"/>
                <img src="{url_for('static', filename='icons/c++.png')}" alt="C++"/>
            </div>
        </div>

        <!-- Section About Me -->
        <div class="about-section" id="about">
            <h2>About Me</h2>
            <hr class="divider">
            <div class="what-and-lists">
                <div class="what-i-do">What I do</div>
                <div class="lists">
                    <ul class="list">
                        <li>Data Analysis</li>
                        <li>Data Processing</li>
                        <li>Models Implementation</li>
                        <li>Cloud Computing</li>
                    </ul>
                    <ul class="list">
                        <li>Systems Thinking</li>
                        <li>Creative Thinking</li>
                        <li>Project Management</li>
                        <li>Cross-Functional Team Building</li>
                    </ul>
                </div>
            </div>
            <hr class="divider">
            <div class="what-and-lists">
                <div class="more">A little bit more <br> about me :)</div>
                <div class="more-about-me">I’m…<br> 
                <br>
                born and raised in Morocco 🇲🇦 <br> 
                <br>
                a TEAM PLAYER 🤝<br>
                <br>
                an ADAPTABLE PROBLEM-SOLVER<br>
                <br>
                swift in EXECUTION<br>
                <br>
                a TRAVELLER<br>
                <br>
                I love…<br>
                <br>
                ⚽️ football, 🌏 travelling, 👨‍👩‍👦 family, and 🌟 building meaningful connections.<br>
                </div>
            </div>
            <hr class="divider">

        </div>

        <!-- Footer -->
        <div class="footer">
            <p>Collaboration? Feedback? Advice?</p>
            <p class="large-text">I'd love to meet you ;)</p>
            <p>Feel free to contact me</p>
            <a href="https://www.linkedin.com/in/ali-anass-amradouch-321567255/" target="_blank">
                <img src="{url_for('static', filename='icons/linkedin.png')}" alt="LinkedIn" class="linkedin-icon"/>
            </a>
        </div>

        <!-- Contact Form -->
        <div class="contact-form">
            <h2>Contact Me</h2>
            <form action="https://formspree.io/f/xgvwglpp" method="POST">
                <div class="form-group">
                    <label for="name">Name:</label>
                    <input type="text" id="name" name="name" required>
                </div>
                <div class="form-group">
                    <label for="email">Email:</label>
                    <input type="email" id="email" name="email" required>
                </div>
                <div class="form-group">
                    <label for="message">Message:</label>
                    <textarea id="message" name="message" required></textarea>
                </div>
                <button type="submit" class="submit-btn">Send Message</button>
            </form>
        </div>

    </body>
    </html>
    '''
    return render_template_string(html_code)

if __name__ == '__main__':
    app.run(debug=True)
