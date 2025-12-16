def basic_profile(rows: list[dict[str, str]]) -> dict:
    cols = get_columns(rows)
    report = {
        "summary": {
            "rows": len(rows),
            "columns": len(cols),
            "column_names": cols,
        },
        "columns": {},
    }

    for col in cols:
        values = column_values(rows, col)
        typ = infer_type(values)

        if typ == "number":
            stats = numeric_stats(values)
        else:
            stats = text_stats(values)

        report["columns"][col] = {"type": typ, **stats}

    return report


def get_columns(rows: list[dict[str, str]]) -> list[str]:
    if not rows:
        return []
    return list(rows[0].keys())



def is_missing(value: str | None) -> bool:
    value = value.strip().lower()
    missing_values = ["", "na", "n/a", "null", "none", "nan"]
    for v in missing_values:
        if value == v:
            return True
    return False

def try_float(value: str) -> float | None:
    try:
        return float(value)
    except ValueError:
        return None

def infer_type(values: list[str]) -> str:
    for i in values:
        if try_float(i) is None:
            return "text"    
    return ("text" for x in values if try_float(x) == None)

def column_values(rows: list[dict[str,str]], column: str) -> list[str]:

    return [row.get(column, "") for row in rows]

def numeric_stats(values: list[str])->dict:
    list = []
    for i in values:
        if not is_missing(i):
            i = try_float(i)
            list.append(i)
    count = len(list)
    missing = count - len(values)
    unique = len(set(list))
    min = min(list)
    max = max(list)
    mean = sum(list)/count
    return {"count":count, "missing": missing, "unique": unique, "min": min, "max": max ,"mean": mean }

def text_stats(values: list[str], top_k: int = 5)->dict:
    list = []
    for i in values:
        if not is_missing(i):
            if try_float(i) == None:
                list.append(i)     
    count = len(list)
    missing = count - len(values)
    unique = len(set(list))
    counts: dict[str,str] = {}
    for i in list:
        counts[i] = counts.get(i,0)+1
    """sorted_counts = sorted(counts.items())
    for i in range (top_k+1):
        if counts"""
    top =  sorted(counts.items(), key=lambda kv: kv[1], reverse=True)[:top_k]
    return {"count":count, "missing": missing, "unique": unique, "top" : top}
