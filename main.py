import streamlit as st
import pandas as pd
import streamlit_viz as stv
import psycopg2
import db

def main():
    print("testing database connection:")
    db.connect()

    print("testing streamlit visualization:")
    stv.test1()
    
    print("Done1")



if __name__ == '__main__':
    main()