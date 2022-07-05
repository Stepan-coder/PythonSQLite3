import enum


class DBType(enum.Enum):
    """
    Enum, for storing possible types of table fields
    """
    NULL = "NULL"  # Null value
    INTEGER = "INTEGER"  # Integer
    REAL = "REAL"  # Floating point number
    TEXT = "TEXT"  # Text
    BLOB = "BLOB"  # Binary representation of large objects stored exactly as it was entered