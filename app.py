from flask import Flask, render_template, request
import streamlit as st
from streamlit.components.v1 import html
import requests
import datetime
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/streamlit", methods=["GET"])
def streamlit_app():  

    st.title("Solar Farm Monitoring")

    return render_template("streamlit.html", streamlit_html=st.experimental_get_query_params())


if __name__ == "__main__":
    app.run(debug=True, port=5000)  

