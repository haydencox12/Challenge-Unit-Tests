import unittest
import datetime

class TestStockVisualizerInputs(unittest.TestCase):
    
    def test_symbol(self):
        # Symbols
        
        # Valid 
        self.assertTrue(symbol_check('AAPL'))
        self.assertTrue(symbol_check('TSLA'))
        self.assertTrue(symbol_check('AMZN'))
        self.assertTrue(symbol_check('GOOG'))
        self.assertTrue(symbol_check('FB'))
        self.assertTrue(symbol_check('NFLX'))
        self.assertTrue(symbol_check('MSFT'))

        # Wrong
        self.assertFalse(symbol_check(''))
        self.assertFalse(symbol_check('aapl'))
        self.assertFalse(symbol_check('Appl'))
        self.assertFalse(symbol_check('AAPL1'))
        self.assertFalse(symbol_check('AAPL123456'))

    def test_chart_type(self):
        # Chart types
        
        # Valid 
        self.assertTrue(chart_type_check('1'))
        self.assertTrue(chart_type_check('2'))

        # Wrong
        self.assertFalse(chart_type_check(''))
        self.assertFalse(chart_type_check('0'))
        self.assertFalse(chart_type_check('3'))
        self.assertFalse(chart_type_check('11'))

    def test_time_series(self):
        # Time series
        
        # Valid 
        self.assertTrue(time_series_check('1'))
        self.assertTrue(time_series_check('2'))
        self.assertTrue(time_series_check('3'))
        self.assertTrue(time_series_check('4'))

        # Wrong
        self.assertFalse(time_series_check(''))
        self.assertFalse(time_series_check('0'))
        self.assertFalse(time_series_check('5'))
        self.assertFalse(time_series_check('123'))

    def test_start_date(self):
        # Start dates
        
        # Valid 
        self.assertTrue(date_check('2022-01-01'))
        self.assertTrue(date_check('2022-05-31'))

        # Wrong
        self.assertFalse(date_check(''))
        self.assertFalse(date_check('2022/01/01'))
        self.assertFalse(date_check('01-01-2022'))
        self.assertFalse(date_check('2022-13-01'))
        self.assertFalse(date_check('2022-01-32'))

    def test_end_date(self):
        # End dates
        # Valid 
        self.assertTrue(date_check('2022-01-01'))
        self.assertTrue(date_check('2022-05-31'))

        # Wrong
        self.assertFalse(date_check(''))
        self.assertFalse(date_check('2022/01/01'))
        self.assertFalse(date_check('01-01-2022'))
        self.assertFalse(date_check('2022-13-01'))
        self.assertFalse(date_check('2022-01-32'))


# Helper functions

def symbol_check(symbol):
    """
    Check if symbol is valid: capitalized, 1-7 alpha characters.
    """
    return symbol.isalpha() and symbol.isupper() and len(symbol) <= 7

def chart_type_check(chart_type):
    """
    Check if chart type is valid: 1 numeric character, 1 or 2.
    """
    return chart_type.isdigit() and chart_type in ['1', '2']

def time_series_check(time_series):
    """
    Check if time series is valid: 1 numeric character, 1-4.
    """
    return time_series.isdigit() and time_series in ['1', '2', '3', '4']

def date_check(date):
    """
    Check if date is valid: date type YYYY-MM-DD.
    """
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
        return True
    except ValueError:
        return False