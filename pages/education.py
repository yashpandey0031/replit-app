import streamlit as st



def show():
    st.title("Mental Health Education")
    
    st.markdown("""
    ## Understanding Mental Health
    
    Education is a key component in understanding and addressing mental health. 
    This page provides comprehensive information about various mental health topics, 
    conditions, treatment options, and coping strategies.
    """)
    
    # Categories tabs
    tabs = st.tabs([
        "Understanding Mental Health", 
        "Common Conditions", 
        "Treatment Options", 
        "Self-Care Strategies", 
        "Supporting Others"
    ])
    
    # Tab 1: Understanding Mental Health
    with tabs[0]:
        st.header("What is Mental Health?")
        
        st.markdown("""
        Mental health includes our emotional, psychological, and social well-being. 
        It affects how we think, feel, and act. It also helps determine how we handle stress, 
        relate to others, and make choices.
        
        Mental health is important at every stage of life, from childhood and adolescence through adulthood.
        
        ### The Importance of Mental Health
        
        Mental health is fundamental to our collective and individual ability to:
        
        - Think, express emotions, and interact with each other
        - Earn a living and enjoy life
        - Contribute to our communities
        
        ### Mental Health vs. Mental Illness
        
        Mental health exists on a spectrum. Having good mental health doesn't just mean the absence of mental health problems.
        
        **Good mental health** is characterized by:
        - Ability to learn
        - Ability to feel, express and manage emotions
        - Ability to form and maintain good relationships
        - Ability to cope with change and uncertainty
        
        **Mental illness** refers to conditions that affect your thinking, feeling, mood, and behavior. 
        These can be occasional or long-lasting (chronic) and can affect your ability to function and relate to others.
        """)
        
        st.subheader("Mental Health Determinants")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### Biological Factors
            - Genetics and family history
            - Brain chemistry and structure
            - Hormonal factors
            - Prenatal development and birth complications
            """)
        
        with col2:
            st.markdown("""
            ### Environmental Factors
            - Childhood experiences and trauma
            - Life stressors and major life changes
            - Social support and relationships
            - Socioeconomic status and education
            - Exposure to violence or abuse
            """)
        
        st.subheader("Mental Health Statistics")
        
        st.markdown("""
        - Globally, approximately **1 in 4 people** will experience a mental health condition in their lifetime
        - Depression is a leading cause of disability worldwide
        - Suicide is the second leading cause of death among 15-29-year-olds globally
        - More than 75% of people in low and middle-income countries receive no treatment for mental health conditions
        - Mental health conditions are on the rise, with a 13% increase in mental health conditions and substance use disorders in the last decade
        """)
    
    # Tab 2: Common Conditions
    with tabs[1]:
        st.header("Common Mental Health Conditions")
        
        conditions = [
            "Depression", 
            "Anxiety Disorders", 
            "Bipolar Disorder", 
            "Post-Traumatic Stress Disorder", 
            "Obsessive-Compulsive Disorder",
            "Schizophrenia",
            "Eating Disorders"
        ]
        
        for condition in conditions:
            with st.expander(condition):
                if condition == "Depression":
                    st.markdown("""
                    ### Depression (Major Depressive Disorder)
                    
                    Depression is a common and serious medical illness that negatively affects how you feel, think, and act.
                    
                    #### Symptoms
                    - Persistent sad, anxious, or "empty" mood
                    - Loss of interest in activities once enjoyed
                    - Decreased energy, fatigue
                    - Difficulty sleeping or oversleeping
                    - Changes in appetite or weight
                    - Thoughts of death or suicide
                    
                    #### Types of Depression
                    - Major Depression
                    - Persistent Depressive Disorder
                    - Seasonal Affective Disorder (SAD)
                    - Postpartum Depression
                    
                    #### Facts
                    - Affects approximately 264 million people worldwide
                    - More common in women than men
                    - Can occur at any age but often begins in adulthood
                    - Highly treatable with psychotherapy, medication, or a combination
                    """)
                
                elif condition == "Anxiety Disorders":
                    st.markdown("""
                    ### Anxiety Disorders
                    
                    Anxiety disorders involve more than temporary worry or fear. The anxiety does not go away and can get worse over time.
                    
                    #### Common Types
                    
                    **Generalized Anxiety Disorder (GAD)**
                    - Persistent and excessive worry about various things
                    - Difficulty controlling the worry
                    - Physical symptoms: restlessness, fatigue, muscle tension
                    
                    **Panic Disorder**
                    - Recurrent unexpected panic attacks
                    - Worry about having more panic attacks
                    - Avoidance of situations that might trigger panic
                    
                    **Social Anxiety Disorder**
                    - Intense fear of social or performance situations
                    - Fear of negative evaluation or judgment
                    - Avoidance of social situations
                    
                    **Specific Phobias**
                    - Intense fear of a specific object or situation
                    - Avoidance of the feared object/situation
                    - Fear disproportionate to actual danger
                    
                    #### Facts
                    - Anxiety disorders are the most common mental disorders, affecting 264 million people worldwide
                    - Often begin in childhood, adolescence, or early adulthood
                    - Highly treatable with therapy, medication, or both
                    - Women are more likely than men to experience anxiety disorders
                    """)
                
                elif condition == "Bipolar Disorder":
                    st.markdown("""
                    ### Bipolar Disorder
                    
                    Bipolar disorder causes unusual shifts in mood, energy, activity levels, concentration, and the ability to carry out day-to-day tasks.
                    
                    #### Types
                    
                    **Bipolar I Disorder**
                    - Defined by manic episodes that last at least 7 days or severe manic symptoms requiring hospitalization
                    - Depressive episodes typically last at least 2 weeks
                    
                    **Bipolar II Disorder**
                    - Defined by a pattern of depressive episodes and hypomanic episodes (less severe than full mania)
                    - No full manic episodes
                    
                    **Cyclothymic Disorder**
                    - Periods of hypomanic and depressive symptoms lasting for at least 2 years
                    - Symptoms don't meet criteria for hypomanic or depressive episodes
                    
                    #### Symptoms of Manic Episodes
                    - Feeling unusually "high," euphoric, or irritable
                    - Increased energy and activity
                    - Racing thoughts and rapid speech
                    - Decreased need for sleep
                    - Risky behavior and poor judgment
                    
                    #### Facts
                    - Affects about 45 million people worldwide
                    - Typically develops in late adolescence or early adulthood
                    - Equally common among men and women
                    - Requires long-term treatment, usually medication and psychotherapy
                    """)
                
                elif condition == "Post-Traumatic Stress Disorder":
                    st.markdown("""
                    ### Post-Traumatic Stress Disorder (PTSD)
                    
                    PTSD is a disorder that develops in some people who have experienced a shocking, scary, or dangerous event.
                    
                    #### Symptoms
                    
                    **Re-experiencing symptoms**
                    - Flashbacks
                    - Nightmares
                    - Intrusive thoughts
                    
                    **Avoidance symptoms**
                    - Staying away from places, events, or objects that remind of the traumatic experience
                    - Avoiding thoughts or feelings related to the trauma
                    
                    **Arousal and reactivity symptoms**
                    - Being easily startled
                    - Feeling tense or on edge
                    - Difficulty sleeping
                    - Angry outbursts
                    
                    **Cognition and mood symptoms**
                    - Negative thoughts about oneself or the world
                    - Distorted feelings of guilt or blame
                    - Loss of interest in enjoyable activities
                    - Difficulty remembering key features of the trauma
                    
                    #### Facts
                    - Can develop at any age
                    - Women are more likely to develop PTSD than men
                    - Not everyone who experiences trauma develops PTSD
                    - Effective treatments include trauma-focused psychotherapies and medication
                    """)
                
                elif condition == "Obsessive-Compulsive Disorder":
                    st.markdown("""
                    ### Obsessive-Compulsive Disorder (OCD)
                    
                    OCD is characterized by unreasonable thoughts and fears (obsessions) that lead to repetitive behaviors (compulsions).
                    
                    #### Obsessions
                    - Fear of contamination
                    - Need for symmetry or exactness
                    - Unwanted forbidden or taboo thoughts
                    - Aggressive thoughts towards self or others
                    
                    #### Compulsions
                    - Excessive cleaning or handwashing
                    - Ordering and arranging things in a particular way
                    - Repeatedly checking things
                    - Compulsive counting
                    - Mental compulsions (prayers, counting)
                    
                    #### Facts
                    - OCD affects 2-3% of the population
                    - Usually begins in childhood, adolescence, or early adulthood
                    - Equally common among men and women
                    - Effective treatments include Cognitive Behavioral Therapy (particularly Exposure and Response Prevention) and medication
                    """)
                
                elif condition == "Schizophrenia":
                    st.markdown("""
                    ### Schizophrenia
                    
                    Schizophrenia is a serious mental disorder in which people interpret reality abnormally.
                    
                    #### Symptoms
                    
                    **Positive symptoms (psychotic symptoms)**
                    - Hallucinations
                    - Delusions
                    - Thought disorders
                    - Movement disorders
                    
                    **Negative symptoms (disruptions to normal emotions and behaviors)**
                    - "Flat affect" (reduced expression of emotions)
                    - Reduced feeling of pleasure
                    - Difficulty beginning and sustaining activities
                    - Reduced speaking
                    
                    **Cognitive symptoms**
                    - Problems with working memory
                    - Poor executive functioning
                    - Trouble focusing or paying attention
                    
                    #### Facts
                    - Affects approximately 20 million people worldwide
                    - Typically appears in late adolescence or early adulthood
                    - Slightly more common in males than females
                    - Treatment typically involves a combination of medication, psychotherapy, and coordinated specialty care
                    """)
                
                elif condition == "Eating Disorders":
                    st.markdown("""
                    ### Eating Disorders
                    
                    Eating disorders are serious conditions related to persistent eating behaviors that negatively impact health, emotions, and ability to function.
                    
                    #### Types
                    
                    **Anorexia Nervosa**
                    - Abnormally low body weight
                    - Intense fear of gaining weight
                    - Distorted perception of body weight or shape
                    
                    **Bulimia Nervosa**
                    - Cycles of binging and purging
                    - Feeling out of control during binges
                    - Self-esteem unduly influenced by body shape and weight
                    
                    **Binge Eating Disorder**
                    - Recurrent episodes of eating large quantities of food
                    - Feeling a lack of control during binges
                    - No compensatory behaviors like purging
                    
                    **Other Specified Feeding or Eating Disorders (OSFED)**
                    - Symptoms that don't meet full criteria for other disorders
                    - Equally serious and requiring professional help
                    
                    #### Facts
                    - Eating disorders have the highest mortality rate of any mental illness
                    - Can affect people of any gender, age, race, or background
                    - More common in women and girls
                    - Effective treatment includes psychological therapy, nutritional counseling, and sometimes medication
                    """)
    
    # Tab 3: Treatment Options
    with tabs[2]:
        st.header("Treatment Options for Mental Health Conditions")
        
        st.markdown("""
        Mental health treatment is not one-size-fits-all. Treatment plans should be tailored to individual needs.
        Most people benefit from a combination of treatments.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Psychotherapy (Talk Therapy)")
            
            st.markdown("""
            **Cognitive Behavioral Therapy (CBT)**
            - Focuses on identifying and changing negative thought patterns
            - Helps develop coping strategies for difficult situations
            - Effective for depression, anxiety, PTSD, and more
            
            **Dialectical Behavior Therapy (DBT)**
            - Combines CBT techniques with mindfulness
            - Focuses on emotional regulation and interpersonal effectiveness
            - Often used for borderline personality disorder, suicidal thoughts
            
            **Interpersonal Therapy (IPT)**
            - Focuses on improving interpersonal relationships
            - Addresses social functioning and social support
            - Effective for depression, eating disorders
            
            **Psychodynamic Therapy**
            - Focuses on unconscious processes and past experiences
            - Explores how past affects present behavior
            - Can help with various conditions including depression and anxiety
            
            **Family Therapy**
            - Involves family members in treatment
            - Improves family communication and functioning
            - Useful for conditions affecting the family system
            """)
        
        with col2:
            st.subheader("Medication")
            
            st.markdown("""
            **Antidepressants**
            - Treat depression, anxiety, and some other conditions
            - Types include SSRIs, SNRIs, TCAs, MAOIs
            - May take 2-4 weeks to begin working
            
            **Anti-anxiety Medications**
            - Reduce symptoms of anxiety
            - Include benzodiazepines and buspirone
            - Some are for short-term use only
            
            **Mood Stabilizers**
            - Treat bipolar disorder and mood swings
            - Help prevent manic and depressive episodes
            - Include lithium and anticonvulsants
            
            **Antipsychotics**
            - Treat psychotic symptoms like hallucinations and delusions
            - Used for schizophrenia, bipolar disorder
            - Can be first or second generation
            
            **Stimulants**
            - Treat ADHD
            - Improve focus and reduce impulsivity
            - Include methylphenidate and amphetamine
            """)
        
        st.subheader("Other Treatment Approaches")
        
        approaches = {
            "Brain Stimulation Therapies": """
            - **Electroconvulsive Therapy (ECT)**: Uses electric currents to trigger a brief seizure, changing brain chemistry
            - **Transcranial Magnetic Stimulation (TMS)**: Uses magnetic fields to stimulate nerve cells
            - **Vagus Nerve Stimulation (VNS)**: Uses electrical impulses to stimulate the vagus nerve
            """,
            
            "Complementary and Alternative Medicine": """
            - **Mindfulness and Meditation**: Practices to increase awareness of the present moment
            - **Yoga**: Combines physical postures, breathing exercises, and meditation
            - **Acupuncture**: Traditional Chinese medicine involving insertion of thin needles
            - **Nutritional Approaches**: Dietary changes that may impact mental health
            """,
            
            "Lifestyle Changes": """
            - **Regular Physical Activity**: Reduces symptoms of depression and anxiety
            - **Healthy Sleep Habits**: Improves mood and cognitive function
            - **Stress Management**: Techniques to reduce stress levels
            - **Social Connection**: Building and maintaining supportive relationships
            """,
            
            "Support Groups": """
            - **Peer Support**: Groups led by peers who share similar experiences
            - **Family Support**: Groups for family members of people with mental health conditions
            - **Online Support Communities**: Digital spaces for connection and support
            """,
            
            "Hospitalization and Residential Treatment": """
            - **Inpatient Hospitalization**: 24-hour care in a hospital setting
            - **Partial Hospitalization Programs**: Structured treatment during the day
            - **Residential Treatment**: Long-term care in a residential facility
            """
        }
        
        for approach, description in approaches.items():
            with st.expander(approach):
                st.markdown(description)
        
        st.info("""
        **Important Note**: Always consult with healthcare professionals before starting or changing treatments. 
        This information is educational and not a substitute for professional medical advice.
        """)
    
    # Tab 4: Self-Care Strategies
    with tabs[3]:
        st.header("Self-Care Strategies for Mental Wellbeing")
        
        st.markdown("""
        Self-care is a vital component of maintaining good mental health. While it doesn't replace 
        professional treatment for mental health conditions, it can help support overall wellbeing 
        and can be an important part of a treatment plan.
        """)
        
        st.subheader("Daily Habits for Mental Wellbeing")
        
        habits_cols = st.columns(3)
        
        with habits_cols[0]:
            st.markdown("""
            ### Physical Self-Care
            
            **Regular Physical Activity**
            - Aim for 30 minutes of moderate activity most days
            - Can reduce anxiety and depression symptoms
            - Improves sleep quality and energy levels
            
            **Balanced Nutrition**
            - Eat regular meals with plenty of fruits and vegetables
            - Stay hydrated
            - Limit alcohol and caffeine
            
            **Quality Sleep**
            - Aim for 7-9 hours of sleep per night
            - Maintain a consistent sleep schedule
            - Create a restful environment
            """)
        
        with habits_cols[1]:
            st.markdown("""
            ### Emotional Self-Care
            
            **Stress Management**
            - Practice relaxation techniques
            - Take breaks when needed
            - Set realistic expectations
            
            **Mindfulness and Meditation**
            - Practice being present in the moment
            - Try guided meditations or apps
            - Start with just a few minutes daily
            
            **Emotional Expression**
            - Journal about your feelings
            - Talk to trusted friends or family
            - Consider creative outlets like art or music
            """)
        
        with habits_cols[2]:
            st.markdown("""
            ### Social Self-Care
            
            **Connection**
            - Maintain regular contact with supportive people
            - Join clubs or groups with shared interests
            - Balance social time with alone time
            
            **Boundaries**
            - Learn to say no when necessary
            - Limit time with people who drain your energy
            - Communicate your needs clearly
            
            **Community Involvement**
            - Volunteer for causes you care about
            - Participate in community events
            - Find ways to help others
            """)
        
        st.subheader("Coping Strategies for Difficult Times")
        
        with st.expander("Healthy Coping Mechanisms"):
            st.markdown("""
            **When feeling overwhelmed:**
            - Take slow, deep breaths
            - Use the 5-4-3-2-1 grounding technique: identify 5 things you see, 4 things you feel, 3 things you hear, 2 things you smell, and 1 thing you taste
            - Practice progressive muscle relaxation
            
            **When feeling anxious:**
            - Challenge negative thoughts with evidence
            - Focus on what you can control
            - Engage in a calming activity like walking or gardening
            
            **When feeling depressed:**
            - Break tasks into smaller, manageable steps
            - Schedule activities that normally bring joy
            - Reach out to a supportive person
            
            **When dealing with stress:**
            - Prioritize and delegate tasks
            - Practice time management
            - Take short breaks throughout the day
            """)
        
        with st.expander("Creating a Self-Care Plan"):
            st.markdown("""
            A personalized self-care plan can help you maintain good mental health practices.
            
            **Steps to create your plan:**
            
            1. **Assess your needs**: Identify areas where you're struggling and what helps you feel better
            
            2. **Set specific goals**: Instead of "reduce stress," try "practice meditation for 10 minutes daily"
            
            3. **Schedule self-care activities**: Put them in your calendar like any other important appointment
            
            4. **Identify barriers**: Plan for what might get in the way of your self-care routine
            
            5. **Track your progress**: Note how different activities affect your mood and wellbeing
            
            6. **Adjust as needed**: Your needs will change over time, so your plan should too
            
            **Sample daily self-care checklist:**
            - Physical activity (30 minutes)
            - Nutritious meals (3 balanced meals)
            - Adequate water intake (8 glasses)
            - Mindfulness practice (10 minutes)
            - Connection with others (meaningful conversation)
            - Enjoyable activity (reading, hobby, etc.)
            - Sufficient sleep (7-9 hours)
            """)
        
        with st.expander("Digital Wellbeing"):
            st.markdown("""
            **Managing your digital life for better mental health:**
            
            - **Set boundaries with technology**
              - Designate tech-free times and zones
              - Use app limits or screen time features
              - Take regular breaks from screens
            
            - **Curate your social media**
              - Follow accounts that make you feel good
              - Unfollow or mute content that triggers negative feelings
              - Be mindful of comparison traps
            
            - **Practice digital mindfulness**
              - Be intentional about when and why you use technology
              - Notice how different apps and activities affect your mood
              - Consider periodic digital detoxes
            
            - **Use technology positively**
              - Try mental health apps for meditation, mood tracking, etc.
              - Connect with supportive online communities
              - Learn new skills or information online
            """)
    
    # Tab 5: Supporting Others
    with tabs[4]:
        st.header("Supporting Someone with Mental Health Challenges")
        
        st.markdown("""
        Supporting a friend, family member, or colleague with mental health challenges can make 
        a significant difference in their recovery. Here's how you can help effectively while also 
        taking care of your own wellbeing.
        """)
        
        st.subheader("How to Provide Support")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### Do's
            
            **Learn about their condition**
            - Educate yourself about their specific mental health challenges
            - Understand common symptoms and treatments
            - Know that everyone's experience is unique
            
            **Communicate effectively**
            - Listen without judgment
            - Validate their feelings
            - Ask how you can help
            - Be patient and give them space when needed
            
            **Encourage professional help**
            - Suggest speaking with a mental health professional
            - Offer to help find resources or make appointments
            - Reinforce that seeking help is a sign of strength
            
            **Support their treatment**
            - Encourage them to follow treatment plans
            - Celebrate small victories and progress
            - Be understanding about setbacks
            """)
        
        with col2:
            st.markdown("""
            ### Don'ts
            
            **Avoid dismissing their experience**
            - Don't say things like "just cheer up" or "it's all in your head"
            - Don't minimize their feelings or compare to others
            - Don't make them feel guilty for their condition
            
            **Refrain from taking control**
            - Don't make decisions for them without consent
            - Don't force them into treatment
            - Don't take responsibility for their recovery
            
            **Avoid unhelpful statements**
            - "Everyone feels that way sometimes"
            - "You have so much to be grateful for"
            - "I know exactly how you feel"
            - "You don't look depressed/anxious"
            
            **Don't neglect boundaries**
            - Don't sacrifice your own mental health
            - Don't become their only support system
            - Don't enable unhealthy behaviors
            """)
        
        st.subheader("Supporting in Specific Situations")
        
        situations = {
            "Crisis Situations": """
            **Signs of a mental health crisis:**
            - Talking about wanting to die or kill oneself
            - Looking for ways to kill oneself
            - Extreme mood swings
            - Increased substance use
            - Withdrawing from people and activities
            - Anxiety or agitation
            - Changes in sleep patterns
            
            **How to respond:**
            1. Stay calm and take the situation seriously
            2. Don't leave them alone if you're concerned about their safety
            3. Remove potential means of harm if possible
            4. Call emergency services (911 in the US) or a crisis hotline like 988
            5. Express concern and offer reassurance
            """,
            
            "Supporting a Child or Teen": """
            **Special considerations:**
            - Use age-appropriate language
            - Reassure them that having mental health challenges doesn't mean something is "wrong" with them
            - Maintain routines and structure when possible
            - Involve them in decisions about their care when appropriate
            - Work with their school to ensure proper support
            - Model healthy emotional expression and coping skills
            
            **Warning signs in young people:**
            - Changes in school performance
            - Excessive worry or fear
            - Hyperactivity
            - Frequent nightmares or sleep problems
            - Persistent disobedience or aggression
            - Frequent temper tantrums
            - Withdrawal from friends and activities
            """,
            
            "Supporting a Partner": """
            **Balancing support and self-care:**
            - Maintain open, honest communication
            - Set and respect boundaries
            - Take care of your own mental health
            - Consider couples counseling if the relationship is strained
            - Remember that supporting doesn't mean solving
            
            **Intimacy and mental health:**
            - Be patient with changes in intimacy or affection
            - Discuss needs and limitations openly
            - Separate the person from the condition
            - Find new ways to connect and maintain closeness
            """,
            
            "Supporting at Work": """
            **For colleagues:**
            - Respect privacy and confidentiality
            - Focus on their work performance, not their condition
            - Be flexible and understanding about accommodation needs
            - Include them in social activities but respect if they decline
            
            **For managers:**
            - Know your organization's policies and resources
            - Discuss reasonable accommodations
            - Maintain confidentiality
            - Focus on job performance, not personal details
            - Create a stigma-free work environment
            """,
            
            "Supporting the Elderly": """
            **Special considerations:**
            - Be aware that symptoms may be attributed to aging
            - Pay attention to physical complaints that may signal depression
            - Consider medication interactions
            - Address isolation and loneliness
            - Respect their autonomy while ensuring safety
            
            **Common challenges:**
            - Grief and loss
            - Physical health problems affecting mental health
            - Cognitive changes
            - Reduced independence
            - Limited access to mental health services
            """
        }
        
        for situation, description in situations.items():
            with st.expander(situation):
                st.markdown(description)
        
        st.subheader("Taking Care of Yourself")
        
        st.markdown("""
        Supporting someone with mental health challenges can be emotionally demanding. Remember that you can't pour from an empty cup.
        
        **Self-care strategies for supporters:**
        
        - **Set clear boundaries**
          - Decide what support you can realistically provide
          - Communicate these boundaries clearly
          - Stick to your limits
        
        - **Build your support network**
          - Don't try to be the only source of support
          - Connect with others who are supporting the person
          - Find your own support system
        
        - **Recognize compassion fatigue**
          - Be aware of signs like exhaustion, irritability, and reduced empathy
          - Take breaks when needed
          - Seek professional support if you're struggling
        
        - **Practice regular self-care**
          - Maintain your own mental health practices
          - Continue activities that bring you joy
          - Make time for rest and relaxation
        
        - **Access resources for caregivers**
          - Support groups for family and friends
          - Educational resources about caregiving
          - Professional guidance from therapists or counselors
        """)
        
        st.info("""
        **Remember**: You cannot force someone to get help, but you can offer support and encouragement.
        In emergency situations where someone is at immediate risk of harming themselves or others,
        contact emergency services immediately.
        """)


