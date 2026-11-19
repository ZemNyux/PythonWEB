from django import template

register = template.Library()


@register.filter(name='format_phone')
def format_phone(value):
    if value is None:
        return ''

    digits = ''.join(ch for ch in str(value) if ch.isdigit())
    if not digits:
        return str(value)

    if digits.startswith('380') and len(digits) >= 12:
        rest = digits[3:]
        return f'+380 {rest[0:2]} {rest[2:5]} {rest[5:7]} {rest[7:9]}'.strip()

    if digits.startswith('44') and len(digits) >= 11:
        return f'+44 {digits[2:4]} {digits[4:8]} {digits[8:]}'.strip()

    if digits.startswith('33') and len(digits) >= 11:
        return f'+33 {digits[2]} {digits[3:5]} {digits[5:7]} {digits[7:9]} {digits[9:]}'.strip()

    if digits.startswith('49') and len(digits) >= 11:
        return f'+49 {digits[2:4]} {digits[4:8]} {digits[8:]}'.strip()

    return str(value)


@register.filter(name='status_badge')
def status_badge(is_active):
    return 'Пріоритетний напрям' if is_active else 'Стандартний напрям'
