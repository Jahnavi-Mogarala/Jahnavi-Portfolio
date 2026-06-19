import re
with open(r'C:\Users\mogar\.gemini\antigravity\brain\e26b699c-b43f-4ecd-9447-4dbcc9375400\.system_generated\steps\9\content.md', 'r', encoding='utf-8') as f:
    content = f.read()
    repos = re.findall(r'href="/Jahnavi-Mogarala/([^/]+)"', content)
    from collections import Counter
    print("Repos found:", [k for k,v in Counter(repos).items() if k not in ['followers', 'following', 'repositories', '']][:10])
