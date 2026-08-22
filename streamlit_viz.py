import streamlit as st
import pandas as pd


def test1():
    st.title("Bardcode")
    st.write("SCAN BARDCODES -> GEAR UP -> FIGHT MONSTERS -> CLIMB THE LEADERBOARDS -> EARN GLORY")
    # barcode_field = st.text_input("Scan new barcode below HERE",st.session_state.submitted_val,placeholder=st.session_state.current_placeholder,key="barcode_text_input",on_change=handle_submit)
    # barcode_entry_2 = barcode_field2.text_input("Scan new barcode below","",placeholder="")

    
    # data_load_state = st.text("Loading data...")
    # data_load_state.text('Loading data...DONE!')
    ##### valid_barcode = check_barcode(barcode_field)
    with st.form("my_form", clear_on_submit=True):
        barcode_field = st.text_input("Message")
        submitted = st.form_submit_button("Send")
        # if submitted:
        #     st.write(f"Sent: {barcode_field}")
        valid_barcode = check_barcode(barcode_field)      

        valid_barcode_text = st.text("")
        valid_barcode_val = st.text("")
        text_loot_gen = st.markdown("")

        if valid_barcode:
            valid_barcode_text.text(f"Valid Barcode = '{barcode_field}'")
            valid_barcode_val.text(f"barcode mod 67: {abs(hash(barcode_field))%67}")
            generate_discovery(barcode_field)
            #st.session_state.barcode_text_input = st.text_input("Scan new barcode below","",placeholder=barcode_field,key="barcode_text_input")

        else:
            valid_barcode_text.text("Please input a valid barcode")
            valid_barcode_val.text("")
            text_loot_gen = st.markdown("")
        #df = pd.read_csv("my_data.csv")
        #st.line_chart(df)


def generate_discovery(barcode_field):
    barcode_hash = abs(hash(barcode_field))
    gen_seed_group = barcode_hash%67
    # if statements to determine nothing, quest, encounter, item, monster
    if gen_seed_group == 0:
        gen_quest(barcode_hash)
    elif gen_seed_group >= 1 and gen_seed_group <= 39:
        gen_nothing(barcode_hash)
    elif gen_seed_group >= 40 and gen_seed_group <= 45:
        gen_encounter(barcode_hash)
    elif gen_seed_group >= 46 and gen_seed_group <= 66:
        gen_item(barcode_hash)
    else:
        raise ValueError(f"Something has gone horribly wrong, def generate_discovery({barcode_field})")


def gen_nothing(barcode_hash):
    print("gen_nothing(barcode_hash)")
    text_loot_gen = st.markdown("YOU'VE FOUND **NOTHING**")
    pass
def gen_quest(barcode_hash):
    text_loot_gen = st.markdown("HARK, A **QUEST**")
    print("def gen_quest(barcode_hash):")
    pass
def gen_encounter(barcode_hash):
    # gift, friendly, undetermined, hostile
    ct_encounter = 17 # translates directly to row
    gen_seed = abs(hash(barcode_hash))%ct_encounter
    if gen_seed == 0:
        text_loot_gen = st.markdown("A GIFT!")
        pass
    elif barcode_hash == abs(hash("045496738228")):
        text_loot_gen = st.markdown("KIRBY! **AND** THE SQUEAK SQUAD!!!")
    else:
        text_loot_gen = st.markdown("EEK, a *something*.... or is it a *someone*?!")
    print("gen_encounter(barcode_hash)")
    pass
def gen_item(barcode_hash):
    ct_items = 100
    gen_seed = abs(hash(barcode_hash))%ct_items

    if gen_seed < 5:    #Weapon
        gen_item_weapon()
        pass
    elif gen_seed < 10: #Armor
        pass
    elif gen_seed < 70: #Consumable
        pass
    else:               #Misc
        pass
    
    text_loot_gen = st.markdown("WOW, it's a **THING**!")
    print("gen_item(barcode_hash):")
    pass



@st.cache_data
def load_data(id):
    pass

def check_barcode_gtin8(barcode):
    print("def check_barcode_gtin8")
    return True
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
        # len() = 6,9,10
        8: check_barcode_gtin8,
        12: check_barcode_gtin12,
        13: check_barcode_gtin13,
        14: check_barcode_gtin14,
        17: check_barcode_gsin,
        18: check_barcode_sscc
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


