from ftfy import fix_text, fix_text_segment
from ftfy.fixes import unescape_html


def test_entities():
    example = '&amp;\n<html>\n&amp;'
    assert fix_text(example) == '&\n<html>\n&amp;'
    assert fix_text_segment(example) == '&amp;\n<html>\n&amp;'

    assert fix_text(example, fix_entities=True) == '&\n<html>\n&'
    assert fix_text_segment(example, fix_entities=True) == '&\n<html>\n&'

    assert fix_text(example, fix_entities=False) == '&amp;\n<html>\n&amp;'
    assert fix_text_segment(example, fix_entities=False) == '&amp;\n<html>\n&amp;'

    assert fix_text_segment('&lt;&gt;', fix_entities=False) == '&lt;&gt;'
    assert fix_text_segment('&lt;&gt;', fix_entities=True) == '<>'
    assert fix_text_segment('&lt;&gt;') == '<>'
    assert fix_text_segment('jednocze&sacute;nie') == 'jednocześnie'
    assert fix_text_segment('JEDNOCZE&Sacute;NIE') == 'JEDNOCZEŚNIE'
    assert fix_text_segment('ellipsis&#133;', normalization='NFKC') == 'ellipsis...'
    assert fix_text_segment('ellipsis&#x85;', normalization='NFKC') == 'ellipsis...'
    assert fix_text_segment('broken&#x81;') == 'broken\x81'
    assert unescape_html('euro &#x80;') == 'euro €'
    assert unescape_html('EURO &EURO;') == 'EURO €'
    assert unescape_html('not an entity &#y20x6;') == 'not an entity &#y20x6;'
    assert unescape_html('partial entity &#20x6;') == 'partial entity x6;'
    assert unescape_html('&amp&amp&AMP') == '&&&'
    assert unescape_html('this&nbspis&nbspterrible') == 'this\xa0is\xa0terrible'
    assert unescape_html('JEDNOCZE&SACUTE;NIE') == 'JEDNOCZEŚNIE'
    assert unescape_html('V&SCARON;ICHNI') == 'VŠICHNI'
