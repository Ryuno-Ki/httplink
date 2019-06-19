from sys import version_info

if version_info[0] == 2:
    from .backport import (
        decode_extended_value,
        Link,
        ParsedLinks,
        parse_link_header,
        unescape
    )
else:  # Python 3
    from .modern import (
        decode_extended_value,
        Link,
        ParsedLinks,
        parse_link_header,
        unescape
    )
