from sqlalchemy import create_engine, text

DB_URL = "postgresql://invoice_db_6gwd_user:OVSuQM8IQWK6NHpGCy53rkYELDPH7zvE@dpg-d0bm76buibrs73dfnbmg-a.oregon-postgres.render.com/invoice_db_6gwd"
engine = create_engine(DB_URL)

def total_invoice_count():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT COUNT(*) FROM invoices"))
        return result.scalar()

def unmatched_invoice_totals():
    query = """
    SELECT i.invoice_id, i.total AS invoice_total, 
           SUM(li.line_rate * li.line_quantity) AS line_total
    FROM invoices i
    JOIN line_items li ON i.invoice_id = li.invoice_id
    GROUP BY i.invoice_id, i.total
    HAVING i.total != SUM(li.line_rate * li.line_quantity)
    """
    with engine.connect() as conn:
        return [dict(row._mapping) for row in conn.execute(text(query))]

def line_items_by_category():
    query = "SELECT category, COUNT(*) FROM line_items GROUP BY category"
    with engine.connect() as conn:
        return [dict(row._mapping) for row in conn.execute(text(query))]

def revenue_by_category():
    query = """
    SELECT category, SUM(line_rate * line_quantity) AS revenue
    FROM line_items
    GROUP BY category
    """
    with engine.connect() as conn:
        return [dict(row._mapping) for row in conn.execute(text(query))]

def top_invoice_totals(limit=5):
    query = text("""
    SELECT invoice_id, total 
    FROM invoices 
    ORDER BY total DESC 
    LIMIT :limit
    """)
    with engine.connect() as conn:
        return [dict(row._mapping) for row in conn.execute(query, {"limit": limit})]
