class ColumnProfile:
    def __init__(self, name: str, inferred_type: str, total: int, missing: int, unique: int):
        self.name = name
        self.inferred_type = inferred_type
        self.total = total
        self.missing = missing
        self.unique = unique
    @property
    def missing_pct(self) -> float:
        return self.missing/self.total * 100
    def to_dict(self) -> dict:
        return {"name": self.name, "inferred_type": self.inferred_type, "total": self.total, "missing": self.missing, "unique": self.unique}
    

