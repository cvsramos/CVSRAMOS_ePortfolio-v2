import streamlit as st

# Sidebar navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", ['Home', 'Accomplishments', 'Goals', 'Skills', 'Resume', 'Contact'])

if selection == 'Home':
    col1, col2, col3 = st.columns([1,2,1])
    st.title('Carlos Ramos - ePortfolio')
    with col2:
        st.image("https://i.imgur.com/S08tkBg.png", use_column_width=True)
    st.write('''
### Hello there!
Welcome to the ePortfolio of Carlos Ramos!

**Who am I?**
             
I'm a Brazilian Law Graduate who decided to reboot my career and come to Canada to study new stuff! I'm here with my wife, Thayale, and we're starting our married life here in Halifax, NS. This is the first version of my ePortfolio, and I'm still working on it, so please be patient with me.

**What do I do?**
             
I'm currently studying at the Nova Scotia Community College, enrolled in the IT Database Administration program.

Now go ahead and check out the other pages of my ePortfolio using the menu on the left!
''')
    
elif selection == 'Goals':
    st.header('My Goals')
    st.markdown("""
- Graduate with Honors
- Get a job in the IT field
- Be granted the Permanent Residency
- Attend at least 3 networking events and make at least 10 new professional connections
- Complete at least one technical certification in my field of interest
    """)
elif selection == 'Skills':
     st.header('Skills')
     st.markdown("""
**HTML/CSS:** Foundation in creating web pages and styling with CSS.

**Python:** Proficient in data analysis and automation tasks.

**Java:** Experience in Object Oriented Programming.

**SQL:** Skilled in designing and querying relational databases.
                 
This includes experience with MySQL, SQL Server, Postgres and Oracle SQL.

**CISCO - Networking:** Knowledge in network design and security.

**Windows OS & Oracle Linux:** Extensive operating system experience, including troubleshooting and server management.
                 
**Windows OS & Oracle Linux:** Extensive operating system experience, including troubleshooting and server management.
    """)
elif selection == 'Accomplishments':
    st.header('Accomplishments')
    st.markdown("""
- Won the Extra Mile Award at the Halifax Innovation Challenge 2022.
- 3rd prize at the NSCC IT Job Fair's What's Your Challenge in 2023.
    """)
elif selection == 'Resume':
    st.header('Resume')
    st.markdown("""
**Professional Summary:** Experienced IT Database Administration student with a background in law, skilled in project management and analytics.

**Education:** Current study in IT Database Administration at Nova Scotia Community College.

**Work Experience:** Roles in academic analysis, legal analysis, and more, with a track record of achievements and skill application in professional settings.

[View Full Resume](https://1drv.ms/b/s!AkC4skJhkpEFhdpGDpgwbljfWLmFVA?e=X8vd5N)
    """)
elif selection == 'Contact':
    st.header('Contact')
    st.markdown("""
**Personal Information**

- Phone: (902) 989 3724
- Email: [cvsramos@gmail.com](mailto:cvsramos@gmail.com)
- LinkedIn: [linkedin.com/in/cvsramos](https://www.linkedin.com/in/cvsramos)
    """)
