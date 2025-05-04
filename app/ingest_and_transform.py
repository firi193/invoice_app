from psycopg2 import OperationalError

from pipeline.base_loader import BaseLoader
from pipeline.transformer import Transformer
from pipeline.ingest import Ingestor
import logging
import traceback

from dotenv import load_dotenv
import os

load_dotenv()

DB_URL = os.getenv("DB_URL")

logging.basicConfig(level=logging.INFO)

def run_pipeline():
    logging.info("Starting pipeline...")

    loader = BaseLoader("./../data/invoices_test.csv", "./../data/invoice_line_items_test.csv")
    invoices, line_items = loader.load_dataframes()
    logging.info(f"Loaded {len(invoices)} invoices and {len(line_items)} line items.")

    transformer = Transformer(invoices, line_items)
    transformer.clean_invoices().clean_line_items().classify_items().add_line_totals()
    invoices_clean, line_items_clean = transformer.get_transformed()
    logging.info(f"Transformed data. Clean invoices: {len(invoices_clean)}, Clean line items: {len(line_items_clean)}.")

    ingestor = Ingestor(DB_URL)
    ingestor.insert(invoices_clean, line_items_clean)
    logging.info("Data successfully ingested into the database.")


if __name__ == "__main__":
    try:
        run_pipeline()
    except Exception as e:
        logging.error("Pipeline failed with error:")
        traceback.print_exc()


# import psycopg2
# from psycopg2 import OperationalError

# def check_db_connection_and_query(DB_URL):
#     try:
#         conn = psycopg2.connect(DB_URL)
#         conn.autocommit = True
#         print("Database connection successful.")
        
#         with conn.cursor() as cursor:
#             # List tables
#             print("\nListing tables:")
#             cursor.execute("""
#                 SELECT table_name 
#                 FROM information_schema.tables 
#                 WHERE table_schema = 'public';
#             """)
#             tables = cursor.fetchall()
#             for table in tables:
#                 print(table[0])
            
#             # Query first five rows from invoices
#             print("\nFirst five rows from 'invoices':")
#             cursor.execute("SELECT * FROM invoices LIMIT 5;")
#             invoices = cursor.fetchall()
#             for row in invoices:
#                 print(row)
            
#             # Query first five rows from invoice_line_items
#             print("\nFirst five rows from 'line_items':")
#             cursor.execute("SELECT * FROM line_items LIMIT 5;")
#             line_items = cursor.fetchall()
#             for row in line_items:
#                 print(row)
        
#         conn.close()
#     except OperationalError as e:
#         print("Failed to connect to the database.")
#         print(e)
#     except Exception as e:
#         print("An error occurred while querying the database.")
#         print(e)


# check_db_connection_and_query(DB_URL)
