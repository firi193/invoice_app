import pandas as pd

class BaseLoader:
    def __init__(self, invoice_path, line_item_path):
        self.invoice_path = invoice_path
        self.line_item_path = line_item_path

    def load_dataframes(self):
        invoices = pd.read_csv(self.invoice_path)
        line_items = pd.read_csv(self.line_item_path)
        return invoices, line_items
