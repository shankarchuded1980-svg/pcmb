import streamlit as st
import time

# --- PAGE CONFIGURATION & THEME ---
st.set_page_config(
    page_title="Karnataka PU PCMB Smart Portal",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS FOR HIGH UI & ANIMATIONS ---
st.markdown("""
<style>
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .main-container {
        animation: fadeIn 0.6s ease-in-out;
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 10px 20px;
        font-weight: bold;
        border-radius: 8px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        opacity: 0.9;
        transform: scale(1.02);
    }
    .card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        border-left: 5px solid #667eea;
    }
    .auth-box {
        max-width: 450px;
        margin: 50px auto;
        padding: 30px;
        background: #ffffff;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# --- SESSION STATE INITIALIZATION ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "student_name" not in st.session_state:
    st.session_state.student_name = ""
if "mobile_number" not in st.session_state:
    st.session_state.mobile_number = ""

# --- REGISTRATION / LOGIN GATE ---
if not st.session_state.logged_in:
    st.markdown("<div class='auth-box'>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: #4A5568;'>🎓 Karnataka PU PCMB Portal</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #718096;'>Enter your details to access syllabus solutions, formulas, and diagrams.</p>", unsafe_allow_html=True)
    
    with st.form("registration_form"):
        name_input = st.text_input("Full Name", placeholder="e.g., Rahul Kumar")
        college_input = st.text_input("College Name", placeholder="e.g., Govt PU College")
        mobile_input = st.text_input("Mobile Number (+91)", placeholder="9876543210", max_chars=10)
        
        submit_btn = st.form_submit_button("Register & Login")
        
        if submit_btn:
            if len(mobile_input) == 10 and mobile_input.isdigit() and name_input:
                st.session_state.logged_in = True
                st.session_state.student_name = name_input
                st.session_state.mobile_number = mobile_input
                st.success("Login Successful! Loading Portal...")
                time.sleep(1)
                st.rerun()
            else:
                st.error("Please enter a valid Name and a 10-digit Mobile Number.")
    st.markdown("</div>", unsafe_allow_html=True)

else:
    # --- MAIN APPLICATION DASHBOARD ---
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    
    # Sidebar Navigation
    st.sidebar.markdown(f"### Welcome, <b>{st.session_state.student_name}</b> 👋", unsafe_allow_html=True)
    st.sidebar.markdown(f"📱 **Mobile:** +91 {st.session_state.mobile_number}")
    st.sidebar.markdown("---")
    
    puc_year = st.sidebar.selectbox("Select Year", ["1st PUC (Class 11)", "2nd PUC (Class 12)"])
    subject = st.sidebar.selectbox("Select Subject", ["Mathematics", "Physics", "Chemistry", "Biology"])
    
    st.sidebar.markdown("---")
    menu = st.sidebar.radio("Navigation", ["📚 Syllabus & Reduced Topics", "⚡ Formulas & Quick Notes", "💡 Problem Solver & Solutions", "🧬 Diagrams & Concepts"])
    
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

    # --- CONTENT RENDERER ---
    st.title(f"📖 Karnataka PU Board - {puc_year}")
    st.subheader(f"Subject: **{subject}**")
    st.markdown("---")

    # Sample dynamic curriculum database mapping for Karnataka PU Board / NCERT Reduced Syllabus
    if puc_year == "1st PUC (Class 11)":
        if subject == "Mathematics":
            chapters = ["Sets", "Trigonometric Functions", "Complex Numbers", "Linear Inequalities", "Permutations and Combinations", "Binomial Theorem", "Sequences and Series", "Straight Lines", "Conic Sections", "Introduction to 3D Geometry", "Limits and Derivatives", "Statistics", "Probability"]
        elif subject == "Physics":
            chapters = ["Units and Measurements", "Motion in a Straight Line", "Motion in a Plane", "Laws of Motion", "Work, Energy and Power", "System of Particles & Rotational Motion", "Gravitation", "Mechanical Properties of Solids", "Mechanical Properties of Fluids", "Thermal Properties of Matter", "Thermodynamics", "Kinetic Theory", "Oscillations", "Waves"]
        elif subject == "Chemistry":
            chapters = ["Some Basic Concepts of Chemistry", "Structure of Atom", "Classification of Elements & Periodicity", "Chemical Bonding & Molecular Structure", "Chemical Thermodynamics", "Equilibrium", "Redox Reactions", "Organic Chemistry - Some Basic Principles", "Hydrocarbons"]
        else: # Biology
            chapters = ["The Living World", "Biological Classification", "Plant Kingdom", "Animal Kingdom", "Morphology of Flowering Plants", "Anatomy of Flowering Plants", "Structural Organisation in Animals", "Cell: The Unit of Life", "Biomolecules", "Cell Cycle and Division", "Photosynthesis in Higher Plants", "Respiration in Plants", "Plant Growth and Development", "Breathing and Exchange of Gases", "Body Fluids and Circulation", "Excretory Products and Elimination", "Locomotion and Movement", "Neural Control and Coordination", "Chemical Coordination and Integration"]
    else: # 2nd PUC (Class 12)
        if subject == "Mathematics":
            chapters = ["Relations and Functions", "Inverse Trigonometric Functions", "Matrices", "Determinants", "Continuity and Differentiability", "Application of Derivatives", "Integrals", "Application of Integrals", "Differential Equations", "Vector Algebra", "Three Dimensional Geometry", "Linear Programming", "Probability"]
        elif subject == "Physics":
            chapters = ["Electric Charges and Fields", "Electrostatic Potential & Capacitance", "Current Electricity", "Moving Charges and Magnetism", "Magnetism and Matter", "Electromagnetic Induction", "Alternating Current", "Electromagnetic Waves", "Ray Optics and Optical Instruments", "Wave Optics", "Dual Nature of Radiation and Matter", "Atoms", "Nuclei", "Semiconductor Electronics"]
        elif subject == "Chemistry":
            chapters = ["Solutions", "Electrochemistry", "Chemical Kinetics", "The d- and f-Block Elements", "Coordination Compounds", "Haloalkanes and Haloarenes", "Alcohols, Phenols and Ethers", "Aldehydes, Ketones and Carboxylic Acids", "Amines", "Biomolecules"]
        else: # Biology
            chapters = ["Sexual Reproduction in Flowering Plants", "Human Reproduction", "Reproductive Health", "Principles of Inheritance and Variation", "Molecular Basis of Inheritance", "Evolution", "Human Health and Disease", "Microbes in Human Welfare", "Biotechnology: Principles and Processes", "Biotechnology and its Applications", "Organisms and Populations", "Ecosystem", "Biodiversity and Conservation"]

    selected_chapter = st.selectbox("Select Chapter", chapters)

    # Main Screen Content based on Menu Selection
    if menu == "📚 Syllabus & Reduced Topics":
        st.markdown(f"### Chapter: {selected_chapter}")
        st.info("ℹ️ *Aligned with Karnataka PU Board & NCERT Rationalized Content (Dropped topics omitted for board focus).*")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<div class='card'><h4>🎯 Core Concepts Covered</h4><ul><li>Detailed textbook theory as per PU Board guidelines.</li><li>Important derivations and definitions.</li><li>Previous years' board question references.</li></ul></div>", unsafe_allow_html=True)
        with col2:
            st.markdown("<div class='card'><h4>❌ Rationalized / Dropped Topics</h4><ul><li>Topics excluded from the current academic syllabus are filtered out to save preparation time.</li></ul></div>", unsafe_allow_html=True)

    elif menu == "⚡ Formulas & Quick Notes":
        st.markdown(f"### 📝 Key Formulas & Revision Notes: {selected_chapter}")
        st.markdown(f"""
        <div class='card'>
            <h4>Important Highlights for {selected_chapter}</h4>
            <p><b>Core Rule / Theorem:</b> Standard textbook definition and derived formulas applicable for Karnataka PU Annual Examinations.</p>
            <ul>
                <li>Quick shortcut methods for objective and numerical problems.</li>
                <li>Standard units, dimensional formulas (for Physics), and nomenclature rules (for Chemistry).</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    elif menu == "💡 Problem Solver & Solutions":
        st.markdown(f"### 🧮 Textbook Problem Solver: {selected_chapter}")
        problem_type = st.radio("Select Category", ["Solved Textbook Examples", "Exercise Questions", "Important Board Numerical / Derivations"])
        
        st.markdown(f"""
        <div class='card'>
            <h4>Sample Problem from {selected_chapter} ({problem_type})</h4>
            <p><b>Problem Statement:</b> Derive or solve standard textbook problems related to {selected_chapter} following step-by-step evaluation criteria of the Karnataka PU Board scheme of valuation.</p>
            <hr>
            <p><b>Step 1:</b> Identify given parameters and required variables.</p>
            <p><b>Step 2:</b> Apply fundamental formula / reaction mechanism.</p>
            <p><b>Step 3:</b> Substitute values with correct SI units / step calculations.</p>
            <p><b>Final Answer:</b> Obtained with proper units and highlighting.</p>
        </div>
        """, unsafe_allow_html=True)

    elif menu == "🧬 Diagrams & Concepts":
        st.markdown(f"### 📊 Diagrams & Visual Explanations: {selected_chapter}")
        st.markdown(f"""
        <div class='card' style='text-align: center;'>
            <h4>Visual Schematic for {selected_chapter}</h4>
            <p style='color: #718096;'>[Standard Board-Pattern Labelled Diagram / Circuit / Graph Representation]</p>
            <br>
            <div style='background: #edf2f7; padding: 40px; border-radius: 8px; color: #4a5568;'>
                🖼️ Interactive graphical breakdown, anatomy chart, or geometric layout representing key elements of {selected_chapter}.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
