import csv
import matplotlib.pyplot as plt
import os
# Initialize an empty list to store the values


# Read the CSV file
signals = [
    "c432.NAND4_141.tem1",
    "c432.NAND4_157.tem2",
    "c432.N162",
    "c432.N307",
    "c432.NAND4_157.tem1",
    "c432.NAND4_140.tem2",
    "c432.NAND4_159.tem2",
    "c432.N24",
    "c432.N254",
    "c432.NAND4_155.tem1",
    "c432.AND9_86.tem2",
    "c432.N294",
    "c432.N126",
    "c432.N332",
    "c432.NAND4_140.tem3",
    "c432.NAND4_140.tem1",
    "c432.AND8_148.tem1",
    "c432.N1",
    "c432.NAND4_141.tem2",
    "c432.N130",
    "c432.N37",
    "c432.NAND4_158.tem2",
    "c432.N267",
    "c432.N386",
    "c432.N196",
    "c432.N118",
    "c432.N431",
    "c432.NAND4_159.tem1",
    "c432.AND9_86.tem3",
    "c432.NAND4_159.tem3",
    "c432.N250",
    "c432.AND8_148.tem2",
    "c432.NAND4_158.tem1",
    "c432.N242",
    "c432.N230",
    "c432.N371",
    "c432.N99",
    "c432.N360",
    "c432.N375",
    "c432.NAND4_139.tem2",
    "c432.AND9_126.tem6",
    "c432.AND9_126.tem5",
    "c432.N108",
    "c432.N92",
    "c432.AND9_126.tem7",
    "c432.AND9_126.tem4",
    "c432.N350",
    "c432.N186",
    "c432.N346",
    "c432.N302",
    "c432.N289",
    "c432.NAND4_138.tem1",
    "c432.N379",
    "c432.N151",
    "c432.N370",
    "c432.N154",
    "c432.AND9_126.tem2",
    "c432.N224",
    "c432.N357",
    "c432.N355",
    "c432.AND9_126.tem3",
    "c432.NAND4_139.tem1",
    "c432.N73",
    "c432.N177",
    "c432.N247",
    "c432.AND9_46.tem2",
    "c432.N344",
    "c432.AND9_46.tem3",
    "c432.N430",
    "c432.N197",
    "c432.AND9_86.tem4",
    "c432.AND8_148.tem4",
    "c432.AND8_148.tem3",
    "c432.NAND4_158.tem3",
    "c432.N30",
    "c432.N185",
    "c432.AND9_86.tem5",
    "c432.N14",
    "c432.N105",
    "c432.AND9_86.tem6",
    "c432.N127",
    "c432.AND8_148.tem5",
    "c432.N184",
    "c432.N53",
    "c432.N79",
    "c432.N195",
    "c432.N40",
    "c432.N119",
    "c432.NAND4_145.tem2",
    "c432.N4",
    "c432.NAND4_144.tem1",
    "c432.NAND4_145.tem1",
    "c432.NAND4_144.tem2",
    "c432.N143",
    "c432.N194",
    "c432.N82",
    "c432.AND9_46.tem7",
    "c432.N34",
    "c432.NAND4_143.tem1",
    "c432.N66",
    "c432.N190",
    "c432.N301",
    "c432.N273",
    "c432.N159",
    "c432.N168",
    "c432.N429",
    "c432.N189",
    "c432.N338",
    "c432.N158",
    "c432.NAND4_160.tem3",
    "c432.NAND3_156.tem1",
    "c432.NAND4_143.tem2",
    "c432.NAND4_142.tem3",
    "c432.N157",
    "c432.N288",
    "c432.NAND4_157.tem3",
    "c432.N399",
    "c432.N432",
    "c432.N236",
    "c432.N335",
    "c432.N227",
    "c432.N336",
    "c432.N334",
    "c432.N89",
    "c432.NAND4_146.tem2",
    "c432.N257",
    "c432.N76",
    "c432.N258",
    "c432.N8",
    "c432.N21",
    "c432.AND8_148.tem6",
    "c432.N285",
    "c432.N414",
    "c432.NAND4_146.tem1",
    "c432.NAND4_146.tem3",
    "c432.N343",
    "c432.N135",
    "c432.N56",
    "c432.N142",
    "c432.AND9_86.tem7",
    "c432.N146",
    "c432.N256",
    "c432.N63",
    "c432.N138",
    "c432.N112",
    "c432.N123",
    "c432.N50",
    "c432.NAND4_142.tem2",
    "c432.NAND4_142.tem1",
    "c432.N255",
    "c432.N134",
    "c432.AND9_46.tem6",
    "c432.AND9_46.tem5",
    "c432.AND9_46.tem4",
    "c432.N347",
    "c432.N17",
    "c432.N122",
    "c432.N411",
    "c432.N47",
    "c432.N102",
    "c432.N420",
    "c432.N11",
    "c432.N150",
    "c432.N341",
    "c432.N340",
    "c432.N259",
    "c432.N282",
    "c432.N180",
    "c432.N246",
    "c432.N27",
    "c432.NAND4_145.tem3",
    "c432.N183",
    "c432.N251",
    "c432.N86",
    "c432.N345",
    "c432.N147",
    "c432.AND9_46.tem1",
    "c432.N95",
    "c432.N60",
    "c432.N342",
    "c432.N425",
    "c432.N191",
    "c432.N407",
    "c432.N393",
    "c432.N291",
    "c432.N199",
    "c432.N377",
    "c432.N372",
    "c432.N188",
    "c432.N139",
    "c432.N243",
    "c432.N292",
    "c432.N305",
    "c432.NAND4_138.tem2",
    "c432.N354",
    "c432.AND9_126.tem1",
    "c432.N374",
    "c432.N270",
    "c432.NAND4_144.tem3",
    "c432.N295",
    "c432.N380",
    "c432.N300",
    "c432.N418",
    "c432.NAND4_138.tem3",
    "c432.N239",
    "c432.N349",
    "c432.N115",
    "c432.N422",
    "c432.NAND4_141.tem3",
    "c432.N353",
    "c432.N331",
    "c432.NAND4_155.tem3",
    "c432.N279",
    "c432.N428",
    "c432.N131",
    "c432.N296",
    "c432.N290",
    "c432.NAND4_155.tem2",
    "c432.N264",
    "c432.N187",
    "c432.N213",
    "c432.N421",
    "c432.AND9_86.tem1",
    "c432.NAND4_160.tem1",
    "c432.N319",
    "c432.N417",
    "c432.N419",
    "c432.N192",
    "c432.N171",
    "c432.N193",
    "c432.N416",
    "c432.N415",
    "c432.NAND3_156.tem2",
    "c432.N233",
    "c432.N303",
    "c432.N373",
    "c432.N308",
    "c432.N330",
    "c432.N309",
    "c432.N276",
    "c432.N306",
    "c432.N352",
    "c432.N198",
    "c432.N260",
    "c432.N356",
    "c432.NAND4_139.tem3",
    "c432.N376",
    "c432.N203",
    "c432.N333",
    "c432.N69",
    "c432.N43",
    "c432.N263",
    "c432.N165",
    "c432.N304",
    "c432.N404",
    "c432.N174",
    "c432.N337",
    "c432.N293",
    "c432.N329",
    "c432.N351",
    "c432.NAND4_143.tem3",
    "c432.N339",
    "c432.N348",
    "c432.NAND4_160.tem2",
    "c432.N378",
    "c432.N223",
    "c432.N381"
]

# To print the list of signals
#print(signals)

for i in signals:
    out2_values = []
    with open('leakage.csv', 'r') as csvfile:
        # Create a CSV reader
        csvreader = csv.reader(csvfile)

        # Initialize a flag to check if the relevant section is reached
        found_section = False

        # Iterate through each row in the CSV file
        for row in csvreader:
            # Check if the row is empty
            if not row:
                continue

            # Check if the section containing values has started
            if row[0] == 'Signal' and row[1] == 'Leakage':
                found_section = True
                continue

            # Check if the relevant signal is found
            if found_section and row[0] == i:
                # Extract the value after the comma and append it to the list
                value = float(row[1])
                out2_values.append(value)

    # Print the list of values adjoining to FullAdder.cla.c2.out2

    #print(len(out2_values))
    # Plot the values
    plt.plot(out2_values, marker='o')
    plt.title(f'Values adjoining to {i}')
    plt.xlabel('Index')
    plt.ylabel('Values')
    #plt.show()
    directory = '/home/varunm/MiniProject/ideal/power-side-channel-analysis/plan/c432/plots'
    if not os.path.exists(directory):
        os.makedirs(directory)

# Save the plot to the directory
    plt.savefig(os.path.join(directory, f'{i}.png'))
    plt.show()
    plt.close()
