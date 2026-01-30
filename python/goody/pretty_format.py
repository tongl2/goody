def fmt_array(array, *, items_per_line=8, indent=0):
    """Format: [1, 2, 3, ...] with 20 items per line, aligned"""
    max_width = max(len(str(i)) for i in array)
    lines = []
    for i in range(0, len(array), items_per_line):
        chunk = array[i:i + items_per_line]
        lines.append(', '.join(f'{idx:>{max_width}}' for idx in chunk) + ',')

    ret = ''
    indent_str = ' ' * indent
    if lines:
        ret += f'{indent_str}[ {lines[0]}'
        for line in lines[1:]:
            ret += f'\n{indent_str}  {line}'
        ret += f' ]'
    return ret
