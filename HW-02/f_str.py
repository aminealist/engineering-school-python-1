def format_number(number: float) -> str:
    return '{:*^30}'.format('{:,.3f}'.format(number)).replace(',', ' ')


print(format_number(12348842390.28174))
