import os
import csv
import pandas as pd
import hashlib
import shutil
from csv import DictReader
import pathlib
csv.register_dialect('pipe_delim', delimiter='|', quoting=csv.QUOTE_NONE)

def main():

    gen_ct_csv('CreateTable_CSVs')
    # gen_ct_csv('CreateTable_CSVs\\has_dependencies1')
    # gen_ct_csv('CreateTable_CSVs\\has_dependencies2')

def gen_ct_csv(dir):
    temp_header = "temp_header.csv"
    temp_full = "temp_full.csv"
    for file in os.listdir(dir):
        try:
            if file[-4:] == '.csv':
                filepath = dir + '\\' + file
                table_name = str(file).replace("CreateTable_","").replace(".csv","")

                #REWRITE HEADER
                with open(filepath,"r") as fin:
                    with open(temp_header, 'w', newline='') as fout:
                        r = csv.reader(fin, dialect="pipe_delim")
                        w = csv.writer(fout, dialect="pipe_delim")
                        old_header = next(r)
                        if old_header[0][-3:] == 'int':
                            old_header[0] = old_header[0][:-3] + 'varchar(255)'
                        
                        new_header = old_header
                        w.writerow(new_header)
                        for row in r:
                            w.writerow(row)

                #REWRITE IDs
                with open(temp_header,"r") as fin:
                    with open(temp_full, 'w', newline='') as fout:
                        reader = csv.DictReader(fin, dialect="pipe_delim")
                        list_of_dicts = list(reader)
                        for each in range(0,len(list_of_dicts)):
                            ct = 0
                            id_key = None
                            hash_val = ""
                            for key, val in list_of_dicts[each].items():
                                if val:
                                    if ct == 0:
                                        id_key = key

                                    elif ct == 1 or ct == 2:
                                        hash_val += val
                                    elif ct > 2:
                                        break
                                ct+=1
                            # print(f"\thash_val: {hash_val}")
                            # print(f"\tval_to_be_hashed: {table_name + hash_val}")
                            list_of_dicts[each][id_key] = "'" + hashlib.sha256(bytes(table_name + hash_val,"utf-8")).hexdigest() + "'"
                        # print(f"\t\tlist_of_dicts: {list_of_dicts}")
                        writer = csv.DictWriter(fout, reader.fieldnames, delimiter='|')
                        writer.writeheader()
                        writer.writerows(list_of_dicts)

                # rename csv, clean up temp files
                shutil.copy(temp_full,filepath)
                os.remove(temp_header)
                os.remove(temp_full)

        except Exception as e:
            print(e)


# def fix_id_header(filepath):
#     df = pd.read_csv(filepath,delimiter='|')
#     df['_id int'] = hashlib.sha256(b"hello").hexdigest()


if __name__ == '__main__':
    main()