def profile_rows(rows: list[dict[str, str]]) -> dict:
    n_rows, columns = len(rows), list(rows[0].keys())
    col_profiles = []
    for col in columns:
        values = [r.get(col, "") for r in rows]
        usable = [v for v in values if not is_missing(v)]
        missing = len(values) - len(usable)
        inferred = infer_type(values)
        unique = len(set(usable))
        profile = {
            "name": col,
            "type": inferred,
            "missing": missing,
            "missing_pct": 100.0 * missing / n_rows if n_rows else 0.0,
            "unique": unique,
        }
        if inferred == "number":
            nums = [try_float(v) for v in usable]
            nums = [x for x in nums if x is not None]
            if nums:
                profile.update({"min": min(nums), "max": max(nums), "mean": sum(nums) / len(nums)})
        col_profiles.append(profile)
    return {"n_rows": n_rows, "n_cols": len(columns), "columns": col_profiles}







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

"""def text_stats(values: list[str], top_k: int = 5)->dict:
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
    sorted_counts = sorted(counts.items())
    for i in range (top_k+1):
        if counts
    top =  sorted(counts.items(), key=lambda kv: kv[1], reverse=True)[:top_k]
    return {"count":count, "missing": missing, "unique": unique, "top" : top}"""
def text_stats(values: list[str], top_k: int = 5) -> dict:
    usable = [v for v in values if not is_missing(v)]
    missing = len(values) - len(usable)

    counts: dict[str, int] = {}
    for v in usable:
        counts[v] = counts.get(v, 0) + 1

    top_items = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)[:top_k]
    top = [{"value": v, "count": c} for v, c in top_items]

    return {
        "count": len(usable),
        "missing": missing,
        "unique": len(counts),
        "top": top,
    }
