import re
from user_scanner.core.helpers import get_random_user_agent
from user_scanner.core.orchestrator import Result, make_request

def validate_blogger(user):
    url = f"https://{user}.blogspot.com/"
    
    headers = {
        "User-Agent": get_random_user_agent(),
    }
    
    resp = make_request(url, headers=headers, http2=True, follow_redirects=True)
    title_match = re.search(r'<title>(.*?)</title>', resp.text, re.IGNORECASE)
    title = title_match.group(1).strip() if title_match else ""

    if resp.status_code == 404 or title == "Blog not found":
        return Result.available(url=url)
    elif resp.status_code == 200:
        extra = {"title": title} if title else {}
        return Result.taken(extra=extra, url=url)

    return Result.error(f"Unexpected response status: {resp.status_code}")
