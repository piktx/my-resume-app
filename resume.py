import streamlit as st

# Title and header
st.title("Interactive CV Viewer")
st.header("Piyush Kumar Tiwari - Data Scientist")

# About me
st.subheader("About Me")
st.write("""
Dynamic and detail-oriented Business Intelligence Consultant with over 4 years of hands-on experience. 
Expertise in Power BI, Microsoft Fabric, Python programming, and Machine Learning. Strong focus on ETL processes, data visualization, and driving actionable insights for decision-making.
""")

# Contact Information
st.subheader("Contact Information")
st.write("""
- **Email:** businessbypkt@gmail.com  
- **Address:** Lucknow, India  
- **LinkedIn:** [linkedin.com/in/pikt](https://linkedin.com/in/pikt)  
- **GitHub:** [github.com/piktx](https://github.com/piktx)
""")

# Experience Section
st.subheader("Experience")
st.write("""
### Data Engineer 
**BainBridge | Jan 2023 - Jan 2024 | Remote**  
- Analyzed trends and patterns in customer behaviors, improving insights by **30%**.  
- Designed surveys and polls, increasing response rates by **25%**.  
- Built end-to-end predictive models using ML algorithms, achieving **85% prediction accuracy**.  
- Streamlined ETL processes, improving data pipeline stability and reducing errors by **15%**. 

### Data Analyst  
**DataDrive | Feb 2019 - March 2022 | Remote**  
- Improved data accuracy by **20%**, enabling robust data management.  
- Analyzed large datasets using statistical techniques, enhancing data-driven decisions for partners and customers.  
- Identified trends and correlations in complex data, visualized insights, and supported strategic decision-making.  
- Delivered **10+ monthly reports** by compiling data, updating spreadsheets, and conducting research.  
- Resolved data collection and reporting bugs, reducing errors by **15%** through root cause analysis.
""")

# Skills
st.subheader("Skills")
st.write("""
- **Business Intelligence:** Power BI, Tableau, ETL Processes  
- **Programming:** Python, PostgreSQL, PyTorch   
- **Database Management:** SQL Server, MongoDB, Data Warehousing  
- **Natural Language Analytics:** PandasAI  
- **Machine Learning:** Model Development, Feature Engineering, Reinforcement Learning 
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

# Languages
st.subheader("Languages")
st.write("""
- English: Fluent  
- Hindi: Fluent  
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
