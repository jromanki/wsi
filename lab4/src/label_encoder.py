def label_encode(series):
    categories = series.unique()
    cat_to_num = {cat: idx for idx, cat in enumerate(categories)}
    return series.map(cat_to_num)