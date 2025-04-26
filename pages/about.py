import streamlit as st
def show():
    st.title("About Us")
    
    # Mission Banner
    st.markdown("""
    <div style="background-color: #6096BA; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
        <h2 style="color: white; text-align: center; margin: 0;">Our Mission: To make mental health care accessible for everyone</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ## Who We Are
    
    Mental Health Hub was created by a team of passionate developers and mental health advocates who believe 
    that quality mental health information and resources should be available to everyone.
    
    Our team combines expertise in psychology, education, and technology to create a platform that makes 
    mental health knowledge accessible, engaging, and practical.
    """)
    
    # Developer profiles
    st.header("Our Team")
    
    # Team members
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.image("assets/yash.jpeg", width=200)
        st.markdown("""
        **Yash Pandey**  
        *Developer*
        
        Yash loves talking and researching about human psychology and is also a passionate developer
        """)
    
    with col2:
        st.image("assets/1tanazza.jpg", width=200)
        st.markdown("""
        **Tanazza**  
        *Developers*
        
        Tanazza is a passionate developer who loves to create engaging and interactive content. She is dedicated to making mental health resources accessible to all.
        """)
    
    with col3:
        st.image("assets/harshita.jpg", width=200)
        st.markdown("""
        **Harshita**  
        *Developer*
        
        Harshita combined her tech expertise with a passion for mental health to build this platform, making it user-friendly and engaging.
        """)
    
    # Our approach section
    st.markdown("---")
    st.header("Our Approach")
    
    st.markdown("""
    
    
    ### Accessible for Everyone
    
    We believe mental health resources should be available to all. Our content is written in clear, jargon-free language and designed to be helpful regardless of your background or experience.
    
    ### Stigma Reduction
    
    Through education and open discussion, we aim to reduce the stigma surrounding mental health issues and encourage more people to seek help when needed.
    
    ### Tech for Good
    
    We leverage technology to make mental health information more interactive, personalized, and engaging, helping users better understand their own mental health.
    """)
    
    # Contact information
    st.markdown("---")
    st.header("Contact Us")
    
    st.markdown("""
    We welcome your feedback, questions, and suggestions. Please reach out to us at:
    
    📧 Email: yashpandey1556@gmail.com / Tanazzamuskan@gmail.com / loveharshi005@gmail.com
    📱 Phone: +91 9717273400 , 9315067537 , 9654558311
    
   
    """)
    
    # Add sticky footer
    st.markdown("""
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #123458;
        padding: 10px 0;
        text-align: center;
        font-size: 14px;
        border-top: 1px solid #e6e6e6;
        z-index: 999;
    }
    
    .main .block-container {
        padding-bottom: 50px;
    }
    </style>
    
    <div class="footer">
        Made with ❤️ in India
    </div>
    """, unsafe_allow_html=True)

# Disclaimer
    st.markdown("""
    ---
    ⚠ *Disclaimer:*  
    The ML-generated quiz *is not a medical diagnosis*. It is only meant to give you a general idea about your mental health condition.  
    If you're experiencing mental health challenges, *please consult a qualified medical professional*.  
""")
