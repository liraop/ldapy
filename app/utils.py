"""

Utilities module

"""


def url_to_dn(domain_url):
    """
    Get an domain URL and parses it to DN.

    Args:
        "my.domain.my.org"

    Returns:
        "DC=my,DC=domain,DC=my,DC=org"

    """

    domain_dn = ""

    for w in domain_url.split('.'):
        domain_dn += "DC=" + w + ","

    #remove >last< semicolon
    return(domain_dn[0:-1])
