"""
Provides utility functions, specifically for extracting the domain from a URL.
"""

import tldextract

def extract_domain(url):
    """
    Extracts the domain from a URL using tldextract.

    Example:
        url='http://sub.example.com' -> domain='example.com'

    Args:
        url (str): The URL string from which to extract the domain.

    Returns:
        str: The domain plus suffix, e.g. 'example.com'.
    """
    # Use tldextract to parse the URL, extracting subdomain, domain, and suffix
    result = tldextract.extract(url)
    # Join the domain and suffix into a standard domain string
    return f"{result.domain}.{result.suffix}"
