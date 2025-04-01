import psycopg2
from psycopg2 import sql, extras
from contextlib import contextmanager
import os


class DatabaseHander:
    def __init__(self):
        self.conn_params = {
            'dbname': os.getenv('DB_NAME', 'expense_application'),
            'user': os.getenv('DB_USER', 'postgres'),
            'password': os.getenv('DB_PASSWORD', 'Pass12!'),
            'host': os.getenv('DB_HOST', 'localhost'),
            'port': os.getenv('DB_PORT', '5432')
        }

    # Context manager for safe cursor handling
    @contextmanager
    def _get_cursor(self, cursor_type=None):
        conn = psycopg2.connect(**self.conn_params)
        try:
            cursor_t = extras.DictCursor if cursor_type == 'dict' else None
            with conn.cursor(cursor_factory=cursor_t) as cursor:
                yield cursor
                conn.commit()
        except Exception as e:
            conn.rollback()
            raise Exception(f"Database operation failed: {e}")
        finally:
            conn.close()
    
    # Returns all records in selected table from database
    def get_all_values(self, table):
        with self._get_cursor(cursor_type='dict') as cursor:
            query = sql.SQL("SELECT * FROM {}").format(
                sql.Identifier(table)
            )
            cursor.execute(query)
            return cursor.fetchall()
    
    # Returns values of specific record from table selected by user
    def get_specific_record(self, table, record_id):
        with self._get_cursor() as cursor:
            query = sql.SQL("SELECT * FROM {} WHERE id = %s").format(
                sql.Identifier(table)
            )
            cursor.execute(query, (record_id,))
            return cursor.fetchall()
    
    # Returns values from specific field selected in database by user
    def get_specfic_field(self, table, field):
        with self._get_cursor() as cursor:
            query = sql.SQL("SELECT {} FROM {}").format(
                sql.Identifier(field),
                sql.Identifier(table)
            )
            cursor.execute(query)
            return cursor.fetchall()
        
    def add_expense(self, expense):
        with self._get_cursor() as cursor:
            try:
                query = """INSERT INTO expenses (id, date, category, has_receipt, description, amount_spent) VALUES (%s, %s, %s, %s, %s, %s)"""
                cursor.execute(query, (expense.id, expense.date, expense.category, expense.has_receipt, expense.description, expense.amount_spent))
                return "expense added"
            except Exception as e:
                print(f"Error details: {e}")
                raise ValueError(f"Failed to create expense: {str(e)}")
    
    def delete_record(self, table, record_id):
         with self._get_cursor() as cursor:
            try:
                query = sql.SQL("DELETE FROM {} where id = %s").format(
                    sql.Identifier(table)
                )
                cursor.execute(query, (record_id,))
                return "expense deleted"
            except Exception as e:
                print(f"Error details: {e}")
                raise ValueError(f"Failed to delete expense: {str(e)}")
            
    def edit_expense(self, expense):
        with self._get_cursor() as cursor:
            try:
                query = """UPDATE expenses SET date = %s, category = %s, has_receipt = %s, description = %s, amount_spent = %s WHERE id = %s """
                cursor.execute(query, (expense.date, expense.category, expense.has_receipt, expense.description, expense.amount_spent, expense.id))
                return "expense updated"
            except Exception as e:
                print(f"Error details: {e}")
                raise ValueError(f"Failed to update expense: {str(e)}")
