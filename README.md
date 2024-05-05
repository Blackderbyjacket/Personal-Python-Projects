The script automates the extraction of transaction data from multiple PDF files, organizes it into a structured format, and saves it for further analysis or processing. Code will need to be updated to clean the data as you require OR work will be required to clean and analyse data in excel.

This is done in 5 main stages 
1 - Find PDF Files: It looks for PDF files in a specified folder.
2 - Extract Tables: For each PDF file found, it uses a library called Tabula to extract tables from the PDF.
3 - Parse Table Rows: For each table extracted from the PDF, it goes through each row and tries to find transaction data using a specific pattern (date, description, and amount).
4 - Collect Transactions: When it finds transaction data in a row, it records it along with the file name it came from.
5 - Save Data: After processing all PDF files, it saves the collected transaction data into a CSV file. Each row in the CSV represents a transaction, with columns for the transaction date, description, amount, and the name of the PDF file it originated from.
