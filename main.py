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
background_image ="assets/images/6193220.jpg" #"https://images.pexels.com/photos/956999/milky-way-starry-sky-night-sky-star-956999.jpeg"
image_base64 = get_base64_image(background_image)
profile_image = "assets/images/Xolela Solomon.jpg" # Use a local image that exists in the workspace
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
    st.markdown('<p>I am a visionary cybersecurity and AI/ML enthusiast and a CAPACITI Tech Career Accelerator graduate, driven to pioneer innovative, secure technology solutions that protect and advance modern digital systems.</p>', unsafe_allow_html=True)
    download_resume()
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with tabs[1]:
    st.markdown('<div class="content">', unsafe_allow_html=True)
    
    st.header("About Me")
    st.write("""
       I am Xolela Solomon, a dedicated technology professional and recent graduate of the CAPACITI Tech Career Accelerator, where I developed strong skills in machine learning, data science, software development, and foundational cybersecurity principles. With a passion for building intelligent and secure systems, I have gained hands-on experience in Python, TensorFlow, and PyTorch through practical bootcamp projects. My journey is driven by continuous learning, innovation, and a commitment to leveraging AI to strengthen cybersecurity solutions.
        """)
    st.write("""**Career Objectives**: My goal is to secure a role in cybersecurity, where I can apply artificial intelligence and machine learning techniques to enhance threat detection, vulnerability analysis, fraud prevention, and incident response. I aim to contribute to securing digital infrastructure across industries such as healthcare, finance, and technology, while continuously advancing my expertise in cybersecurity operations, secure systems design, and AI-driven security solutions.
        """)
    st.write("""**Personal Branding Statement**: I am an innovative problem-solver who transforms complex data into secure, scalable, and actionable insights, delivering AI-powered cybersecurity solutions that protect systems, data, and users.""")
    st.markdown('</div>', unsafe_allow_html=True)

with tabs[2]:
    st.header("🚀 Featured Projects")
    st.write(
        "A selection of projects demonstrating my expertise in AI, machine learning, cybersecurity "
    )

    # -------- Project 1 --------
    with st.container():
        col1, col2 = st.columns([3, 1])

        with col1:
            st.subheader("📍 Route Optimizer for the Transport Sector")
            st.write(
                "An intelligent route optimization system designed to improve logistics efficiency "
                "by calculating optimal delivery paths based on distance, traffic conditions, time "
                "constraints, and vehicle capacity. The system applies graph-based algorithms to "
                "reduce fuel consumption, delivery time, and operational costs."
            )
            st.markdown(
                "**Tech Stack:** Python, Streamlit, Pandas, NumPy, Google Maps API / OpenStreetMap, NetworkX"
            )

        with col2:
            st.markdown("[ GitHub](https://github.com/Serzariax/RouteOptimizer)")

    st.divider()

    # -------- Project 2 --------
    with st.container():
        col1, col2 = st.columns([3, 1])

        with col1:
            st.subheader(" Sentiment Analysis Dashboard")
            st.write(
                "A data-driven NLP dashboard that analyzes public sentiment from text data such as "
                "social media posts, reviews, or surveys. The application classifies sentiment and "
                "visualizes trends, enabling organizations to monitor brand perception and make "
                "data-informed decisions."
            )
            st.markdown(
                "**Tech Stack:** Python, Streamlit, Pandas, NLP (NLTK / spaCy / Transformers), Plotly / Matplotlib"
            )

        with col2:
            st.markdown("[ GitHub](https://github.com/Serzariax/Sentiment-Analysis-Dashboard)")

    st.divider()

    # -------- Project 3 --------
    with st.container():
        col1, col2 = st.columns([3, 1])

        with col1:
            st.subheader(" AI Resume Builder")
            st.write(
                "An AI-powered web application that automates resume creation using natural language "
                "processing. It generates ATS-friendly resumes tailored to specific roles, offering "
                "real-time suggestions, keyword optimization, and export options in multiple formats."
            )
            st.markdown(
                "**Tech Stack:** Python, Streamlit, OpenAI / NLP APIs, Pandas, python-docx, fpdf"
            )

        with col2:
            st.markdown("[ Live Demo](https://five-panel-19326201.figma.site/)")

with tabs[3]:
    st.header(" Technical Skills")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Programming Languages")
        st.markdown("""
        - Python  
        - JavaScript  
        - PHP  
        - SQL  
        - Bash & PowerShell
        """)

        st.subheader("Databases")
        st.markdown("""
        - MySQL  
        - MongoDB  
        - Firebase
        """)

    with col2:
        st.subheader("Web & Backend Development")
        st.markdown("""
        - HTML5, CSS3  
        - React, Node.js  
        - Streamlit 
        - RESTful APIs
        """)

        st.subheader("Development Practices")
        st.markdown("""
        - Git & GitHub  
        - API Integration  
        - Documentation & Testing  
        - Performance Optimization
        """)

    with col3:
        st.subheader("AI & Machine Learning")
        st.markdown(""" 
        - Scikit-learn  
        - NLP & Deep Learning  
        - OpenAI API  
        - Prompt Engineering
        """)

        st.subheader("Cybersecurity")
        st.markdown("""
        - Wireshark  
        - Nmap  
        - Metasploit  
        - OSINT Frameworks  
        - Network Monitoring  
        - Risk Analysis  
        - Penetration Testing
        """)

with tabs[4]:
    st.header(" Contact")

    st.write(
        "I’m open to opportunities, collaborations, and professional networking. "
        "Feel free to reach out through any of the channels below:"
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("🔗 LinkedIn")
        st.markdown("[Xolela Solomon](https://www.linkedin.com/in/xolela-solomon-b8229515b)")

    with col2:
        st.subheader("💻 GitHub")
        st.markdown("[Xolela Solomon](https://github.com/Serzariax)")

    with col3:
        st.subheader("📧 Email")
        st.markdown("[Xolela Solomon](mailto:xolela.solomon@capaciti.org.za)")


# Footer
st.markdown('<div style="text-align: center; color: var(--platinum); padding: 10px;">© 2025 Xolela Solomon. All rights reserved.</div>', unsafe_allow_html=True)