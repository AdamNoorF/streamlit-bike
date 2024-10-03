### Setup environment

python -m venv dashboard
dashboard\Scripts\activate
pip install -r requirements.txt
# jika file requirements.txt belum ada maka
pip install numpy pandas matplotlib seaborn streamlit

### Penggunaan jupyter

jupyter notebook notebook.ipynb

### Run Streamlit app

streamlit run dashbroad_bike.py
