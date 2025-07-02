💄 IngreMatch – Smart Cosmetic Checker

IngreMatch is a Progressive Web App (PWA) that allows users to check the availability and ingredient list of 1,470+ real cosmetics from Sephora - simply by entering the product name.

🚀 Key Features:

🔎 Search Any Product – Check if a cosmetic exists and view its ingredient list.  
🧪 Ingredient Transparency – Get simplified insight into what's inside your product.  
📱  PWA Capable – Installable like a native app, responsive on mobile and desktop.  
⚡ Fast Flask API – Backend powered by Python + Flask with JSON responses.  
📊 Interactive Dashboard – Tableau dashboard visualizing product label distribution, rank vs. price trends and ingredient patterns.

🧪 Dataset:

The app is powered by a structured dataset scraped from Sephora, containing:
- Product Names
- Labels (e.g., moisturizer, serum)
- Ingredient Lists
- Price
- Product Rank

📁 Dataset file: `cosmetics.csv`

🧰 Tech Stack:

| Component       | Tools Used                  |
|-----------------|-----------------------------|
| Frontend        | HTML, CSS, JavaScript       |
| Backend         | Flask (Python)              |
| Data Handling   | pandas, CSV                 |
| Visualization   | Tableau (for dashboards)    |
| Application Type| Progressive Web App (PWA)   |

📊 Tableau Dashboard Highlights:

Developed an interactive Tableau dashboard using the same dataset to visually analyze:
- 🧴 Product Count per Label 
- 💸 Price vs Rank Correlation 
- 🔍 Skin Type Suitability Count 
- 🏷️ Category-wise product count

Dashboards are exportable and can aid cosmetic product research and marketing analysis.

🖥️ How to Run the App:

1. Clone the repository:
   Navigate to backend directory: cd ingrematch/backend
   Create virtual environment & install requirements: python -m venv venv
                                                      venv\Scripts\activate
                                                      pip install -r requirements.txt
   Run Flask server: python app.py
   Open your browser: http://127.0.0.1:5000/

📁 Project folder structure:

| Folder / File Path          | Description                         |
| --------------------------- | ----------------------------------- |
| `ingrematch/`               | Root project directory              |
| ├── `backend/`              | Flask backend files                 |
| │   ├── `app.py`            | Main Flask API script               |
| │   ├── `cosmetics.csv`     | Dataset file with Sephora products  |
| │   └── `templates/`        | Folder for HTML templates           |
| │      └── `index.html`     | Main HTML frontend interface        |
| ├── `static/`               | Static files used by frontend       |
| │   ├── `css/`              | CSS styling folder                  |
| │   │   └── `style.css`     | Main stylesheet                     |
| │   ├── `js/`               | JavaScript folder                   |
| │   │   └── `script.js`     | JS for frontend logic and API calls |
| │   └── `img/`              | Images used in the app              |
| │      ├── `logo.png`       | Logo image shown in the app         |
| │      └── `background.jpg` | Background image for the webpage    |




