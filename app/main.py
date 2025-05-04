from fastapi import FastAPI
from reports import reports

app = FastAPI()

@app.get("/report/invoice-count")
def report_invoice_count():
    return {"invoice_count": reports.total_invoice_count()}

@app.get("/report/unmatched-totals")
def report_unmatched_totals():
    return reports.unmatched_invoice_totals()

@app.get("/report/line-items-category")
def report_line_items_by_category():
    return reports.line_items_by_category()

@app.get("/report/revenue-category")
def report_revenue_by_category():
    return reports.revenue_by_category()

@app.get("/report/top-invoices")
def report_top_invoices():
    return reports.top_invoice_totals()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1")

