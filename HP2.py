import streamlit as st
import base64
import os # Import os module to check file existence

# Function to encode image to Base64
def image_to_base64(file_path):
    # Check if the file exists
    if not os.path.exists(file_path):
        st.error(f"Error: Image file not found at {file_path}")
        return None
    try:
        with open(file_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
        # Assuming JPG. If it's PNG, use "image/png"
        return f"data:image/jpeg;base64,{encoded_string}"
    except Exception as e:
        st.error(f"Error reading or encoding image file {file_path}: {e}")
        return None

st.set_page_config(layout="wide")

# --- Get Base64 Data URL for the local image ---
image_file_path = "pyramid.jpg" # Make sure this path is correct relative to where you run the script
bg_image_data_url = image_to_base64(image_file_path)

# --- CSS Styling ---
# Use a raw string literal (r""") and f-string to insert the data URL
# Only apply background if data URL was successfully created
page_style = r"""
<style>
[data-testid="stAppViewContainer"] {{
    {bg_style} /* Placeholder for background style */
}}

/* Optional: Keep container transparency */
/* .main .block-container {{
     background-color: rgba(255, 255, 255, 0.85);
     border-radius: 10px;
     padding: 2rem;
     margin-top: 1rem;
     margin-bottom: 1rem;
}} */

/* Style for the popover trigger text if needed */
/* [data-testid="stPopover"] > button {{
    font-weight: bold;
}} */

/* Style the element containers */
[data-testid="stVerticalBlock"] > [data-testid="stVerticalBlockBorderWrapper"] > div > [data-testid="stVerticalBlock"] > [data-testid="stExpander"] {{
     border: none !important; /* Remove expander border if using st.expander inside */
}}
[data-testid="stVerticalBlock"] > [data-testid="stVerticalBlockBorderWrapper"] > div > [data-testid="stVerticalBlock"] {{
    /* Add background colors to containers */
    padding: 10px; /* Add some padding */
    border-radius: 5px; /* Add rounded corners */
    text-align: center; /* Center text */
    margin: 5px; /* Add margin */
}}

/* Level-specific colors for containers */
.level-4-item [data-testid="stVerticalBlock"] > [data-testid="stVerticalBlockBorderWrapper"] > div > [data-testid="stVerticalBlock"]{{ background-color: rgba(255, 243, 224, 0.8); }}
.level-3-item [data-testid="stVerticalBlock"] > [data-testid="stVerticalBlockBorderWrapper"] > div > [data-testid="stVerticalBlock"]{{ background-color: rgba(255, 235, 238, 0.8); }}
.level-2-item [data-testid="stVerticalBlock"] > [data-testid="stVerticalBlockBorderWrapper"] > div > [data-testid="stVerticalBlock"]{{ background-color: rgba(227, 242, 253, 0.8); }}
.level-1-item [data-testid="stVerticalBlock"] > [data-testid="stVerticalBlockBorderWrapper"] > div > [data-testid="stVerticalBlock"]{{ background-color: rgba(232, 245, 233, 0.8); }}

</style>
""".format(
    # Insert the background style only if the data URL exists
    bg_style=f"""
    background-image: url("{bg_image_data_url}") !important;
    background-size: cover !important;
    background-repeat: no-repeat !important;
    background-attachment: fixed !important;
    background-position: center !important;
    """ if bg_image_data_url else ""
)


st.markdown(page_style, unsafe_allow_html=True)

# --- Apex Title ---
st.markdown("<h1 style='text-align: center; color: #1E88E5; background-color: rgba(255, 255, 255, 0.7); display: inline-block; padding: 5px 10px; border-radius: 5px;'>HAPPINESS AND CONTENTMENT</h1>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True) # Add some space

# --- Define Detail Content (Example) ---
details = {
    "Internal Aspirations": "More detail about finding your purpose, achieving self-fulfillment, and understanding yourself better...",
    "External Aspirations": "Expanded thoughts on contributing to society, acting with kindness, and environmental consciousness...",
    "Core Precept 1": "Details on taking control of your choices, setting healthy boundaries, and the feeling of agency...",
    "Core Precept 2": "Information about accepting yourself and others, understanding limitations, and practicing non-judgment...",
    "Core Precept 3": "Strategies for facing challenges head-on, building resilience, and learning from adversity instead of avoiding it...",
    "Social Connectedness & Relationships": "The importance of strong bonds with family, friends, and community for well-being...",
    "Financial Means & Stability": "How financial security (or lack thereof) impacts stress and opportunities...",
    "Work Purpose & Satisfaction": "Finding meaning and fulfillment in your work or daily activities...",
    "Travel, Leisure, Exploration & Play": "The role of rest, novelty, and fun in a balanced life...",
    "Sleep Quality": "Why good sleep is foundational and tips for improving it...",
    "Diet & Nutrition": "How what you eat affects mood, energy, and overall health...",
    "Exercise & Physical Activity": "The benefits of movement for physical and mental health...",
    "Stress Management & Mindfulness": "Techniques to manage stress and cultivate present-moment awareness...",
    "Health Factors": "Acknowledging the impact of physical health conditions, substance use, etc...",
}

# --- Build Pyramid with Streamlit Widgets ---

# Level 4: Aspirations (2 items)
cols4 = st.columns([1, 2, 2, 1]) # Add spacer columns for centering
with cols4[1]:
    with st.container(border=True):
         st.markdown("<div class='level-4-item'>", unsafe_allow_html=True) # Apply level color class
         popover_title = "Internal Aspirations"
         popover = st.popover(popover_title)
         popover.markdown(f"**{popover_title}**")
         popover.markdown("e.g., Sense of purpose<br>e.g., Self-fulfillment<br>e.g., Self-understanding", unsafe_allow_html=True)
         popover.markdown("---")
         popover.write(details.get(popover_title, "No details available."))
         st.markdown("</div>", unsafe_allow_html=True)

with cols4[2]:
    with st.container(border=True):
         st.markdown("<div class='level-4-item'>", unsafe_allow_html=True) # Apply level color class
         popover_title = "External Aspirations"
         popover = st.popover(popover_title)
         popover.markdown(f"**{popover_title}**")
         popover.markdown("e.g., Social contribution<br>e.g., Kindness & respect<br>e.g., Environmental responsibility", unsafe_allow_html=True)
         popover.markdown("---")
         popover.write(details.get(popover_title, "No details available."))
         st.markdown("</div>", unsafe_allow_html=True)


# Level 3: Core Precepts (3 items)
cols3 = st.columns([0.5, 2, 2, 2, 0.5]) # Add spacer columns
with cols3[1]:
     with st.container(border=True):
         st.markdown("<div class='level-3-item'>", unsafe_allow_html=True)
         popover_title = "Core Precept 1"
         popover = st.popover(popover_title)
         popover.markdown(f"**{popover_title}**")
         popover.markdown("e.g., Personal agency<br>To make choices/changes & to set boundaries", unsafe_allow_html=True)
         popover.markdown("---")
         popover.write(details.get(popover_title, "No details available."))
         st.markdown("</div>", unsafe_allow_html=True)
with cols3[2]:
     with st.container(border=True):
         st.markdown("<div class='level-3-item'>", unsafe_allow_html=True)
         popover_title = "Core Precept 2"
         popover = st.popover(popover_title)
         popover.markdown(f"**{popover_title}**")
         popover.markdown("e.g., Acceptance<br>For self and others, but within defined terms", unsafe_allow_html=True)
         popover.markdown("---")
         popover.write(details.get(popover_title, "No details available."))
         st.markdown("</div>", unsafe_allow_html=True)
with cols3[3]:
     with st.container(border=True):
         st.markdown("<div class='level-3-item'>", unsafe_allow_html=True)
         popover_title = "Core Precept 3"
         popover = st.popover(popover_title)
         popover.markdown(f"**{popover_title}**")
         popover.markdown("e.g., Facing difficulty<br>Facing difficulty and 'turning into' adverse circumstances/situations (i.e. vs avoidance)", unsafe_allow_html=True)
         popover.markdown("---")
         popover.write(details.get(popover_title, "No details available."))
         st.markdown("</div>", unsafe_allow_html=True)

# Level 2: Lifestyle & Environment (4 items)
cols2 = st.columns(4)
level2_items = ["Social Connectedness & Relationships", "Financial Means & Stability", "Work Purpose & Satisfaction", "Travel, Leisure, Exploration & Play"]
level2_desc = ["Family, friends, community", "...", "...", "..."]
for i, col in enumerate(cols2):
    with col:
        with st.container(border=True):
            st.markdown("<div class='level-2-item'>", unsafe_allow_html=True)
            popover_title = level2_items[i]
            popover = st.popover(popover_title)
            popover.markdown(f"**{popover_title}**")
            popover.markdown(level2_desc[i], unsafe_allow_html=True)
            popover.markdown("---")
            popover.write(details.get(popover_title, "No details available."))
            st.markdown("</div>", unsafe_allow_html=True)

# Level 1: Foundational Health (5 items)
cols1 = st.columns(5)
level1_items = ["Sleep Quality", "Diet & Nutrition", "Exercise & Physical Activity", "Stress Management & Mindfulness", "Health Factors"]
level1_desc = ["...", "...", "...", "...", "e.g. Health issues,<br>substance issues etc."]
for i, col in enumerate(cols1):
     with col:
        with st.container(border=True):
            st.markdown("<div class='level-1-item'>", unsafe_allow_html=True)
            popover_title = level1_items[i]
            popover = st.popover(popover_title)
            popover.markdown(f"**{popover_title}**")
            popover.markdown(level1_desc[i], unsafe_allow_html=True)
            popover.markdown("---")
            popover.write(details.get(popover_title, "No details available."))
            st.markdown("</div>", unsafe_allow_html=True)


st.markdown("---")

# Notes (Keep as before)
st.header("Notes")
st.markdown("""
**Note 1:** Dimensions 1 and 2 are the foundational elements for pursuing happiness and contentment. These factors are considered *critical* and need to be established as well as possible prior to exploring and considering dimensions 3 and 4.

**Note 2:** Dimensions 3 and 4 need to be established based on the individual's unique experiences and priorities. The factors included in these dimensions will vary.
""")
