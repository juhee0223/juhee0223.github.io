#!/usr/bin/env python3
"""Build a dependency-free, public portfolio from reviewed content."""
from pathlib import Path
from html import escape
import json
from hashlib import sha256

ROOT = Path(__file__).parent
DATA = json.loads((ROOT / 'content.json').read_text())
BASE = 'https://juhee0223.github.io'
STYLE_VERSION = sha256((ROOT / 'styles.css').read_bytes()).hexdigest()[:10]
CATS = {'service':'서비스 개발·운영','ai':'AI 응용','systems':'시스템 연구'}
def e(s): return escape(str(s), quote=True)
def tags(items): return ''.join(f'<span>{e(x)}</span>' for x in items)
def links(items): return ''.join(f'<a class="text-link" href="{e(x["url"])}" target="_blank" rel="noopener noreferrer">{e(x["label"])} <span aria-hidden="true">↗</span></a>' for x in items)
def shell(title, body, depth='', description='현장의 요구를 구체화하고, 구현과 검증으로 서비스에 반영하는 개발자 박주희의 포트폴리오.', canonical=''):
    home = depth+'index.html' if depth else ''
    return f'''<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)} · 박주희</title><meta name="description" content="{e(description)}">
<meta name="theme-color" content="#ffffff"><meta property="og:title" content="{e(title)} · 박주희"><meta property="og:description" content="{e(description)}"><meta property="og:type" content="website"><meta property="og:url" content="{BASE}/{canonical}">
<link rel="canonical" href="{BASE}/{canonical}"><link rel="icon" href="{depth}assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Noto+Sans+KR:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{depth}styles.css?v={STYLE_VERSION}"><script src="{depth}site.js" defer></script></head>
<body><a class="skip-link" href="#main">본문으로 바로가기</a>
<header class="site-header"><div class="nav-wrap"><a class="brand" href="{depth}index.html" aria-label="박주희 포트폴리오 홈"><span>박주희</span><small>Software Engineer</small></a>
<button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav">메뉴 <span aria-hidden="true">☰</span></button>
<nav id="site-nav" aria-label="주요 메뉴"><a href="{home}#projects">프로젝트</a><a href="{home}#research">논문·출판</a><a href="{home}#awards">수상</a><a href="{home}#activities">활동</a><a class="nav-contact" href="{home}#contact">연락처</a></nav></div></header>
{body}
<footer class="site-footer"><div class="container footer-inner"><p>박주희의 프로젝트와 연구 기록.<br><span>© 2026 Park Juhee</span></p><a href="https://github.com/juhee0223" target="_blank" rel="noopener noreferrer">GitHub ↗</a><a href="#main">맨 위로 ↑</a></div></footer>
</body></html>'''

def card(p, i):
    return f'''<article class="project-card" data-category="{e(p['category'])}"><div class="card-body"><div class="card-meta"><span>{e(p['kind'])}</span><span>{e(p['period'])}</span></div><h3><a href="projects/{e(p['slug'])}.html">{e(p['title'])}<span aria-hidden="true">↗</span></a></h3><p class="card-subtitle">{e(p['subtitle'])}</p><p class="card-description">{e(p['summary'])}</p><div class="tech-tags">{tags(p['tech'][:5])}</div><div class="card-result">{e(p['outcome'])}</div><a class="card-cta" href="projects/{e(p['slug'])}.html">프로젝트 읽기 <span aria-hidden="true">→</span></a></div></article>'''

def home():
    project_html=''.join(card(p,i) for i,p in enumerate(DATA['projects']))
    pubs=''.join(f'''<article class="publication"><div class="pub-main"><div class="eyebrow">{e(p['venue'])} / {e(p['year'])}</div><h3>{e(p['title'])}</h3><p>{e(p['description'])}</p><p class="pub-authors">{e(p['authors'])}</p><div class="pub-links">{links(p['links'])}</div></div><span class="pub-distinction">{e(p['distinction'])}</span></article>''' for i,p in enumerate(DATA['publications']))
    awards=''.join(f'''<article class="award"><time>{e(a['date'])}</time><div><h3>{e(a['title'])}</h3><p>{e(a['organization'])}</p></div><span>{e(a['project'])}</span></article>''' for a in DATA['awards'])
    activities=''.join(f'''<article class="activity"><div class="eyebrow">{e(a['period'])}</div><h3>{e(a['title'])}</h3><ul>{''.join(f'<li>{e(b)}</li>' for b in a['bullets'])}</ul></article>''' for a in DATA['activities'])
    return f'''<main id="main">
<section class="hero container"><p class="eyebrow">박주희 · SOFTWARE ENGINEER</p><h1>문제를 이해하고,<br>쓰이는 기술로 답합니다.</h1><p class="hero-description">현장의 요구를 구체화하고 AI를 활용해 구현하며,<br>실제 사용과 검증을 통해 더 나은 결과를 만듭니다.</p><div class="hero-actions"><a class="text-link" href="#projects">프로젝트 살펴보기 ↓</a><a class="text-link" href="https://github.com/juhee0223" target="_blank" rel="noopener noreferrer">GitHub ↗</a></div></section>
<section id="projects" class="section container"><div class="section-heading"><div><h2>프로젝트 <span class="section-count">9</span></h2></div><p>축제 서비스부터 AI 에이전트, 스토리지 연구까지.<br>각 프로젝트의 문제와 선택, 구현 과정을 담았습니다.</p></div><div class="filter-row"><div class="filters" role="group" aria-label="프로젝트 분야 필터"><button type="button" data-filter="all" class="active" aria-pressed="true">전체 <span>9</span></button><button type="button" data-filter="service" aria-pressed="false">서비스</button><button type="button" data-filter="ai" aria-pressed="false">AI 응용</button><button type="button" data-filter="systems" aria-pressed="false">시스템 연구</button></div><p class="project-count" role="status" aria-live="polite">9개의 프로젝트</p></div><div class="project-grid">{project_html}</div></section>
<section id="research" class="section research-section"><div class="container"><div class="section-heading"><div><h2>논문 · 출판 <span class="section-count">3</span></h2></div><p>스토리지 성능 분석과 텍스트 임베딩 연구,<br>그리고 운영체제 교재 기반 RAG 저서.</p></div><div class="publication-list">{pubs}</div></div></section>
<section id="awards" class="section container"><div class="section-heading"><div><h2>수상 <span class="section-count">4</span></h2></div><p>해커톤에서의 실행과 연구의 성과.</p></div><div class="award-list">{awards}</div></section>
<section id="activities" class="section activities-section"><div class="container"><div class="section-heading"><div><h2>활동</h2></div><p>행사 운영, 콘텐츠 기획, 실습·연구 지원 경험.</p></div><div class="activity-grid">{activities}</div><div class="skills-panel"><div><h3>사용 기술</h3></div><div class="skill-groups"><p><strong>Development</strong><span>Java · Spring Boot · React · TypeScript · Python · C / C++</span></p><p><strong>AI & Data</strong><span>LLM / RAG · LangGraph · PyTorch · OpenCV · scikit-learn</span></p><p><strong>Systems & Operations</strong><span>Redis · Kafka · MySQL · Docker · Kubernetes · AWS · Linux · Git</span></p></div></div></div></section>
<section id="contact" class="section container contact-section"><div><h2>연락처</h2><p>단국대학교 소프트웨어학과 4학년<br>정보처리기사 · 2026.09</p></div><div class="contact-links"><a class="contact-email" href="mailto:pjuhee23@dankook.ac.kr">pjuhee23@dankook.ac.kr <span>↗</span></a><div><a class="text-link" href="https://github.com/juhee0223" target="_blank" rel="noopener noreferrer">GitHub ↗</a><a class="text-link" href="https://github.com/juhee0223/juhee0223/blob/main/Resume_JuheePark.md" target="_blank" rel="noopener noreferrer">이력서 보기 ↗</a></div></div></section></main>'''

def detail(p,i):
    body_sections=''
    for j,s in enumerate(p['sections']):
        paragraphs=''.join(f'<p>{e(t)}</p>' for t in s.get('paragraphs',[]))
        bullets='<ul>'+''.join(f'<li>{e(t)}</li>' for t in s.get('bullets',[]))+'</ul>' if s.get('bullets') else ''
        body_sections+=f'<section class="case-section" id="section-{j}"><div><h2>{e(s["title"])}</h2>{paragraphs}{bullets}</div></section>'
    gallery=''
    if p['slug']=='danzzan':
        gallery='''<section class="case-gallery"><div class="eyebrow">서비스 화면</div><h2>서비스 화면</h2><div class="phone-gallery"><figure><a href="../assets/danzzan-ticketing.png" target="_blank" rel="noopener"><img src="../assets/danzzan-ticketing.png" alt="단짠 날짜별 예매 상태와 예매 버튼 화면" loading="lazy" width="941" height="1672"></a><figcaption>날짜별 예매 상태와 예매 흐름 · 팀 공동 산출물</figcaption></figure><figure><a href="../assets/danzzan-consent.png" target="_blank" rel="noopener"><img src="../assets/danzzan-consent.png" alt="단짠 예매 안내와 필수 동의 확인 화면" loading="lazy" width="941" height="1672"></a><figcaption>예매 안내와 필수 동의 확인 · 팀 공동 산출물</figcaption></figure></div></section>'''
    elif p['slug']=='olly':
        gallery='''<section class="case-gallery"><div class="eyebrow">로컬 MVP 데모</div><h2>오류 요청도 추적할 수 있도록</h2><figure><a href="../assets/olly-error.png" target="_blank" rel="noopener"><img class="wide-image" src="../assets/olly-error.png" alt="의도적으로 오류를 발생시킨 OLLY 데모에서 요청 ID, trace ID, 오류 상태가 함께 표시된 화면" width="1336" height="676" loading="lazy"></a><figcaption>실패 요청의 ID와 오류 상태를 유지하는 데모 화면 · 팀 공동 산출물</figcaption></figure></section>'''
    nav=''.join(f'<a href="#section-{j}">{e(s["title"])}</a>' for j,s in enumerate(p['sections']))
    nxt=DATA['projects'][(i+1)%len(DATA['projects'])]
    return f'''<main id="main"><div class="container"><a class="back-link" href="../index.html#projects">← 전체 프로젝트</a><section class="case-hero"><div><p class="eyebrow">{e(CATS[p['category']])}</p><h1>{e(p['title'])}</h1><p class="case-subtitle">{e(p['subtitle'])}</p><div class="case-meta"><span>{e(p['period'])}</span><span>{e(p['kind'])}</span></div><p class="case-summary">{e(p['summary'])}</p><div class="pub-links">{links(p['links'])}</div></div></section><div class="case-overview"><div><span class="eyebrow">기여와 역할</span><p>{e(p['role'])}</p></div><div><span class="eyebrow">결과</span><p>{e(p['outcome'])}</p></div><div><span class="eyebrow">사용 기술</span><div class="tech-tags">{tags(p['tech'])}</div></div></div><div class="case-layout"><aside class="case-toc"><span class="eyebrow">목차</span>{nav}<a href="#evidence">관련 자료</a></aside><div class="case-body">{body_sections}{gallery}<section id="evidence" class="case-evidence"><p class="eyebrow">관련 자료</p><h2>구현과 기록 살펴보기</h2><div class="evidence-links">{links(p['links'])}</div></section></div></div><nav class="project-pagination" aria-label="프로젝트 이동"><a href="../index.html#projects">← 프로젝트 목록</a><a href="{e(nxt['slug'])}.html"><small>다음 프로젝트</small><strong>{e(nxt['title'])} →</strong></a></nav></div></main>'''

(ROOT/'index.html').write_text(shell('Portfolio', home()))
(ROOT/'projects').mkdir(exist_ok=True)
for i,p in enumerate(DATA['projects']):
    (ROOT/'projects'/f'{p["slug"]}.html').write_text(shell(p['title'],detail(p,i),'../',p['summary'],f'projects/{p["slug"]}.html'))
(ROOT/'.nojekyll').touch()
(ROOT/'404.html').write_text(shell('페이지를 찾을 수 없습니다','<main id="main" class="container not-found"><p class="eyebrow">404 / NOT FOUND</p><h1>여기는 아직 빈 페이지예요.</h1><p>프로젝트 목록에서 다시 시작해 주세요.</p><a class="button primary" href="/">포트폴리오 홈으로 →</a></main>',depth='/'))
urls=['']+[f'projects/{p["slug"]}.html' for p in DATA['projects']]
(ROOT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{BASE}/{u}</loc></url>' for u in urls)+'</urlset>')
(ROOT/'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n')
print(f'Built homepage, {len(DATA["projects"])} project pages, 404, sitemap.')
