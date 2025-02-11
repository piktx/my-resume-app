import streamlit as st

# Title and header
st.title("Interactive CV Viewer")
st.header("Piyush Kumar Tiwari - Data Scientist")

# About me
st.subheader("About Me")
st.write("""
Dynamic and detail-oriented Data Scientist with over 5 years of hands-on experience. 
Expertise in Python, Machine Learning, SQL. Strong focus on Reinforcement Leaning, GEN AI, and driving actionable insights for decision-making using ML models.
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
- **Machine Learning:** Model Development, Feature Engineering, Reinforcement Learning 
- **Time Series Forecasting:** ARIMA, SARIMA, Prophet
""")

# AI Projects
st.subheader("AI Projects")
st.write("""
- **[AI-News-Generator](https://github.com/piktx/ai-news-gen):** Generate comprehensive blog posts about any topic using AI agents.  
- **[Gemini 2.0 Multimodal Chatbot](https://github.com/piktx/flash-mutimodal-chatbot):** A Streamlit application demonstrating a multimodal chatbot using Google's Gemini Flash model.  
- **[RAG over Excel with IBM Dockling and Llama 3.2](https://github.com/piktx/excel-rag):** Use Retrieval-Augmented Generation (RAG) for Excel with Llama 3.2 locally.  
- **[MarkAI-RAG](https://github.com/piktx/markai-rag):** Use RAG with Groq API, Microsoft MarkItDown, and PandasAI for smart document querying.  
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
- Playing Cricket  
- Reading books        
- Yoga  
""")

st.markdown("---")
st.write("Created with ❤️ using Streamlit.")
