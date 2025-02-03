import streamlit as st

# Title and header
st.title("Interactive CV Viewer")
st.header("Martin Khristi - Business Intelligence Consultant")

# About me
st.subheader("About Me")
st.write("""
Dynamic and detail-oriented Business Intelligence Consultant with over 4 years of hands-on experience. 
Expertise in Power BI, Microsoft Fabric, Python programming, and Machine Learning. Strong focus on ETL processes, data visualization, and driving actionable insights for decision-making.
""")

# Contact Information
st.subheader("Contact Information")
st.write("""
- **Phone:** +45 22 28 65 66  
- **Email:** mkhristi32@gmail.com  
- **Address:** Fjenneslevvej 12 st th, 2700 Brønshøj  
- **LinkedIn:** [linkedin.com/in/martinkhristi](https://linkedin.com/in/martinkhristi)  
- **GitHub:** [github.com/martinkhristi](https://github.com/martinkhristi)
""")

# Experience Section
st.subheader("Experience")
st.write("""
### Business Intelligence Consultant  
**CA - Karrierepartner og A-kasse | June 2023 – Present | Copenhagen, Denmark | On-site**  
- Delivered actionable insights using Power BI and Microsoft Fabric to support decision-making.
- Managed ETL processes and optimized databases, ensuring data accuracy and availability.
- Designed and developed interactive dashboards tailored to business needs, enhancing operational efficiency.
- Collaborated across teams to implement data-driven strategies that improved customer satisfaction and retention.

### Data Science Specialist (Intern)  
**Careerera - SNVA EduTech | April 2021 – January 2023 | Remote**  
- Supported data preprocessing and transformation for analytics and reporting tasks.
- Built machine learning models using Python and R, applying advanced statistical techniques.
- Designed and presented dynamic dashboards in Power BI to communicate data insights.

### Contributor and Tester  
**PandasAI Open-Source Project | Ongoing | Remote**  
- Actively contributed to and tested the development of Pandas AI, an innovative open-source tool for performing data analysis using natural language.
- Collaborated with the development team to enhance the tool's functionality, ensuring efficient and accurate data analysis workflows.
- Tested new features and provided valuable feedback to improve performance and user experience.
""")

# Skills
st.subheader("Skills")
st.write("""
- **Business Intelligence:** Power BI, Microsoft Fabric, ETL Processes  
- **Programming:** Python, SQL  
- **Database Management:** SQL, Optimization, Data Warehousing  
- **Natural Language Analytics:** PandasAI  
- **Machine Learning:** Model Development, Feature Engineering  
- **Time Series Forecasting:** ARIMA, SARIMA, Prophet  
""")

# AI Projects
st.subheader("AI Projects")
st.write("""
- **[Realtime Voice Bot](https://github.com/martinkhristi/realtime_voice_bot):** Build a real-time AI voice assistant app in 2 minutes (open-source edition).  
- **[AI-News-Generator](https://github.com/martinkhristi/AI-News-Generator):** Generate comprehensive blog posts about any topic using AI agents.  
- **[Gemini 2.0 Multimodal Chatbot](https://github.com/martinkhristi/gemini2.0_multimodal_chatbot):** A Streamlit application demonstrating a multimodal chatbot using Google's Gemini Flash model.  
- **[RAG over Excel with IBM Dockling and Llama 3.2](https://github.com/martinkhristi/RAG-over-Excel-using-IBM-Dockling-Llama-3.2-100-Locally-):** Use Retrieval-Augmented Generation (RAG) for Excel with Llama 3.2 locally.  
- **[MarkAI-RAG](https://github.com/martinkhristi/MarkAI-RAG):** Use RAG with Groq API, Microsoft MarkItDown, and PandasAI for smart document querying.  
- **[Chat with Docs](https://github.com/martinkhristi/Chat-with-Docs-powered-by-ModernBert-and-Llama-3.2-100-open-source-and-100-secure-):** Chat with documents using ModernBERT and Llama 3.2, open-source and secure.
""")

# Education
st.subheader("Education")
st.write("""
**Bachelor of Computer Science**  
2020 - MS University
""")

# Certifications
st.subheader("Awards and Certifications")
st.write("""
- Data Fundamentals – IBM SkillsBuild  
- Machine Learning Fundamentals – Alteryx  
- Microsoft Certified Azure AI Fundamentals  
- Post Graduation Program – Career-era  
- Tata - Data Visualization: Empowering Business with Effective Insights Job Simulation  
- PwC Switzerland - Power BI Job Simulation  
- Danish Language PD 2  
""")

# Languages
st.subheader("Languages")
st.write("""
- English: Fluent  
- Danish: Intermediate  
""")

# Hobbies
st.subheader("Hobbies")
st.write("""
- Listening to music  
- Playing Cricket  
- Reading books        
- Yoga  
""")

st.markdown("---")
st.write("Created with ❤️ using Streamlit.")
