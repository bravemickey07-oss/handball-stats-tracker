import streamlit as st

st.title("Handball Stats Tracker")

playername = "Malek"

# Use session state to keep track of matches and cumulative stats across clicks
if "match_count" not in st.session_state:
    st.session_state.match_count = 0
    st.session_state.total_assists = 0
    st.session_state.total_turnovers = 0

with st.form("stats_form"):
    st.subheader(f"Log Match #{st.session_state.match_count + 1}")
    
    assists = st.number_input("How many assists do you have?", min_value=0, step=1)
    turnovers = st.number_input("How many turnovers did you commit?", min_value=0, step=1)
    shots_taken = st.number_input("How many shots did you take?", min_value=0, step=1)
    goals_scored = st.number_input("How many goals did you score?", min_value=0, step=1)
    
    submitted = st.form_submit_button("Submit Match Stats")

if submitted:
    if shots_taken > 0:
        st.session_state.match_count += 1
        st.session_state.total_assists += assists
        st.session_state.total_turnovers += turnovers
        
        shooting_pct = round((goals_scored / shots_taken) * 100)
        
        st.write(f"**{playername}'s shooting percentage this match:** {shooting_pct}%")[cite: 5]
        
        if shooting_pct > 70:
            st.success("Excellent work")[cite: 5]
        else:
            st.warning("You need to sharpen your aim")[cite: 5]
            
        st.info(f"{playername}'s match count is {st.session_state.match_count}")[cite: 5]
        st.info(f"{playername}'s total assist count is {st.session_state.total_assists}")[cite: 5]
        st.info(f"{playername}'s total turnovers count is {st.session_state.total_turnovers}")[cite: 5]
    else:
        st.error("Shots taken cannot be zero!")
