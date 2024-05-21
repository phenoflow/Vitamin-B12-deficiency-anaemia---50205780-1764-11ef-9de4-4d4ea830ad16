# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"D011.11","system":"readv2"},{"code":"C262100","system":"readv2"},{"code":"35092","system":"readv2"},{"code":"29486","system":"readv2"},{"code":"22715","system":"readv2"},{"code":"2464","system":"readv2"},{"code":"46289","system":"readv2"},{"code":"24581","system":"readv2"},{"code":"48714","system":"readv2"},{"code":"72895","system":"readv2"},{"code":"11126","system":"readv2"},{"code":"55370","system":"readv2"},{"code":"7403","system":"readv2"},{"code":"6028","system":"readv2"},{"code":"66935","system":"readv2"},{"code":"12329","system":"readv2"},{"code":"8013","system":"readv2"},{"code":"5271","system":"readv2"},{"code":"62637","system":"readv2"},{"code":"2813","system":"readv2"},{"code":"58599","system":"readv2"},{"code":"42928","system":"readv2"},{"code":"56973","system":"readv2"},{"code":"7736","system":"readv2"},{"code":"47952","system":"readv2"},{"code":"69275","system":"readv2"},{"code":"36840","system":"readv2"},{"code":"2482","system":"readv2"},{"code":"31126","system":"readv2"},{"code":"53846","system":"readv2"},{"code":"31270","system":"readv2"},{"code":"32953","system":"readv2"},{"code":"2515","system":"readv2"},{"code":"D51","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('vitamin-b12-deficiency-anaemia-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["vitamin---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["vitamin---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["vitamin---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
