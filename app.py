import streamlit as st
from textblob import TextBlob

# Title
st.title("🤖 AI Mentor - Sentiment & Career Support")

# Sidebar Menu
menu = ["Home", "Sentiment Support", "Career Guidance", "Resume Tips"]
choice = st.sidebar.selectbox("📌 Navigate", menu)

# 1. Home
if choice == "Home":
    st.subheader("Welcome to AI Mentor! 🎯")
    st.write("This app helps you with:")
    st.markdown("""
    1. **💬 Sentiment Support** - Share your feelings and get AI feedback  
    2. **🎓 Career Guidance** - Get career tips based on your mood  
    3. **📄 Resume Tips** - Learn how to improve your resume  
    """)

# 2. Sentiment Support
elif choice == "Sentiment Support":
    st.subheader("💬 Sentiment Support")
    user_input = st.text_area("Type how you feel:")

    if st.button("Analyze"):
        if user_input.strip() != "":
            blob = TextBlob(user_input)
            sentiment = blob.sentiment.polarity

            if sentiment > 0:
                st.success("😊 Positive Sentiment")
                st.write("Keep up the good vibes! You're doing great 🚀")
            elif sentiment < 0:
                st.error("☹️ Negative Sentiment")
                st.write("Don't worry, tough times don’t last. Stay strong 💪")
            else:
                st.info("😐 Neutral Sentiment")
                st.write("Thanks for sharing your feelings. Stay balanced ✨")
        else:
            st.warning("⚠️ Please type something to analyze.")

# 3. Career Guidance
elif choice == "Career Guidance":
    st.subheader("🎓 Career Guidance")
    mood = st.selectbox("How are you feeling today?", ["Motivated", "Confused", "Stressed", "Excited"])

    if mood == "Motivated":
        st.success("🔥 Great! Use this energy to apply for jobs or work on projects.")
    elif mood == "Confused":
        st.info("🤔 Try exploring different career paths. Start with internships and certifications.")
    elif mood == "Stressed":
        st.error("😓 Take a break, relax, and come back stronger. Balance is important.")
    else:
        st.success("🎉 Keep your excitement alive! Work on something creative today.")

# 4. Resume Tips
elif choice == "Resume Tips":
    st.subheader("📄 Resume Tips")

    st.markdown("""
    ✅ **Tips for a strong resume:**
    - Keep it **1 page** (for freshers).
    - Highlight **skills, projects, and internships**.
    - Use **action words** (Developed, Designed, Implemented).
    - Avoid spelling/grammar mistakes.
    - Tailor resume for each job.
    """)

    st.write("🔽 Example Resume Format:")

    resume_template = """Name: Your Name
Email: your.email@example.com
Phone: +91-XXXXXXXXXX

Summary:
Enthusiastic and detail-oriented graduate with a passion for technology and problem-solving. Skilled in Python, Java, and SQL. Strong interest in full-stack development and cloud computing.

Education:
- B.Tech in Computer Science, XYZ College, 2025

Skills:
- Programming: Python, Java, C, SQL
- Web: HTML, CSS, JavaScript, Django, Bootstrap
- Tools: Git, Google Colab

Experience:
- Internships in AI, Cloud Computing, Data Science, and Full Stack Java

Projects:
- Disease Detection using Deep Learning
- Web-based Student Event Management System

Achievements:
- Scored 531/800 in CoCubes (2025)
- Certified in Python Programming
"""
    st.code(resume_template, language="markdown")
