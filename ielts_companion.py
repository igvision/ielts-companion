import streamlit as st
import time

st.set_page_config(page_title="IELTS Companion", page_icon="📘", layout="centered")

# Main title + your name
st.title("📘 IELTS Companion")
st.markdown("### 👩‍🏫 Teacher Tania Phillips")

st.markdown("Your interactive guide to IELTS basics and practice.")

# Step 1: Choose Test Type
st.header("🏁 Step 1: Choose Your IELTS Test")
test_type = st.radio(
    "Which IELTS test do you need?",
    ["Academic (for university/professional)", "General Training (for work/immigration)"]
)
st.success(f"You selected: {test_type}")

# Step 2: Understand the Format
st.header("📘 Step 2: Understand the Test Format")
with st.expander("See IELTS Format Details"):
    st.markdown("""
    - **Listening**: 4 recordings, 40 questions  
    - **Reading**: 3 passages, 40 questions  
    - **Writing**: 2 tasks (Task 1: report/letter, Task 2: essay)  
    - **Speaking**: 3 parts (introduction, long turn, discussion)  
    """)

# Step 3: Target Score
st.header("🎯 Step 3: Set Your Target Score")
target_score = st.slider("Select your target band score:", 5.0, 9.0, 6.5, 0.5)
st.info(f"Your target score is: Band {target_score}")

# Step 4: Build Core Skills
st.header("📈 Step 4: Build Core Skills")
skills = st.multiselect(
    "Which skills do you want to focus on first?",
    ["Vocabulary", "Grammar", "Reading comprehension", "Listening practice", "Speaking fluency"]
)
if skills:
    st.write("Great choice! You’ll start with:", ", ".join(skills))

# Step 5: Create a Study Plan
st.header("🗓 Step 5: Create a Study Plan")
weeks = st.number_input("How many weeks do you want to prepare?", min_value=1, max_value=52, value=4)
st.write(f"📅 You’ve set a {weeks}-week preparation plan.")

if st.button("Generate Study Roadmap"):
    st.success("Here’s your starter roadmap:")
    st.markdown(f"""
    - **Week 1**: Learn the IELTS format + focus on {skills[0] if skills else "Vocabulary"}  
    - **Week 2**: Practice Listening & Reading with sample tests  
    - **Week 3**: Work on Writing tasks (Task 1 & Task 2)  
    - **Week 4**: Mock Speaking test + full practice exam  
    """)
    st.balloons()

# Practice Quiz Section
st.header("📝 Practice Quiz: IELTS Basics")
question = "How many sections are in IELTS?"
options = ["2", "3", "4", "5"]
answer = st.radio(question, options, key="quiz_q1")

if st.button("Check Answer"):
    if answer == "4":
        st.success("Correct! 🎉 IELTS has 4 sections: Listening, Reading, Writing, Speaking.")
    else:
        st.error("Oops, not quite. IELTS has 4 sections.")

st.markdown("---")
st.caption("© 👩‍🏫 Teacher Tania Phillips — Built with ❤️ using Streamlit")