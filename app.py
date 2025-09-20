import streamlit as st
import streamlit.components.v1 as components

# Page configuration
st.set_page_config(
    page_title="AutoResume AI - Hackathon Submission",
    page_icon="📄",
    layout="wide"
)

# Title
st.title("📄 Automated Resume Relevance Check System")
st.markdown("### AI-Powered Matching for Innomatics Research Labs | Generative AI Theme")

# Warning message
st.warning("""
⚠️ HACKATHON SUBMISSION MODE:
This Streamlit app embeds our V0 prototype for compliance with deployment rules.
The core AI scoring engine (Python) is simulated in this demo. Full backend integration will follow post-hackathon.
""")

# Your live V0 app URL
V0_URL = "https://resumerelevance.vercel.app"

# Embed your V0 app
st.markdown("### 👇 Try the Live App Below")
components.iframe(V0_URL, height=850, scrolling=True)

# Footer explaining tech
st.markdown("---")
st.subheader("⚙️ How It Works (Behind the Scenes)")
st.markdown("""
- **Frontend UI**: Built with V0.dev + React → Hosted on Vercel
- **AI Scoring Engine**: Python-based (Hybrid: Rule-based + LLM) → Simulated in demo
- **Parsing**: PyMuPDF, spaCy
- **Matching**: BM25 (keywords) + SentenceTransformers (semantic) + GPT-4o (feedback)
- **Deployed On**: Streamlit Cloud (as required by hackathon rules)
""")

st.markdown("🔗 **V0 Prototype URL**: [resumerelevance.vercel.app](https://resumerelevance.vercel.app)")