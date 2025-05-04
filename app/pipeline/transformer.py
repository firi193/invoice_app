import pandas as pd

class Transformer:
    def __init__(self, invoices_df, line_items_df):
        self.invoices = invoices_df.copy()
        self.line_items = line_items_df.copy()

    def clean_invoices(self):
        df = self.invoices
        df.columns = df.columns.str.strip().str.lower()
        df['invoice_id'] = df['invoice_id'].astype(int)
        df['total'] = pd.to_numeric(df['total'], errors='coerce')
        df.dropna(subset=['invoice_id', 'total'], inplace=True)
        self.invoices = df
        return self

    def clean_line_items(self):
        df = self.line_items
        df.columns = df.columns.str.strip().str.lower()
        df['invoice_id'] = df['invoice_id'].astype(int)
        df['line_rate'] = pd.to_numeric(df['line_rate'], errors='coerce')
        df['line_quantity'] = pd.to_numeric(df['line_quantity'], errors='coerce')
        df.dropna(subset=['invoice_id', 'line_rate', 'line_quantity'], inplace=True)
        self.line_items = df
        return self

    def classify_items(self):
        def classify_item(name):
            name = name.lower()
            if "coaching" in name:
                return "coaching"
            elif "outbound" in name:
                return "outbound"
            elif "shipping" in name:
                return "shipping"
            elif "rollover" in name:
                return "rollover"
            else:
                return "supplement"

        self.line_items["category"] = self.line_items["item_name"].apply(classify_item)
        return self

    def add_line_totals(self):
        self.line_items["line_total"] = self.line_items["line_rate"] * self.line_items["line_quantity"]
        return self

    def get_transformed(self):
        return self.invoices, self.line_items
