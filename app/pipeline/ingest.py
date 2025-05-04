from sqlalchemy import create_engine

class Ingestor:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)

    def insert(self, invoices_df, line_items_df):
        invoices_df.to_sql("invoices", self.engine, if_exists="replace", index=False)
        line_items_df.to_sql("line_items", self.engine, if_exists="replace", index=False)
