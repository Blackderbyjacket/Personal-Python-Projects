#Imports of required libraries. 
import os #os: for operating system related functions.
from datetime import datetime #datetime: for working with dates and times.
import pandas as pd #pandas as pd: for data manipulation and analysis.
import tabula #tabula: for extracting tables from PDF files.
import re #re: for working with regular expressions.

#This line defines a function named extract_tables_from_pdfs which takes a folder path as input.
def extract_tables_from_pdfs(folder_path):
    pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')] #This line creates a list pdf_files containing names of all files in the specified folder (folder_path) that end with '.pdf'.
    transactions = [] #This line initializes an empty list named transactions to store extracted transaction data.

    for file in pdf_files:#This line starts a loop to iterate over each PDF file in the pdf_files list.
        file_path = os.path.join(folder_path, file) #This line constructs the full file path for the current PDF file by joining the folder path (folder_path) with the file name (file).
        tables = tabula.read_pdf(file_path, pages="all", multiple_tables=True) #This line uses Tabula to read tables from the PDF file specified by file_path. It reads all pages (pages="all") and extracts multiple tables if they exist (multiple_tables=True).
        
        # Extract file name without extension
        file_name = os.path.splitext(file)[0]

        for table in tables:#This line starts a loop to iterate over each table extracted from the PDF file.
            for row in table.itertuples(index=False): #This line starts a loop to iterate over each row in the current table.
                row_str = ','.join(str(elem) for elem in row)  #This line converts the row (which is a named tuple) to a string, with each element separated by a comma.
                transaction_pattern = (
                    r"\d+\s\w+\s*,\s*\d+\s\w+\s*,\s*(.*?),\s*([£$€]?\s?[\d.,]+)"
                ) #This line defines a regular expression pattern to extract transaction data from the row.
                matches = re.findall(transaction_pattern, row_str) #This line uses the regular expression pattern to find all matches of transaction data in the row.
                for match in matches: #This line starts a loop to iterate over each match found in the row.
                    if len(match) == 2:  # Check if match contains both description and amount
                        transactions.append({
                            'transaction_date': row[0],
                            'transaction_description': match[0],
                            'transaction_amount': match[1],
                            'file_name': file_name  # Add file name as a column
                        }) #This appends a dictionary containing transaction details (date, description, amount, and file name) to the transactions list.

    if transactions:
        return pd.DataFrame(transactions)
    else:
        return None
#This line checks if any transactions were extracted. If there are transactions, it converts the list of dictionaries into a DataFrame using pandas and returns it. Otherwise, it returns None.
def save_to_csv(data, output_folder):
    today_date = datetime.today().strftime('%d-%m-%Y')
    output_filename = os.path.join(output_folder, f"{today_date}.csv")
    data.to_csv(output_filename, index=False)
    print(f"Data saved to {output_filename}") #Publishes a CVS File with the current date as the title to a given path

if __name__ == "__main__":
    folder_path = r"#PATH"
    output_folder = r"#PATH"

    extracted_data = extract_tables_from_pdfs(folder_path)
    if extracted_data is not None:
        save_to_csv(extracted_data, output_folder)
    else:
        print("No relevant data found in PDFs.") #Defines response if no relevant data in PDF