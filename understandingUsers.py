import streamlit as st
import time
import random
from datetime import datetime, date

st.set_page_config(
    page_title="HCI UX Redesign Lab",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=DM+Sans:wght@300;400;500;600&display=swap');

html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #0f0f23;
    border-right: 2px solid #7c3aed;
}
section[data-testid="stSidebar"] * { color: #e2e8f0 !important; }
section[data-testid="stSidebar"] .stRadio label { 
    font-size: 15px; 
    padding: 6px 0;
    cursor: pointer;
}

/* Nav label */
.nav-label {
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #7c3aed !important;
    margin-bottom: 8px;
}

.phase-badge {
    display: inline-block;
    background: #7c3aed;
    color: white;
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    padding: 3px 10px;
    border-radius: 20px;
    letter-spacing: 1px;
    margin-bottom: 12px;
}

/* Cards */
.card {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 24px;
    margin-bottom: 16px;
    box-shadow: 0 1px 4px rgba(0,0,0,0.06);
}

.card-dark {
    background: #1e1e3f;
    border: 1px solid #7c3aed44;
    border-radius: 12px;
    padding: 24px;
    margin-bottom: 16px;
    color: white;
}

/* Section headers */
.section-header {
    font-family: 'Space Mono', monospace;
    font-size: 13px;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #7c3aed;
    margin-bottom: 4px;
}

.big-title {
    font-family: 'DM Sans', sans-serif;
    font-size: 38px;
    font-weight: 600;
    line-height: 1.15;
    color: #0f0f23;
}

/* Violation tags */
.tag-bad {
    display: inline-block;
    background: #fef2f2;
    border: 1px solid #fca5a5;
    color: #dc2626;
    font-size: 12px;
    padding: 2px 10px;
    border-radius: 20px;
    margin: 3px;
    font-family: 'Space Mono', monospace;
}
.tag-good {
    display: inline-block;
    background: #f0fdf4;
    border: 1px solid #86efac;
    color: #16a34a;
    font-size: 12px;
    padding: 2px 10px;
    border-radius: 20px;
    margin: 3px;
    font-family: 'Space Mono', monospace;
}

/* Principle cards */
.principle-box {
    border-left: 4px solid #7c3aed;
    background: #faf5ff;
    padding: 14px 18px;
    border-radius: 0 8px 8px 0;
    margin-bottom: 12px;
}
.principle-name {
    font-weight: 600;
    font-size: 15px;
    color: #5b21b6;
}
.principle-desc {
    font-size: 14px;
    color: #4b5563;
    margin-top: 4px;
}

/* Bad UI styles */
.bad-ui-container {
    background: #c0c0c0;
    border: 3px inset #808080;
    padding: 10px;
    font-family: 'Times New Roman', serif;
}
.bad-button {
    background: #008000;
    color: #ffff00;
    border: 3px outset #00ff00;
    padding: 3px 6px;
    font-size: 9px;
    cursor: pointer;
    margin: 2px;
}
.bad-title {
    color: #ff0000;
    font-size: 24px;
    text-decoration: blink;
    text-align: center;
    font-weight: bold;
}
.bad-text {
    font-size: 9px;
    color: #000080;
    background: #ffff00;
}

/* Good UI styles */
.good-card {
    background: white;
    border-radius: 16px;
    padding: 20px 24px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    margin-bottom: 12px;
    transition: box-shadow 0.2s;
}
.event-category {
    font-size: 11px;
    font-family: 'Space Mono', monospace;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #7c3aed;
    margin-bottom: 6px;
}
.event-title-good {
    font-size: 18px;
    font-weight: 600;
    color: #111827;
    margin-bottom: 4px;
}
.event-meta {
    font-size: 13px;
    color: #6b7280;
}

/* Rubric */
.rubric-row {
    display: flex;
    align-items: center;
    padding: 10px 0;
    border-bottom: 1px solid #f3f4f6;
    gap: 12px;
}
.rubric-pts {
    font-family: 'Space Mono', monospace;
    font-size: 14px;
    color: #7c3aed;
    font-weight: 700;
    min-width: 40px;
}
.rubric-item {
    font-size: 14px;
    color: #374151;
}

/* Feedback box */
.feedback-box {
    background: linear-gradient(135deg, #faf5ff 0%, #ede9fe 100%);
    border: 1px solid #c4b5fd;
    border-radius: 12px;
    padding: 20px 24px;
    font-size: 14px;
    line-height: 1.7;
    color: #3b0764;
}

/* Score tracker */
.score-ring {
    text-align: center;
    padding: 16px;
    background: #0f0f23;
    border-radius: 12px;
    color: white;
}
.score-number {
    font-family: 'Space Mono', monospace;
    font-size: 42px;
    color: #a78bfa;
}
</style>
""", unsafe_allow_html=True)

EVENTS = [
    {"id": 1, "title": "AI & Society Panel", "category": "Academic", "date": "Mar 18, 2026",
     "time": "2:00 PM", "location": "GC 140", "seats": 45, "capacity": 80,
     "description": "Faculty panel on responsible AI development and societal impact."},
    {"id": 2, "title": "Spring Career Fair", "category": "Career", "date": "Mar 20, 2026",
     "time": "10:00 AM", "location": "Wertheim Conservatory", "seats": 12, "capacity": 200,
     "description": "Meet 60+ employers. Bring your résumé. Business casual attire required."},
    {"id": 3, "title": "Python Workshop: Data Viz", "category": "Workshop", "date": "Mar 22, 2026",
     "time": "3:30 PM", "location": "AHC4 320", "seats": 28, "capacity": 30,
     "description": "Hands-on session using Matplotlib and Seaborn. Laptop required."},
    {"id": 4, "title": "Salsa Night @ The Pit", "category": "Social", "date": "Mar 21, 2026",
     "time": "7:00 PM", "location": "GC Pit", "seats": 150, "capacity": 250,
     "description": "Free salsa lessons for beginners, live DJ, and refreshments."},
    {"id": 5, "title": "Hackathon Kickoff", "category": "Workshop", "date": "Mar 23, 2026",
     "time": "9:00 AM", "location": "CASE 241", "seats": 8, "capacity": 60,
     "description": "36-hour hackathon on sustainability tech. Teams of 2-4. Register early!"},
]

HCI_VIOLATIONS = {
    "Poor Color Contrast": "Bright yellow text on grey background fails WCAG AA (ratio < 4.5:1)",
    "Tiny Font Sizes": "9px body text is unreadable — minimum is 16px for body copy",
    "Inconsistent Layout": "No grid or alignment — elements placed arbitrarily",
    "No Visual Hierarchy": "Everything looks the same — no clear path for the eye",
    "Clutter & Noise": "Too many elements compete for attention simultaneously",
    "Missing Affordances": "Buttons don't look clickable; unclear what is interactive",
    "No Feedback": "No confirmation, loading states, or success/error messages",
    "Jargon Overload": "Unexplained abbreviations and insider terminology",
    "Inconsistent Terminology": "Same action called different things in different places",
    "No Empty State": "Blank screen shown when filters return no results",
}

HCI_PRINCIPLES = [
    ("Visibility of System Status", "Always keep users informed about what's happening through feedback."),
    ("Match System & Real World", "Use language and concepts familiar to the user, not system internals."),
    ("User Control & Freedom", "Support undo, redo, and easy exit from unwanted states."),
    ("Consistency & Standards", "Follow platform conventions so users don't have to guess."),
    ("Error Prevention", "Design to prevent problems from occurring in the first place."),
    ("Recognition over Recall", "Minimize memory load — make options visible and choices obvious."),
    ("Flexibility & Efficiency", "Accelerators for experts; simple paths for novices."),
    ("Aesthetic & Minimalist Design", "Don't display irrelevant or rarely needed information."),
    ("Help Users Recover from Errors", "Error messages should be plain-language and constructive."),
    ("Help & Documentation", "Provide concise, searchable docs that focus on the user's task."),
]

if "found_violations" not in st.session_state:
    st.session_state.found_violations = set()
if "ai_feedback" not in st.session_state:
    st.session_state.ai_feedback = None
if "show_good_ui" not in st.session_state:
    st.session_state.show_good_ui = False
if "redesign_choices" not in st.session_state:
    st.session_state.redesign_choices = {}
if "filter_cat" not in st.session_state:
    st.session_state.filter_cat = "All"
if "search_term" not in st.session_state:
    st.session_state.search_term = ""

def _build_urgency_html(style, pct, color, label, seats_left, capacity):
    filled_pct = (1 - pct) * 100
    if style == "Progress bar" or style == "All of the above":
        bar = f"""
        <div style="display:flex; align-items:center; gap:10px; margin-top:8px;">
            <div style="flex:1; background:#f3f4f6; border-radius:4px; height:6px;">
                <div style="width:{filled_pct:.0f}%; background:{color}; height:6px; border-radius:4px;"></div>
            </div>
            <span style="font-size:12px; color:{color}; font-weight:600">{label}</span>
            <span style="font-size:12px; color:#9ca3af">{seats_left} seats left</span>
        </div>"""
        if style != "All of the above":
            return bar
    if style == "Color-coded badge (red/yellow/green)" or style == "All of the above":
        badge = f'<span style="display:inline-block; background:{color}22; border:1px solid {color}; color:{color}; font-size:11px; font-weight:700; padding:2px 10px; border-radius:20px; margin-top:6px;">{label}</span>'
        if style != "All of the above":
            return badge
    if style == "Seats remaining count" or style == "All of the above":
        count = f'<span style="font-size:13px; color:{color}; font-weight:600; margin-top:6px; display:inline-block;">🪑 {seats_left} of {capacity} seats remaining</span>'
        if style != "All of the above":
            return count
    if style == "Percentage display":
        return f'<span style="font-size:13px; color:{color}; font-weight:600; margin-top:6px; display:inline-block;">{filled_pct:.0f}% full</span>'
    # All of the above — combine everything
    return f"""
    <div style="margin-top:8px;">
        <div style="display:flex; align-items:center; gap:10px; margin-bottom:4px;">
            <div style="flex:1; background:#f3f4f6; border-radius:4px; height:6px;">
                <div style="width:{filled_pct:.0f}%; background:{color}; height:6px; border-radius:4px;"></div>
            </div>
            <span style="font-size:12px; color:{color}; font-weight:600">{label}</span>
        </div>
        <span style="display:inline-block; background:{color}22; border:1px solid {color}; color:{color}; font-size:11px; font-weight:700; padding:2px 10px; border-radius:20px; margin-right:8px;">{label}</span>
        <span style="font-size:12px; color:#9ca3af;">🪑 {seats_left} / {capacity} &nbsp; {filled_pct:.0f}% full</span>
    </div>"""

with st.sidebar:
    st.markdown('<div class="nav-label">HCI Lab Module</div>', unsafe_allow_html=True)
    st.markdown("### 🎨 UX Redesign Challenge")
    st.markdown("### 👨‍💻 Prof. Gregory Reis")
    st.markdown("---")
    page = st.radio(
        "Navigate",
        ["📋 Activity Overview", "💀 The Bad UI", "🔍 Violation Hunt",
         "📐 HCI Principles", "🛠️ Your Redesign", "✅ Evaluation & Rubric"],
        label_visibility="collapsed"
    )
    st.markdown("---")
    score = len(st.session_state.found_violations)
    st.markdown(f"""
    <div class="score-ring">
        <div style="font-size:11px; letter-spacing:2px; color:#94a3b8; margin-bottom:4px;">VIOLATIONS FOUND</div>
        <div class="score-number">{score}<span style="font-size:20px; color:#6d28d9;">/{len(HCI_VIOLATIONS)}</span></div>
        <div style="font-size:12px; color:#94a3b8; margin-top:4px;">Phase 2 progress</div>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
#  PAGE 1 — Activity Overview
# ══════════════════════════════════════════════════════════════════════════════
if page == "📋 Activity Overview":
    st.markdown('<div class="section-header">HCI Lab · Spring 2026 · Prof. Gregory Reis · March 12th 2026</div>', unsafe_allow_html=True)
    st.markdown('<div class="big-title">The UX Redesign Challenge</div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    for col, (icon, label, val) in zip(
        [col1, col2, col3, col4],
        [("⏱️","Duration","45 min"), ("👥","Team Size","2–3 students"),
         ("💯","Points","100 pts"), ("🛠️","Tool","Streamlit + Python")]
    ):
        with col:
            st.metric(label, val, label_visibility="visible")

    st.markdown("---")

    col_a, col_b = st.columns([3, 2])
    with col_a:
        st.markdown("""
        ### What You'll Do
        You're a UX consultant hired to rescue a **Campus Event Finder** app that has 
        somehow made it to production with terrible UX. Your job:

        1. **Explore** the broken UI and feel the pain firsthand  
        2. **Identify** specific HCI violations and explain *why* they're problems  
        3. **Study** Nielsen's 10 Usability Heuristics  
        4. **Redesign** the UI using Streamlit's built-in components  
        5. **Justify** every design decision using HCI principles  
        6. **Reflect** on the tradeoffs you made  

        > 💡 **Optional extension**: Use the Claude AI feedback tool to get automated 
        > UX critique of your redesign rationale.
        """)

    with col_b:
        st.markdown("""
        <div class="card-dark">
        <div style="font-family:'Space Mono',monospace; font-size:11px; letter-spacing:2px; color:#a78bfa;">LEARNING OBJECTIVES</div>
        <br>
        ✦ Apply Nielsen's heuristics to real UI<br><br>
        ✦ Identify contrast, hierarchy, and affordance failures<br><br>
        ✦ Implement accessible, usable Streamlit layouts<br><br>
        ✦ Articulate design decisions with HCI vocabulary<br><br>
        ✦ Practice iterative UI evaluation
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### Activity Flow")
    phases = [
        ("1", "Explore Bad UI", "Navigate the broken Campus Event Finder. Note your frustrations.", "💀"),
        ("2", "Violation Hunt", "Check off HCI violations you find. Earn points for each!", "🔍"),
        ("3", "Study Principles", "Review the 10 heuristics before redesigning.", "📐"),
        ("4", "Redesign", "Build the improved UI right here in Streamlit.", "🛠️"),
        ("5", "Evaluate", "Score yourself and use AI feedback if desired.", "✅"),
    ]
    cols = st.columns(5)
    for col, (num, title, desc, icon) in zip(cols, phases):
        with col:
            st.markdown(f"""
            <div class="card" style="text-align:center; min-height:160px;">
                <div style="font-size:28px">{icon}</div>
                <div style="font-family:'Space Mono',monospace; font-size:11px; color:#7c3aed; letter-spacing:1px;">PHASE {num}</div>
                <div style="font-weight:600; margin: 6px 0 8px">{title}</div>
                <div style="font-size:12px; color:#6b7280">{desc}</div>
            </div>
            """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
#  PAGE 2 — The Bad UI
# ══════════════════════════════════════════════════════════════════════════════
elif page == "💀 The Bad UI":
    st.markdown('<div class="phase-badge">PHASE 1 · Explore the Disaster</div>', unsafe_allow_html=True)
    st.markdown("## 💀 The Bad UI")
    st.warning("⚠️ This UI is intentionally terrible. Feel the frustration — then articulate *why* it's bad.")

    st.markdown("""
    <div class="bad-ui-container">
        <div class="bad-title">⚡ FIU EVT FINDER SYSTM v1.0 ⚡</div>
        <hr style="border-color: navy;">
        <marquee style="color:blue; font-size:8px;">WELCOME TO THE FIU EVENT FINDER SYSTEM PLEASE READ ALL INSTRUCTIONS CAREFULLY BEFORE PROCEEDING</marquee>
        <br>
        <table border="1" width="100%" style="font-size:9px; border-collapse:collapse;">
            <tr style="background:#000080; color:yellow;">
                <td><b>EVT_ID</b></td>
                <td><b>EVT_NM</b></td>
                <td><b>CAT_CD</b></td>
                <td><b>DT_TM</b></td>
                <td><b>LOC_CD</b></td>
                <td><b>AVL_CAP</b></td>
                <td><b>ACT</b></td>
            </tr>
            <tr style="background:#ffff00;">
                <td class="bad-text">001</td>
                <td class="bad-text">AI & Society Panel PLEASE NOTE THIS EVENT HAS LIMITED SEATING AND IS FOR GRADUATE STUDENTS ONLY BUT UNDERGRADS MAY ATTEND IF SPACE AVAILABLE</td>
                <td class="bad-text">ACDMC</td>
                <td class="bad-text">03182026@1400HRS</td>
                <td class="bad-text">GC-BLD-RM140</td>
                <td class="bad-text">45/80</td>
                <td><button class="bad-button" onclick="">REG_PROC_INIT</button></td>
            </tr>
            <tr style="background:#c0c0c0;">
                <td class="bad-text">002</td>
                <td class="bad-text">Spring Career Fair</td>
                <td class="bad-text">CR_FR</td>
                <td class="bad-text">03202026@1000HRS</td>
                <td class="bad-text">WRTHM-CNSRV</td>
                <td class="bad-text">12/200</td>
                <td><button class="bad-button">REG_PROC_INIT</button></td>
            </tr>
            <tr style="background:#ffff00;">
                <td class="bad-text">003</td>
                <td class="bad-text">Python Workshop: Data Viz</td>
                <td class="bad-text">WRKSHP</td>
                <td class="bad-text">03222026@1530HRS</td>
                <td class="bad-text">AHC4-RM320</td>
                <td class="bad-text">28/30</td>
                <td><button class="bad-button">REG_PROC_INIT</button></td>
            </tr>
            <tr style="background:#c0c0c0;">
                <td class="bad-text">004</td>
                <td class="bad-text">Salsa Night @ The Pit</td>
                <td class="bad-text">SOC</td>
                <td class="bad-text">03212026@1900HRS</td>
                <td class="bad-text">GC-PIT-AREA</td>
                <td class="bad-text">150/250</td>
                <td><button class="bad-button">REG_PROC_INIT</button></td>
            </tr>
            <tr style="background:#ffff00;">
                <td class="bad-text">005</td>
                <td class="bad-text">Hackathon Kickoff</td>
                <td class="bad-text">WRKSHP</td>
                <td class="bad-text">03232026@0900HRS</td>
                <td class="bad-text">CASE-BLD-241</td>
                <td class="bad-text">8/60</td>
                <td><button class="bad-button">REG_PROC_INIT</button></td>
            </tr>
        </table>
        <br>
        <table width="100%">
            <tr>
                <td><button class="bad-button">FILTER_CAT_ACDMC</button></td>
                <td><button class="bad-button">FILTER_CAT_CR_FR</button></td>
                <td><button class="bad-button">FILTER_CAT_WRKSHP</button></td>
                <td><button class="bad-button">FILTER_CAT_SOC</button></td>
                <td><button class="bad-button" style="background:red; color:white;">CLR_ALL_FLTRS</button></td>
            </tr>
        </table>
        <br>
        <div style="font-size:7px; color:#333; background: #eee; padding: 4px;">
            NOTICE: This system is for authorized FIU personnel and students only. Unauthorized use is prohibited.
            System last updated: UNKNOWN. For technical support contact: IT_HELP_DESK_MAIN_OFFICE_BLDG_PC_316.
            © 1997 FIU Information Technology Services. All rights reserved. Some rights reserved. 
            Use of this system constitutes agreement to all terms. See page 47 of the student handbook.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 📝 Quick Reflection")
    st.text_area(
        "In 2–3 sentences, describe how this UI made you feel as a user. What was your first instinct?",
        placeholder="e.g., I immediately felt overwhelmed by the color contrast and couldn't figure out what 'REG_PROC_INIT' meant...",
        height=100,
        key="bad_ui_reflection"
    )
    st.caption("Save this reflection — you'll reference it in Phase 5.")


# ══════════════════════════════════════════════════════════════════════════════
#  PAGE 3 — Violation Hunt
# ══════════════════════════════════════════════════════════════════════════════
elif page == "🔍 Violation Hunt":
    st.markdown('<div class="phase-badge">PHASE 2 · Identify Problems</div>', unsafe_allow_html=True)
    st.markdown("## 🔍 Violation Hunt")
    st.markdown("Check each UX violation you spotted in the Bad UI. For each one, write **why** it matters.")

    found = st.session_state.found_violations

    for violation, explanation in HCI_VIOLATIONS.items():
        col1, col2 = st.columns([0.05, 0.95])
        with col1:
            checked = st.checkbox("", key=f"v_{violation}", value=(violation in found))
        with col2:
            if checked:
                found.add(violation)
                st.markdown(f'<span class="tag-bad">{violation}</span> ✓', unsafe_allow_html=True)
                st.caption(f"*Expert note: {explanation}*")
                st.text_input(
                    f"Why is this a problem? (your words)",
                    key=f"explain_{violation}",
                    placeholder="e.g., I couldn't read the text because..."
                )
            else:
                found.discard(violation)
                st.markdown(f'<span style="color:#9ca3af">{violation}</span>', unsafe_allow_html=True)

    st.session_state.found_violations = found

    st.markdown("---")
    total = len(found)
    st.markdown(f"**You've identified {total}/{len(HCI_VIOLATIONS)} violations.**")
    if total == len(HCI_VIOLATIONS):
        st.success("🎉 You found them all! Expert UX analyst eyes.")
    elif total >= 7:
        st.info("👍 Great coverage — you have a strong eye for UX problems.")
    elif total >= 4:
        st.warning("👀 Keep looking — there are more issues to find!")
    else:
        st.error("💡 Tip: Look carefully at colors, fonts, labels, and button text in the Bad UI.")

    st.markdown("### 💬 Were there violations NOT on this list?")
    st.text_area(
        "If you noticed other HCI problems, describe them here:",
        placeholder="e.g., The page title doesn't describe what the app does...",
        height=80,
        key="extra_violations"
    )


# ══════════════════════════════════════════════════════════════════════════════
#  PAGE 4 — HCI Principles
# ══════════════════════════════════════════════════════════════════════════════
elif page == "📐 HCI Principles":
    st.markdown('<div class="phase-badge">PHASE 3 · Study Before Building</div>', unsafe_allow_html=True)
    st.markdown("## 📐 Nielsen's 10 Usability Heuristics")
    st.markdown("Study each principle. In the redesign phase, you'll select which heuristics each of your decisions addresses.")

    for i, (name, desc) in enumerate(HCI_PRINCIPLES, 1):
        with st.expander(f"#{i} — {name}"):
            st.markdown(f"""
            <div class="principle-box">
                <div class="principle-name">{name}</div>
                <div class="principle-desc">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

            # Quick check: how does this apply to the bad UI?
            examples = {
                "Visibility of System Status": "The bad UI shows '45/80' but gives no visual indicator of urgency. Almost-full events look the same as empty ones.",
                "Match System & Real World": "'REG_PROC_INIT' and 'ACDMC' are system codes — not human language.",
                "User Control & Freedom": "There's no way to undo a registration, and the 'CLR_ALL_FLTRS' button is placed randomly.",
                "Consistency & Standards": "Filter buttons look completely different from action buttons. No visual system.",
                "Error Prevention": "No confirmation dialog before registering. No warning when an event is almost full.",
                "Recognition over Recall": "Column headers use codes (EVT_ID, CAT_CD) that users must memorize.",
                "Flexibility & Efficiency": "No search, no sort, no shortcuts. One mode for all users.",
                "Aesthetic & Minimalist Design": "Legal disclaimers, marquee text, and 7px copyright notices clutter everything.",
                "Help Users Recover from Errors": "No error messages exist — clicking register either works or silently fails.",
                "Help & Documentation": "Help link points to a building room number, not actual documentation.",
            }
            if name in examples:
                st.markdown(f"**Bad UI example:** *{examples[name]}*")
                st.markdown("**Your fix?**")
                st.text_input("How will you address this in your redesign?", key=f"fix_{i}", placeholder="I will...")

    st.markdown("---")
    st.markdown("### 🎯 Which 3 heuristics matter MOST for an event finder app?")
    top3 = st.multiselect(
        "Select your top 3:",
        [name for name, _ in HCI_PRINCIPLES],
        max_selections=3,
        key="top3_heuristics"
    )
    if top3:
        st.text_area("Explain your ranking:", key="ranking_reason", height=80,
                     placeholder="I chose these because...")


# ══════════════════════════════════════════════════════════════════════════════
#  PAGE 5 — Your Redesign
# ══════════════════════════════════════════════════════════════════════════════
elif page == "🛠️ Your Redesign":
    st.markdown('<div class="phase-badge">PHASE 4 · Build the Better UI</div>', unsafe_allow_html=True)
    st.markdown("## 🛠️ Your Redesign")

    tab1, tab2, tab3 = st.tabs(["🎯 Design Decisions", "📱 Live Redesign Preview", "🤖 AI UX Feedback"])

    # ── Tab 1: Design Decisions ──────────────────────────────────────────────
    with tab1:
        st.markdown("Document your design choices **before** building. This is your design rationale.")
        st.markdown("---")

        choices = st.session_state.redesign_choices

        st.markdown("**1. Color Palette**")
        col1, col2 = st.columns(2)
        with col1:
            primary = st.color_picker("Primary color", value="#7c3aed", key="color_primary")
            secondary = st.color_picker("Accent/action color", value="#10b981", key="color_secondary")
        with col2:
            st.text_area("Why these colors? (contrast ratio, brand, emotion)",
                         key="color_rationale", height=80,
                         placeholder="I chose these because they meet WCAG AA contrast standards and...")

        st.markdown("**2. Layout Approach**")
        layout_choice = st.radio("How will you display events?",
                                 ["Cards in a single column", "Cards in a grid", "List with expandable rows", "Tabbed by category"],
                                 key="layout_choice")
        st.text_input("Heuristic this addresses:", key="layout_heuristic",
                      placeholder="e.g., Aesthetic & Minimalist Design — because...")

        st.markdown("**3. Search & Filter**")
        filter_choices = st.multiselect("Which filter mechanisms will you include?",
                                        ["Text search", "Category buttons", "Date range picker", "Availability toggle", "Sort dropdown"],
                                        key="filter_choices")
        st.text_input("Why these? What UX problem do they solve?", key="filter_rationale")

        st.markdown("**4. Urgency & Status**")
        urgency = st.selectbox("How will you show nearly-full events?",
                               ["Progress bar", "Color-coded badge (red/yellow/green)", "Seats remaining count", "Percentage display", "All of the above"],
                               key="urgency_choice")
        st.text_input("Which heuristic does this address?", key="urgency_heuristic",
                      placeholder="e.g., Visibility of System Status")

        st.markdown("**5. Button & Action Labels**")
        btn_label = st.text_input("What will your registration button say?",
                                  value="Register for Event", key="btn_label",
                                  placeholder="Not 'REG_PROC_INIT'!")
        st.text_area("Why? What makes a good action label?", key="btn_rationale", height=60)

        st.markdown("**6. Accessibility Consideration**")
        a11y = st.multiselect("What accessibility features will you include?",
                              ["High contrast colors (WCAG AA)", "Minimum 16px body font",
                               "Descriptive alt text", "Keyboard navigable",
                               "Screen reader labels", "No color as sole indicator"],
                              key="a11y_choices")

        choices.update({
            "primary_color": primary,
            "layout": layout_choice,
            "filters": filter_choices,
            "urgency": urgency,
            "btn_label": btn_label,
            "accessibility": a11y
        })
        st.session_state.redesign_choices = choices

    # ── Tab 2: Live Redesign Preview ─────────────────────────────────────────
    with tab2:

        # ── Read student's design decisions from session state ────────────────
        primary_color  = st.session_state.get("color_primary",  "#7c3aed")
        secondary_color= st.session_state.get("color_secondary","#10b981")
        layout_mode    = st.session_state.get("layout_choice",  "Cards in a single column")
        filter_choices = st.session_state.get("filter_choices", [])
        urgency_style  = st.session_state.get("urgency_choice", "Progress bar")
        btn_label_val  = st.session_state.get("btn_label",      "Register for Event") or "Register for Event"
        show_text_search   = not filter_choices or "Text search"         in filter_choices
        show_cat_filter    = not filter_choices or "Category buttons"    in filter_choices
        show_avail_toggle  = not filter_choices or "Availability toggle" in filter_choices
        show_sort          = not filter_choices or "Sort dropdown"       in filter_choices

        # ── Live preview header with student's chosen primary color ──────────
        st.markdown(f"""
        <div style="background:{primary_color}; padding:16px 24px; border-radius:12px; margin-bottom:20px;">
            <div style="font-family:'Space Mono',monospace; font-size:11px; letter-spacing:3px; color:rgba(255,255,255,0.7);">CAMPUS EVENTS</div>
            <div style="font-size:24px; font-weight:700; color:white; margin-top:4px;">Find Your Next Event</div>
        </div>
        """, unsafe_allow_html=True)

        # ── Filter controls — shown/hidden based on student's choices ─────────
        active_filters_count = sum([show_text_search, show_cat_filter, show_avail_toggle, show_sort])
        if active_filters_count == 0:
            st.info("💡 No filter mechanisms selected yet — go to **Design Decisions** and pick some under #3 Search & Filter.")

        col_s, col_f, col_sort = st.columns([3, 2, 2])
        search = ""
        cat_filter = "All"
        sort_by = "Date"
        if show_text_search:
            with col_s:
                search = st.text_input("🔍 Search events", placeholder="e.g., Python, career, social…",
                                       key="redesign_search")
        if show_cat_filter:
            with col_f:
                categories = ["All"] + sorted(set(e["category"] for e in EVENTS))
                cat_filter = st.selectbox("Category", categories, key="redesign_cat")
        if show_sort:
            with col_sort:
                sort_by = st.selectbox("Sort by", ["Date", "Seats Available", "Category"], key="redesign_sort")

        show_available = False
        if show_avail_toggle:
            show_available = st.toggle("Show only events with available seats", value=False)

        # ── Filter + sort events ───────────────────────────────────────────────
        filtered = list(EVENTS)
        if search:
            filtered = [e for e in filtered if search.lower() in e["title"].lower() or
                        search.lower() in e["description"].lower()]
        if cat_filter != "All":
            filtered = [e for e in filtered if e["category"] == cat_filter]
        if show_available:
            filtered = [e for e in filtered if e["seats"] > 0]
        if sort_by == "Seats Available":
            filtered = sorted(filtered, key=lambda e: e["seats"], reverse=True)
        elif sort_by == "Category":
            filtered = sorted(filtered, key=lambda e: e["category"])

        st.markdown(f"**{len(filtered)} event{'s' if len(filtered) != 1 else ''} found**")
        st.markdown("---")

        # ── Empty state ────────────────────────────────────────────────────────
        if not filtered:
            st.markdown(f"""
            <div style="text-align:center; padding:60px 20px; color:#9ca3af;">
                <div style="font-size:48px">🔎</div>
                <div style="font-size:18px; font-weight:600; margin:12px 0; color:#374151">No events match your search</div>
                <div style="font-size:14px">Try clearing your filters or searching for a different term.</div>
            </div>
            """, unsafe_allow_html=True)

        # ── GRID layout ────────────────────────────────────────────────────────
        elif layout_mode == "Cards in a grid":
            rows = [filtered[i:i+2] for i in range(0, len(filtered), 2)]
            for row in rows:
                cols_grid = st.columns(2)
                for col_g, event in zip(cols_grid, row):
                    with col_g:
                        seats_left = event["seats"]
                        capacity   = event["capacity"]
                        pct        = seats_left / capacity
                        urgency_color = "#ef4444" if pct < 0.15 else "#f59e0b" if pct < 0.4 else secondary_color
                        urgency_label = "Almost Full" if pct < 0.15 else "Filling Up" if pct < 0.4 else "Available"

                        urgency_html = _build_urgency_html(urgency_style, pct, urgency_color, urgency_label, seats_left, capacity)

                        st.markdown(f"""
                        <div class="good-card" style="border-top:4px solid {primary_color};">
                            <div style="font-size:11px; font-family:'Space Mono',monospace; letter-spacing:2px; color:{primary_color}; margin-bottom:6px;">{event["category"].upper()}</div>
                            <div style="font-size:17px; font-weight:600; color:#111827; margin-bottom:4px;">{event["title"]}</div>
                            <div style="font-size:12px; color:#6b7280; margin-bottom:8px;">
                                📅 {event["date"]} &nbsp;·&nbsp; 🕑 {event["time"]}<br>📍 {event["location"]}
                            </div>
                            <div style="font-size:13px; color:#4b5563; margin-bottom:10px;">{event["description"]}</div>
                            {urgency_html}
                        </div>
                        """, unsafe_allow_html=True)
                        if seats_left > 0:
                            if st.button(btn_label_val, key=f"reg_{event['id']}", use_container_width=True):
                                st.success(f"✅ Registered for **{event['title']}**!")
                        else:
                            st.button("Join Waitlist", key=f"wait_{event['id']}", use_container_width=True)

        # ── EXPANDABLE LIST layout ─────────────────────────────────────────────
        elif layout_mode == "List with expandable rows":
            for event in filtered:
                seats_left = event["seats"]
                capacity   = event["capacity"]
                pct        = seats_left / capacity
                urgency_color = "#ef4444" if pct < 0.15 else "#f59e0b" if pct < 0.4 else secondary_color
                urgency_label = "Almost Full" if pct < 0.15 else "Filling Up" if pct < 0.4 else "Available"
                with st.expander(f"**{event['title']}** · {event['date']} · {event['time']} · *{urgency_label}*"):
                    col_d, col_a = st.columns([3, 1])
                    with col_d:
                        st.markdown(f"📍 **{event['location']}**")
                        st.markdown(event["description"])
                        urgency_html = _build_urgency_html(urgency_style, pct, urgency_color, urgency_label, seats_left, capacity)
                        st.markdown(urgency_html, unsafe_allow_html=True)
                    with col_a:
                        if seats_left > 0:
                            if st.button(btn_label_val, key=f"reg_{event['id']}", use_container_width=True):
                                st.success(f"✅ Registered for **{event['title']}**!")
                        else:
                            st.button("Join Waitlist", key=f"wait_{event['id']}", use_container_width=True)

        # ── TABBED BY CATEGORY layout ──────────────────────────────────────────
        elif layout_mode == "Tabbed by category":
            all_cats = sorted(set(e["category"] for e in filtered))
            if not all_cats:
                st.info("No events to show.")
            else:
                cat_tabs = st.tabs(all_cats)
                for cat_tab, cat_name in zip(cat_tabs, all_cats):
                    with cat_tab:
                        cat_events = [e for e in filtered if e["category"] == cat_name]
                        for event in cat_events:
                            seats_left = event["seats"]
                            capacity   = event["capacity"]
                            pct        = seats_left / capacity
                            urgency_color = "#ef4444" if pct < 0.15 else "#f59e0b" if pct < 0.4 else secondary_color
                            urgency_label = "Almost Full" if pct < 0.15 else "Filling Up" if pct < 0.4 else "Available"
                            urgency_html  = _build_urgency_html(urgency_style, pct, urgency_color, urgency_label, seats_left, capacity)
                            col_ev, col_ac = st.columns([4, 1])
                            with col_ev:
                                st.markdown(f"""
                                <div class="good-card">
                                    <div style="font-size:17px; font-weight:600; color:#111827; margin-bottom:4px;">{event["title"]}</div>
                                    <div style="font-size:13px; color:#6b7280; margin-bottom:6px;">📅 {event["date"]} &nbsp;·&nbsp; 🕑 {event["time"]} &nbsp;·&nbsp; 📍 {event["location"]}</div>
                                    <div style="font-size:13px; color:#4b5563; margin-bottom:8px;">{event["description"]}</div>
                                    {urgency_html}
                                </div>
                                """, unsafe_allow_html=True)
                            with col_ac:
                                st.markdown("<br><br><br>", unsafe_allow_html=True)
                                if seats_left > 0:
                                    if st.button(btn_label_val, key=f"reg_{event['id']}", use_container_width=True):
                                        st.success(f"✅ Registered for **{event['title']}**!")
                                else:
                                    st.button("Join Waitlist", key=f"wait_{event['id']}", use_container_width=True)

        # ── DEFAULT: Single column cards ───────────────────────────────────────
        else:
            for event in filtered:
                seats_left = event["seats"]
                capacity   = event["capacity"]
                pct        = seats_left / capacity
                urgency_color = "#ef4444" if pct < 0.15 else "#f59e0b" if pct < 0.4 else secondary_color
                urgency_label = "Almost Full" if pct < 0.15 else "Filling Up" if pct < 0.4 else "Available"
                urgency_html  = _build_urgency_html(urgency_style, pct, urgency_color, urgency_label, seats_left, capacity)

                col_event, col_action = st.columns([4, 1])
                with col_event:
                    st.markdown(f"""
                    <div class="good-card">
                        <div style="font-size:11px; font-family:'Space Mono',monospace; letter-spacing:2px; color:{primary_color}; margin-bottom:6px;">{event["category"].upper()}</div>
                        <div style="font-size:18px; font-weight:600; color:#111827; margin-bottom:4px;">{event["title"]}</div>
                        <div style="font-size:13px; color:#6b7280; margin-bottom:8px;">
                            📅 {event["date"]} &nbsp;·&nbsp; 🕑 {event["time"]} &nbsp;·&nbsp; 📍 {event["location"]}
                        </div>
                        <div style="font-size:13px; color:#4b5563; margin-bottom:10px;">{event["description"]}</div>
                        {urgency_html}
                    </div>
                    """, unsafe_allow_html=True)
                with col_action:
                    st.markdown("<br><br><br>", unsafe_allow_html=True)
                    if seats_left > 0:
                        if st.button(btn_label_val, key=f"reg_{event['id']}", use_container_width=True):
                            st.success(f"✅ Registered for **{event['title']}**!")
                    else:
                        st.button("Join Waitlist", key=f"wait_{event['id']}", use_container_width=True)

        # ── Design decision summary callout ───────────────────────────────────
        st.markdown("---")
        decisions_made = [
            ("Primary color", primary_color),
            ("Layout", layout_mode),
            ("Filters active", ", ".join(filter_choices) if filter_choices else "none selected"),
            ("Urgency style", urgency_style),
            ("Button label", btn_label_val),
        ]
        st.markdown("### 🔎 Your Active Design Decisions")
        st.caption("← Change these in the **Design Decisions** tab and come back to see the preview update live.")
        cols_dec = st.columns(len(decisions_made))
        for col_d, (label, val) in zip(cols_dec, decisions_made):
            with col_d:
                if label == "Primary color":
                    st.markdown(f"""<div style="background:{val}; width:100%; height:8px; border-radius:4px; margin-bottom:4px;"></div>""", unsafe_allow_html=True)
                st.markdown(f"**{label}**")
                st.caption(val)

    # ── Tab 3: AI Feedback ───────────────────────────────────────────────────
    with tab3:
        st.markdown("### 🤖 AI UX Feedback (Optional)")
        st.info("Get Claude AI to critique your design rationale. You'll need an Anthropic API key.")

        api_key = st.text_input("Anthropic API Key", type="password",
                                placeholder="sk-ant-...", key="api_key_input")

        choices = st.session_state.redesign_choices

        if st.button("Get AI Feedback on My Redesign", type="primary"):
            if not api_key:
                st.warning("Enter your API key above to use AI feedback.")
            else:
                rationale_summary = f"""
                Student's UX Redesign Choices:
                - Layout: {choices.get('layout', 'not specified')}
                - Filters: {', '.join(choices.get('filters', [])) or 'not specified'}
                - Urgency indicator: {choices.get('urgency', 'not specified')}
                - Button label: {choices.get('btn_label', 'not specified')}
                - Accessibility: {', '.join(choices.get('accessibility', [])) or 'not specified'}
                """

                with st.spinner("Claude is reviewing your UX decisions..."):
                    try:
                        import urllib.request, json as _json
                        payload = _json.dumps({
                            "model": "claude-sonnet-4-20250514",
                            "max_tokens": 600,
                            "messages": [{
                                "role": "user",
                                "content": f"""You are a senior UX designer reviewing a student's redesign of a university event finder app.

The original app had these HCI violations: poor color contrast, 9px fonts, jargon labels like 'REG_PROC_INIT', 
no visual hierarchy, no empty states, no affordance cues.

The student's redesign choices:
{rationale_summary}

Give constructive feedback in 4 parts:
1. **What they got right** (2-3 specific things)
2. **What could be stronger** (2-3 improvements, referencing specific Nielsen heuristics)
3. **One insight they might have missed** 
4. **Overall assessment** (1-2 sentences)

Use clear, direct language appropriate for an HCI course. Reference Nielsen's heuristics by name where relevant."""
                            }]
                        }).encode()

                        req = urllib.request.Request(
                            "https://api.anthropic.com/v1/messages",
                            data=payload,
                            headers={
                                "Content-Type": "application/json",
                                "x-api-key": api_key,
                                "anthropic-version": "2023-06-01"
                            }
                        )
                        with urllib.request.urlopen(req) as resp:
                            result = _json.loads(resp.read())
                        feedback_text = result["content"][0]["text"]
                        st.session_state.ai_feedback = feedback_text
                    except Exception as e:
                        st.error(f"API error: {e}. Check your API key and try again.")

        if st.session_state.ai_feedback:
            st.markdown("---")
            st.markdown("### Claude's Feedback on Your Redesign")
            st.markdown(f'<div class="feedback-box">{st.session_state.ai_feedback}</div>',
                        unsafe_allow_html=True)
            st.download_button("Download Feedback", st.session_state.ai_feedback,
                               file_name="ux_feedback.txt")


# ══════════════════════════════════════════════════════════════════════════════
#  PAGE 6 — Evaluation & Rubric
# ══════════════════════════════════════════════════════════════════════════════
elif page == "✅ Evaluation & Rubric":
    st.markdown('<div class="phase-badge">PHASE 5 · Evaluate Your Work</div>', unsafe_allow_html=True)
    st.markdown("## ✅ Evaluation & Rubric")

    rubric = [
        ("20", "Violation Identification", "Found ≥7 HCI violations with clear explanations of user impact"),
        ("15", "Principle Application", "Correctly mapped redesign choices to Nielsen's heuristics by name"),
        ("25", "Redesign Quality", "Improved contrast, hierarchy, labels, layout, and affordances"),
        ("20", "Design Rationale", "Justified every major decision with HCI vocabulary"),
        ("10", "Accessibility", "Addressed ≥3 accessibility concerns explicitly"),
        ("10", "Reflection", "Thoughtful comparison of bad vs. good UI; honest tradeoff discussion"),
    ]

    st.markdown("### Grading Rubric (100 pts)")
    for pts, criterion, desc in rubric:
        st.markdown(f"""
        <div class="rubric-row">
            <div class="rubric-pts">{pts}pts</div>
            <div>
                <div class="rubric-item" style="font-weight:600">{criterion}</div>
                <div class="rubric-item" style="color:#9ca3af; font-size:13px">{desc}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### Self-Assessment")
    self_score = {}
    for pts, criterion, desc in rubric:
        self_score[criterion] = st.slider(
            f"{criterion} ({pts} pts max)",
            0, int(pts), int(pts) // 2, key=f"self_{criterion}"
        )

    total_self = sum(self_score.values())
    st.markdown(f"**Your self-assessed score: {total_self}/100**")

    if total_self >= 90:
        st.success("🌟 Outstanding work!")
    elif total_self >= 75:
        st.info("👍 Solid effort — review the rubric areas where you scored lower.")
    else:
        st.warning("📚 Review the principles and strengthen your rationale before submitting.")

    st.markdown("---")
    st.markdown("### Final Reflection")
    st.text_area(
        "What's the most important HCI lesson you're taking from this activity?",
        key="final_reflection",
        height=100,
        placeholder="e.g., I never realized how much cognitive load poor labeling creates..."
    )
    st.text_area(
        "What tradeoffs did you make in your redesign? What did you sacrifice for simplicity?",
        key="tradeoff_reflection",
        height=80,
        placeholder="e.g., I removed the date filter to reduce clutter, but this means..."
    )

    st.markdown("---")
    st.markdown("### 📤 Submission Checklist")
    items = [
        "Completed violation hunt (Phase 2) with written explanations",
        "Filled in design decisions in Phase 4 → Design Decisions tab",
        "Can explain each choice using at least one Nielsen heuristic by name",
        "Wrote final reflection above",
        "Ready to demo your redesign to the class",
    ]
    for item in items:
        st.checkbox(item, key=f"submit_{item}")