# # import sys
# # import os

# # # Add project root to Python path
# # sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))


# # import streamlit as st
# # from PIL import Image
# # #from services.checklist_service import evaluate_image
# # from app.services.checklist_service import evaluate_image

# # st.title("AI Inspection System")

# # uploaded_file = st.file_uploader("Upload Image")

# # if uploaded_file:

# #     image = Image.open(uploaded_file)

# #     st.image(image)

# #     if st.button("Run Inspection"):

# #         result = evaluate_image(image)

# #         st.write("Inspection Result")

# #         st.json(result)
# #-------------------------old script with no css--------------------
# import sys
# import os

# # Add project root to Python path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

# import streamlit as st
# from PIL import Image
# from app.services.checklist_service import evaluate_image


# # ---------------- PAGE CONFIG ----------------

# st.set_page_config(
#     page_title="AI Inspection System",
#     page_icon="🔍",
#     layout="wide"
# )


# # ---------------- CUSTOM STYLE ----------------

# st.markdown("""
# <style>

# .stApp {
#     background-color: #0e1117;
# }

# h1, h2, h3 {
#     color: white;
# }

# div[data-testid="stMetricValue"] {
#     font-size: 30px;
# }

# </style>
# """, unsafe_allow_html=True)


# # ---------------- TITLE ----------------

# st.markdown("""
# # 🔍 AI Inspection System
# ### Automated Visual Inspection using AI
# Upload an image and let AI evaluate cleanliness and arrangement.
# """)


# # ---------------- LAYOUT ----------------

# col1, col2 = st.columns([2,1])

# with col1:

#     uploaded_file = st.file_uploader(
#         "Upload Inspection Image",
#         type=["jpg", "jpeg", "png"]
#     )

#     if uploaded_file:

#         image = Image.open(uploaded_file)

#         st.image(
#             image,
#             caption="Uploaded Image",
#             use_container_width=True
#         )

# with col2:

#     st.subheader("Inspection Panel")

#     run_btn = st.button("🚀 Run Inspection")


# # ---------------- AI INSPECTION ----------------

# if run_btn and uploaded_file:

#     result = evaluate_image(image)

#     st.markdown("## Inspection Results")

#     c1, c2, c3, c4 = st.columns(4)

#     with c1:
#         st.metric("Glass Clean", result["glass_clean"])

#     with c2:
#         st.metric("Floor Clean", result["floor_clean"])

#     with c3:
#         st.metric("Chairs Arranged", result["chairs_arranged"])

#     with c4:
#         st.metric("Room Clean", result["room_clean"])
import sys
import os

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import streamlit as st
from PIL import Image
from app.services.checklist_service import evaluate_image


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="AI Inspection System",
    page_icon="🔍",
    layout="wide"
)


# ---------------- CUSTOM STYLE ----------------

st.markdown("""
<style>

.stApp {
    background-color: #0e1117;
}

h1, h2, h3 {
    color: white;
}

div[data-testid="stMetricValue"] {
    font-size: 30px;
}

</style>
""", unsafe_allow_html=True)


# ---------------- TITLE ----------------

st.markdown("""
# 🔍 AI Inspection System
### Automated Visual Inspection using AI
Upload an image and let AI evaluate cleanliness and arrangement.
""")


# ---------------- LAYOUT ----------------

col1, col2 = st.columns([2,1])

with col1:

    uploaded_file = st.file_uploader(
        "Upload Inspection Image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file:

        image = Image.open(uploaded_file)

        # FIXED LINE (removed use_container_width)
        st.image(
            image,
            caption="Uploaded Image"
        )

with col2:

    st.subheader("Inspection Panel")

    run_btn = st.button("🚀 Run Inspection")


# ---------------- AI INSPECTION ----------------

if run_btn and uploaded_file:

    result = evaluate_image(image)

    st.markdown("## Inspection Results")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("Glass Clean", result["glass_clean"])

    with c2:
        st.metric("Floor Clean", result["floor_clean"])

    with c3:
        st.metric("Chairs Arranged", result["chairs_arranged"])

    with c4:
        st.metric("Room Clean", result["room_clean"])