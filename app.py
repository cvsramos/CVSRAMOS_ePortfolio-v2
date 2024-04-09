import streamlit as st

# Creating tabs for navigation
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Home", "Accomplishments", "Goals", "Skills", "Resume", "Contact"])

with tab1:
    col1, col2, col3 = st.columns([1,2,1])
    st.title('Carlos Ramos - ePortfolio')
    with col2:
        st.image("https://i.imgur.com/S08tkBg.png", use_column_width=True)
    st.write('''
### Hello there!
Welcome to the ePortfolio of Carlos Ramos!

**Who am I?**
             
I'm a Brazilian Law Graduate who decided to reboot my career and come to Canada to study new stuff! I'm here with my wife, Thayale, and we're starting our married life here in Halifax, NS. This is portfolio is a work in progress and will be updated with new content!

**What do I do?**
             
I'm currently studying at the Nova Scotia Community College, enrolled in the IT Database Administration program.

Now go ahead and check out the other pages of my ePortfolio!
''')
    
with tab2:
    st.header('My Goals')
    st.markdown("""
- Graduate with Honors
- Get a job in the IT field
- Attend at least 3 networking events and make at least 10 new professional connections
- Complete at least one technical certification in my field of interest
    """)
with tab3:
     st.header('Skills')
     st.markdown("""
**HTML/CSS:** Foundation in creating web pages and styling with CSS.

**Python:** Proficient in data analysis and automation tasks.

**Java:** Experience in Object Oriented Programming.

**SQL:** Skilled in designing and querying relational databases.
                 
This includes experience with MySQL, SQL Server, Postgres and Oracle SQL.

**CISCO - Networking:** Knowledge in network design and security.

**Windows OS & Oracle Linux:** Extensive operating system experience, including troubleshooting and server management.
    """)
with tab4:
    st.header('Accomplishments')
    st.markdown("""
- Won the Extra Mile Award at the Halifax Innovation Challenge 2022.
- 3rd prize at the NSCC IT Job Fair's What's Your Challenge in 2023.
    """)
with tab5:
    st.header('Resume')
    st.markdown("""
**Professional Summary:** Experienced IT Database Administration student with a background in law, skilled in project management and analytics.

**Education:** Current study in IT Database Administration at Nova Scotia Community College.

**Work Experience:** Roles in academic analysis, legal analysis, and more, with a track record of achievements and skill application in professional settings.

[View Full Resume](https://1drv.ms/b/s!AkC4skJhkpEFhdpGDpgwbljfWLmFVA?e=X8vd5N)
    """)
with tab6:
    st.header('Contact')
    st.markdown("""
**Personal Information**

- Phone: (902) 989 3724
- Email: [cvsramos@gmail.com](mailto:cvsramos@gmail.com)
- LinkedIn: [linkedin.com/in/cvsramos](https://www.linkedin.com/in/cvsramos)
    """)
