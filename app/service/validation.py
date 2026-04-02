def validate(data):
    if not isinstance(data, dict):
        return False

    try:
        total = float(data.get("total_amount", 0))
        vat = float(data.get("vat_amount", 0))

        return total >= vat
    except:
        return False