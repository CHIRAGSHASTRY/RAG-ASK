# start.py
import subprocess
import webbrowser
import time

# Open the app after a short delay
webbrowser.open("http://localhost:8501")

# Run Streamlit app
subprocess.Popen(["streamlit", "run", "app.py"])

# Optional: keep script running to avoid auto-close
time.sleep(5)
