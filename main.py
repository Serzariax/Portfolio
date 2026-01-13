import streamlit as st
import requests
import base64
from io import BytesIO
# Load and encode background image

def get_base64_image(image_path):
    if image_path.startswith("http"):
        response = requests.get(image_path)
        response.raise_for_status()
        image_bytes = response.content
    else:
        with open(image_path, "rb") as image_file:
            image_bytes = image_file.read()
    return base64.b64encode(image_bytes).decode()

# Load images (CAPACITI logo placeholder; replace with actual logo)
background_image ="https://images.pexels.com/photos/333850/pexels-photo-333850.jpeg" #"https://images.pexels.com/photos/956999/milky-way-starry-sky-night-sky-star-956999.jpeg"
image_base64 = get_base64_image(background_image)
profile_image = "assets/images/profile.jpg" # Use a local image that exists in the workspace
profile_image_base64 = get_base64_image(profile_image)#image_pro_base64 = get_base64_image(profile_image)
# Define CAPACITI-inspired professional color palette
st.markdown(f"""
    <style>
    :root {{
        --rich-black: #0d1b2aff;
        --oxford-blue: #1b263bff;
        --yinmn-blue: #415a77ff;
        --silver-lake-blue: #778da9ff;
        --platinum: #e0e1ddff;
    }}
    body {{
        background: linear-gradient(135deg, #0d1b2a, #1b263b),
                    url('data:image/jpeg;base64,{image_base64}') no-repeat center center fixed !important;
        background-size: cover !important;
    }}
    .stApp, .main, .block-container {{
        background: transparent !important;
    }}
    .block-container {{
        background: transparent !important;
    }}
    .header {{
        background-color: var(--yinmn-blue);
        color: var(--platinum);
        text-align: center;
        padding: 10px 0;
        position: fixed;
        width: 100%;
        top: 0;
        z-index: 1000;
    }}
    .header img {{
        height: 40px;
        vertical-align: middle;
    }}
    h1, h2, h3 {{
        color: var(--silver-lake-blue);
        font-weight: 900;
        letter-spacing: 1px;
    }}
    p, li {{
        color: var(--platinum);
        font-size: 16px;
    }}
    .nav-bar {{
        display: flex;
        justify-content: center;
        background-color: var(--oxford-blue);
        padding: 0;
        margin: 0;
        border-bottom: 2px solid var(--yinmn-blue);
    }}
    .nav-bar .stTabs [data-baseweb="tab-list"] {{
        background: transparent;
        border: none;
        margin: 0;
        padding: 0;
    }}
    .nav-bar .stTabs [data-baseweb="tab"] {{
        background: transparent;
        color: var(--platinum);
        padding: 12px 25px;
        margin: 0 10px;
        border: none;
        border-bottom: 3px solid transparent;
        transition: all 0.3s ease;
        font-weight: bold;
        text-transform: uppercase;
    }}
    .nav-bar .stTabs [aria-selected="true"] {{
        border-bottom: 3px solid var(--silver-lake-blue);
        color: var(--platinum);
    }}
    .content {{
        margin-top: 60px; /* Adjust to match header height */
        padding: 20px;
    }}
    .home-content {{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start;
        text-align: center;
        padding-top: 0;
        margin-top: 0;
    }}
    .profile-img {{
        border-radius: 50%;
        width: 250px;
        height: 250px;
        border: 5px solid var(--silver-lake-blue);
        box-shadow: 0 0 10px rgba(119, 141, 169, 0.3);
        animation: rotate 20s linear infinite;
    }}
    @keyframes rotate {{
        from {{ transform: rotate(0deg); }}
        to {{ transform: rotate(360deg); }}
    }}
    .blurred-bg {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: url('data:image/jpeg;base64,{image_base64}');
        background-size: cover;
        filter: blur(10px);
        z-index: -1;
        opacity: 0.7;
    }}
    .download-btn {{
        background-color: var(--silver-lake-blue);
        color: var(--rich-black);
        padding: 10px 20px;
        border-radius: 20px;
        text-decoration: none;
        font-weight: bold;
        transition: all 0.3s ease;
        margin-top: 20px;
    }}
    .download-btn:hover {{
        transform: scale(1.05);
        box-shadow: 0 0 10px var(--silver-lake-blue);
    }}
    </style>
    """, unsafe_allow_html=True)
#st.markdown(f"""
   # <div class="blurred-bg"></div>
    #""", unsafe_allow_html=True)

# ATS-optimized resume content as base64 PDF with AI/ML keywords
resume_pdf_base64 = "data:application/pdf;base64,JVBERi0xLjQKJeLjz9MKMSAwIG9iago8PCAvVHlwZSAvQ2F0YWxvZyAvUGFnZXMgMiAwIFIgPj4KZW5kb2JqCjIgMCBvYmoKPDwgL1R5cGUgL1BhZ2VzIC9LaWRzIFsgMyAwIFJdIC9Db3VudCAxID4+CmVuZG9iagozIDAgb2JqCjw8IC9UeXBlIC/..."  # Placeholder; replace with actual base64-encoded resume

# Function to download resume
def download_resume():
    href = f'<a href="{resume_pdf_base64}" download="Xolela_Solomon_Resume.pdf" class="download-btn">Download Resume</a>'
    st.markdown(href, unsafe_allow_html=True)

# Header with CAPACITI branding
st.markdown("""
    <div class="header">
        #<img src="https://via.placeholder.com/150x40?text=CAPACITI+Logo" alt="CAPACITI Logo">
       <span>Tech Career Accelerator</span>
    </div>
    """, unsafe_allow_html=True)

# Navigation bar
tabs = st.tabs(["Home", "About", "Projects", "Skills", "Contact"])
st.markdown('<div class="nav-bar">', unsafe_allow_html=True)
with tabs[0]:
    st.markdown('<div class="content">', unsafe_allow_html=True)
    #st.markdown(f"""
        #<div style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background-image: url('data:image/jpeg;base64,{image_base64}'); background-size: cover; z-index: -1;"></div>
        #""", unsafe_allow_html=True)
    st.markdown('<div class="home-content">', unsafe_allow_html=True)
    st.markdown(f'<h1>Xolela Solomon Portfolio</h1>', unsafe_allow_html=True)
    st.markdown(f'<img src="data:image/jpeg;base64,{profile_image_base64}" class="profile-img">', unsafe_allow_html=True)
    st.markdown('<p>I am a visionary AI/ML enthusiast and CAPACITI Tech Career Accelerator graduate, pioneering cutting-edge tech innovations.</p>', unsafe_allow_html=True)
    download_resume()
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with tabs[1]:
    st.markdown('<div class="content">', unsafe_allow_html=True)
    
    st.header("About Me")
    st.write("""
       I am Xolela Solomon, a dedicated technology professional and recent graduate of the CAPACITI Tech Career Accelerator, where I developed strong skills in machine learning, data science, software development, and foundational cybersecurity principles. With a passion for building intelligent and secure systems, I have gained hands-on experience in Python, TensorFlow, and PyTorch through practical bootcamp projects. My journey is driven by continuous learning, innovation, and a commitment to leveraging AI to strengthen cybersecurity solutions

        **Career Objectives**: My goal is to secure a role in cybersecurity, where I can apply artificial intelligence and machine learning techniques to enhance threat detection, vulnerability analysis, fraud prevention, and incident response. I aim to contribute to securing digital infrastructure across industries such as healthcare, finance, and technology, while continuously advancing my expertise in cybersecurity operations, secure systems design, and AI-driven security solutions.
        **Personal Branding Statement**: I am an innovative problem-solver who transforms complex data into secure, scalable, and actionable insights, delivering AI-powered cybersecurity solutions that protect systems, data, and users.
    st.markdown('</div>', unsafe_allow_html=True)

with tabs[2]:
    st.markdown('<div class="content">', unsafe_allow_html=True)
    
    st.header("Featured Projects")
    st.subheader("Project 1: Route Optimizer for the Transport Sector")
    st.write("""
       The Route Optimizer is an intelligent system designed to streamline logistics and transportation by calculating the most efficient delivery or travel routes. It leverages algorithms that analyze multiple factors such as distance, traffic conditions, delivery time windows, and vehicle capacity to minimize operational costs and maximize efficiency.

The project was developed for the transport sector, where route planning directly affects fuel consumption, delivery time, and overall resource utilization. The system integrates data from multiple sources and applies optimization techniques such as Dijkstras algorithm, A* search, or genetic algorithms  to produce real-time route recommendations.

Key Features:

Dynamic route calculation based on live or simulated traffic data.

Cost and distance optimization to reduce travel time and fuel usage.

Support for multiple stops and delivery points.

Custom constraints (vehicle load, delivery priority, or time limits).

Interactive map visualization for route inspection.

Tech Stack:
Python, Streamlit (for the web interface), Google Maps API / OpenStreetMap, Pandas, NumPy, and possibly a graph library like NetworkX for pathfinding.

Impact:
This project demonstrates how AI and algorithmic optimization can be applied to solve real-world logistical challenges, improving productivity and reducing transport costs for businesses.""")
    st.markdown("[Live Demo](https://github.com/Serzariax/RouteOptimizer)")
    st.subheader("Project 2: Sentiment Analysis Dashboard")
    st.write("""
        The Sentiment Analysis Dashboard is a data driven web application that analyzes and visualizes public opinions, emotions, and attitudes expressed in text data—such as social media posts, customer reviews, or survey responses. It applies Natural Language Processing (NLP) and machine learning techniques to classify text into sentiment categories (positive, negative, neutral) and presents results through an interactive dashboard.

The project was designed to help organizations monitor public perception, track brand reputation, and gain actionable insights from large volumes of unstructured text data.

Key Features:

Real-time sentiment classification using pretrained NLP models (e.g., VADER, TextBlob, or transformer-based models like BERT).

Data visualization of sentiment trends over time using interactive charts and graphs.

Word clouds and keyword frequency analysis for quick insight into dominant themes.

Filtering and search capabilities for exploring specific topics or timeframes.

Integration with social media APIs (like Twitter or Reddit) or CSV uploads for flexible data input.

Tech Stack:
Python, Streamlit (for the dashboard interface), Pandas, Matplotlib / Plotly for visualization, and NLP libraries such as NLTK, spaCy, or Hugging Face Transformers.

Impact:
The dashboard provides an intuitive way to transform raw text data into meaningful business intelligence. It enables decision-makers to understand customer sentiment in real-time and adjust strategies accordingly — whether for marketing, product development, or crisis management.""")
    st.markdown("[Live Demo](https://github.com/Serzariax/Sentiment-Analysis-Dashboard)")
    st.subheader("Project 3: AI Resume Builder")
    st.write("""
        The AI Resume Builder is an intelligent web application that automates the process of creating professional, tailored resumes using artificial intelligence and natural language processing (NLP). It helps users generate, format, and customize resumes based on their skills, experience, and career goals — eliminating the need for manual editing and design.

The system analyzes user input (such as job titles, achievements, or keywords) and uses machine learning models to recommend strong phrasing, highlight relevant skills, and ensure that the resume aligns with ATS (Applicant Tracking System) standards. It can also generate resumes in multiple formats like PDF, DOCX, and Markdown, complete with a clean, modern layout.

Key Features:

AI-powered text generation for resume sections (summary, experience, skills).

Real-time suggestions and keyword optimization for specific job roles.

Export options for multiple formats (PDF, DOCX, TXT).

Smart formatting and design templates.

Option to import or parse existing resumes for editing or enhancement.

Tech Stack:
Python, Streamlit (for the user interface), OpenAI / NLP APIs for text generation, Pandas for data handling, and libraries like python-docx and fpdf for document creation.

Impact:
The project demonstrates how AI can simplify and enhance the job application process by helping users craft compelling, professional resumes in minutes. It bridges the gap between automation and personalization — empowering users to focus on showcasing their potential rather than formatting documents.""")
    st.markdown("[Live Demo](https://five-panel-19326201.figma.site/)")
    st.markdown('</div>', unsafe_allow_html=True)

with tabs[3]:
    st.markdown('<div class="content">', unsafe_allow_html=True)
    
    st.header("Technical Skills")
    skills = [
"Programming Languages: Python, JavaScript, C++, SQL, Bash, PowerShell",

"Web Development: HTML5, CSS3, React, Node.js, Streamlit, Flask, RESTful APIs",

"AI & Machine Learning: TensorFlow, PyTorch, Scikit-learn, OpenAI API, NLP, Deep Learning",

"Data Analysis & Visualization: Pandas, NumPy, Matplotlib, Plotly, Power BI",

"Database Management: MySQL, PostgreSQL, MongoDB, Firebase",

"Cloud & DevOps: AWS, Azure, Docker, GitHub Actions, CI/CD pipelines",

"Cybersecurity Tools: Wireshark, Metasploit, Burp Suite, Nmap, Splunk, Nessus, OSINT Frameworks",

"Operating Systems: Windows, Linux (Ubuntu, Kali), macOS",

"Automation & Scripting: Shell scripting, Python automation, Ansible basics",

"Version Control: Git, GitHub, GitLab",

"Core Competencies",

"Secure software design and vulnerability assessment",

"AI model development and prompt engineering",

"Data-driven decision making and model optimization",

"Full-stack application development and deployment",

"Network monitoring, risk analysis, and penetration testing",

"API integration and backend system design",

"Project planning and agile development",

"Analytical problem-solving and debugging",

"Documentation, testing, and performance optimization",

"Collaboration across multidisciplinary tech teams"
    ]
    for skill in skills:
        st.write(f"- {skill}")
    st.markdown('</div>', unsafe_allow_html=True)

with tabs[4]:
    st.markdown('<div class="content">', unsafe_allow_html=True)
   
    st.header("Contact")
    st.write("LinkedIn: [Xolela Solomon](https://linkedin.com/in/xolelasolomon)")
    st.write("GitHub: [xolelasolomon](https://github.com/Serzariax)")
    st.write("Email: xolela.solomon@example.com")
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div style="text-align: center; color: var(--platinum); padding: 10px;">© 2025 Xolela Solomon. All rights reserved.</div>', unsafe_allow_html=True)