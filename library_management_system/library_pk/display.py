import pandas as pd

def display_books(books):
    data = {
    "Title": [bk.title for bk in books],
    "Author": [bk.author for bk in books],
    "Content": [bk.content for bk in books],
    "Available" :['Yes' if bk.isAvailable else 'No' for bk in books],
    "Borrower Name":[bk.borrowed_name for bk in books],
    "Borrower Id":[bk.borrower_email for bk in books],
    "CreatedAt": [bk.createdAt for bk in books],
    "UpdatedAt":[bk.updatedAt for bk in books]
    }
    df = pd.DataFrame(data,index=[x for x in range(1,len(books)+1)])
    print(df)

def display_transaction(transaction):
    data ={
        "Book ID":[trans.bid+1 for trans in transaction],
        "Book Name": [trans.bname for trans in transaction],
        "Borrower Name":[trans.pname for trans in transaction],
        "Borrower Email":[trans.pid for trans in transaction],
        "Transaction Type":['Assigned' if trans.transaction_type==1 else 'Returned'  for trans in transaction],
    }
    df = pd.DataFrame(data,index=[x for x in range(1,len(transaction)+1)])
    print(df)