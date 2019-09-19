def memorize(f):
    """
    汎用メモ化関数
    引数:
        f:メモ化再帰を行いたい関数
    """
    table = {}
    def func(*args):
        if not args in table:
            table[args] = f(*args)
        return table[args]
    return func