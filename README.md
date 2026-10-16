# Safety-and-Trust-Map
A Django-based web application that visualizes crime data across Mumbai to help people understand the relative safety of different areas. The platform maps crime statistics, displays area-wise crime rates, and provides insights to support more informed location-related decisions.



### Setup and Run

**1. Create and activate virtual environment**

```bash
python -m venv .venv
source .venv/bin/activate
```

**2. Install dependencies** (from the repository root)

```bash
pip install -r requirements.txt
```

**3. Run from the Django `app/` directory**

```bash
cd app
python manage.py migrate
python manage.py tailwind install
```

**4. Start the application**

Open two terminals in the `app/` directory.

Terminal 1 — Tailwind CSS:

```bash
python manage.py tailwind start
```

Terminal 2 — Django server:

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.
