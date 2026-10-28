"""Small Flask site for the EV Tableau dashboard and story."""

from pathlib import Path
import sys


ROOT_DIR = Path(__file__).resolve().parents[1]
REPORTS_DIR = ROOT_DIR / "reports"
LOCAL_PACKAGES = Path(__file__).resolve().parent / ".runtime-packages"
if LOCAL_PACKAGES.is_dir():
    sys.path.insert(0, str(LOCAL_PACKAGES))

from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

DASHBOARD_URL = (
    "https://public.tableau.com/views/ev_market_performance/Dashboard1"
    "?:showVizHome=no&:embed=true"
)
STORY_URL = (
    "https://public.tableau.com/views/ev_market_performance/Story1"
    "?:showVizHome=no&:embed=true"
)
TABLEAU_PROFILE_URL = "https://public.tableau.com/app/profile/yuvraj.devda/vizzes"


@app.get("/")
def home():
    return render_template(
        "index.html",
        dashboard_url=DASHBOARD_URL,
        story_url=STORY_URL,
        tableau_profile_url=TABLEAU_PROFILE_URL,
    )


@app.get("/media/<path:filename>")
def media(filename):
    return send_from_directory(REPORTS_DIR, filename)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
