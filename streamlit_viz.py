import streamlit as st
import pandas as pd
def test1():
    st.title("Bardcode")
    st.write("SCAN BARDCODES -> GEAR UP -> FIGHT MONSTERS -> CLIMB THE LEADERBOARDS -> EARN GLORY")

    # st.write("""
    # # Bardcode
    # **Proof of Concept**
    # """)

    barcode_field = st.text_input("Scan new barcode below","")
    valid_barcode_text = st.text("")
    
    # data_load_state = st.text("Loading data...")
    # data_load_state.text('Loading data...DONE!')
    valid_barcode = check_barcode(barcode_field)
    
    if valid_barcode:
        valid_barcode_text.text(f"Valid Barcode = '{barcode_field}'")
    else:
        valid_barcode_text.text("Please input a valid barcode")
    print(type(barcode_field))
    #df = pd.read_csv("my_data.csv")
    #st.line_chart(df)

@st.cache_data
def load_data(id):
    pass

def check_barcode_gtin8(barcode):
    print("def check_barcode_gtin8")
    return True
    pass

def check_barcode_gtin12(barcode):
    print("def check_barcode_gtin12")
    return True

def check_barcode_gtin13(barcode):
    print("def check_barcode_gtin13")
    return True
def check_barcode_gtin14(barcode):
    print("def check_barcode_gtin14")
    return True
def check_barcode_gsin(barcode):
    print("def check_barcode_gsin")
    return True
def check_barcode_sscc(barcode):
    print("def check_barcode_sscc")
    return True

def check_barcode(barcode):
    encoding_map = {
        8: check_barcode_gtin8,
        12: check_barcode_gtin12
    }
    mapped_encoding = encoding_map.get(len(barcode))
    if not mapped_encoding:
        # st.title("INVALID ENCODING")
        #raise ValueError("Invalid Encoding")
        pass
    else:
        result = mapped_encoding(barcode)
        return result
    return False
    #print(result)
    # if len(barcode) == 8:
    #     valid_barcode = check_barcode_gtin8(barcode)
    #     return valid_barcode
    # elif len(barcode)

