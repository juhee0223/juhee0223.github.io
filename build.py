#!/usr/bin/env python3
"""Build a dependency-free, public portfolio from reviewed content."""
from pathlib import Path
from html import escape
import json

ROOT = Path(__file__).parent
DATA = json.loads((ROOT / 'content.json').read_text())
BASE = 'https://juhee0223.github.io'
CATS = {'service':'서비스 개발·운영','ai':'AI 응용','systems':'시스템 연구'}
def e(s): return escape(str(s), quote=True)
def tags(items): return ''.join(f'<span>{e(x)}</span>' for x in items)
def links(items): return ''.join(f'<a class="text-link" href="{e(x["url"])}" target="_blank" rel="noopener noreferrer">{e(x["label"])} <span aria-hidden="true">↗</span></a>' for x in items)
def shell(title, body, depth='', description='현장의 요구를 구체화하고, 구현과 검증으로 서비스에 반영하는 개발자 박주희의 포트폴리오.', canonical=''):
    home = depth+'index.html' if depth else ''
    return f'''<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)} · 박주희</title><meta name="description" content="{e(description)}">
<meta name="theme-color" content="#f7f8fc"><meta property="og:title" content="{e(title)} · 박주희"><meta property="og:description" content="{e(description)}"><meta property="og:type" content="website"><meta property="og:url" content="{BASE}/{canonical}">
<link rel="canonical" href="{BASE}/{canonical}"><link rel="icon" href="{depth}assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Noto+Sans+KR:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{depth}styles.css"><script src="{depth}site.js" defer></script></head>
<body><a class="skip-link" href="#main">본문으로 바로가기</a>
<header class="site-header"><div class="nav-wrap"><a class="brand" href="{depth}index.html" aria-label="박주희 포트폴리오 홈"><span class="brand-mark">jp<span>.</span></span><span>PARK JUHEE<small>SOFTWARE ENGINEER</small></span></a>
<button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav">메뉴 <span aria-hidden="true">☰</span></button>
<nav id="site-nav" aria-label="주요 메뉴"><a href="{home}#projects">Projects</a><a href="{home}#research">Research</a><a href="{home}#awards">Awards</a><a href="{home}#activities">Activities</a><a class="nav-contact" href="{home}#contact">Contact <span aria-hidden="true">↗</span></a></nav></div></header>
{body}
<footer class="site-footer"><div class="container footer-inner"><a class="brand-mark" href="{depth}index.html" aria-label="홈">jp<span>.</span></a><p>박주희의 프로젝트와 연구 기록.<br><span>© 2026 Park Juhee</span></p><a href="https://github.com/juhee0223" target="_blank" rel="noopener noreferrer">GitHub ↗</a><a href="#main">맨 위로 ↑</a></div></footer>
</body></html>'''

def art(p, detail=False):
    slug=p['slug']
    if slug=='danzzan':
        return '<div class="project-art art-danzzan" aria-hidden="true"><span class="art-eyebrow">CONNECTING THE FESTIVAL</span><div class="mini-ticket"><span>DANZZAN</span><strong>축제의 모든 순간을<br>하나의 서비스로.</strong><div>DISCOVER <b>→</b> BOOK <b>→</b> ENTER</div><i class="ticket-perf"></i><small>함께 만든 서비스, 현장에서 확인한 결과.</small></div><span class="art-number">01</span></div>'
    if slug=='conquer-health':
        return '<div class="project-art art-health" aria-hidden="true"><span class="art-eyebrow">EVALUATE. REFINE. REPEAT.</span><div class="health-notes"><span class="note note-back">EVALUATION<br><b>HealthBench</b></span><span class="note note-front">RESPONSE RULES<br><b>질문을 빠짐없이.<br>맥락에 맞게.</b><i>→ ANSWER_INSTRUCTION</i></span></div><span class="art-number">02</span></div>'
    if slug=='olly':
        return '<div class="project-art art-olly" aria-hidden="true"><span class="art-eyebrow">FOLLOW A SINGLE REQUEST</span><div class="trace-diagram"><span>request_id <b>→</b> trace_id</span><div><i></i><strong>retrieve</strong></div><div><i></i><strong>model</strong></div><div><i></i><strong>response</strong></div><small>검색부터 응답까지, 단계별로 관측.</small></div><span class="art-number">03</span></div>'
    marks={'sketch-to-spec':('SKETCH → SPEC','UI에서 요구사항으로'), 'sun-date':('善 + DATE','함께하는 시간의 가치'), 'gamegc':('GC / FTL','스토리지의 시간을 읽다'), 'dacon':('DATA → INSIGHT','데이터 속 차이를 찾다'), 'bird-repeller':('VISION × SOUND','인식에서 동작까지'), 'rocksdb':('WRITE / READ','정책이 성능을 바꾸는 방식')}
    big,small=marks[slug]
    return f'<div class="project-art art-compact art-{e(p["category"])}" aria-hidden="true"><span class="art-eyebrow">{e(CATS[p["category"]])}</span><strong>{e(big)}</strong><span>{e(small)}</span><div class="dot-grid"></div></div>'

def card(p, i):
    return f'''<article class="project-card" data-category="{e(p['category'])}"><a class="card-art-link" href="projects/{e(p['slug'])}.html" aria-label="{e(p['title'])} 상세 보기">{art(p)}</a><div class="card-body"><div class="card-meta"><span>{e(p['kind'])}</span><span>{e(p['period'])}</span></div><h3><a href="projects/{e(p['slug'])}.html">{e(p['title'])}<span aria-hidden="true">↗</span></a></h3><p class="card-subtitle">{e(p['subtitle'])}</p><p class="card-description">{e(p['summary'])}</p><div class="tech-tags">{tags(p['tech'][:5])}</div><div class="card-result"><span aria-hidden="true">✦</span> {e(p['outcome'])}</div><a class="card-cta" href="projects/{e(p['slug'])}.html">프로젝트 읽기 <span aria-hidden="true">→</span></a></div></article>'''

def home():
    project_html=''.join(card(p,i) for i,p in enumerate(DATA['projects']))
    pubs=''.join(f'''<article class="publication"><div class="pub-index">0{i+1}</div><div class="pub-main"><div class="eyebrow">{e(p['venue'])} / {e(p['year'])}</div><h3>{e(p['title'])}</h3><p>{e(p['description'])}</p><p class="pub-authors">{e(p['authors'])}</p><div class="pub-links">{links(p['links'])}</div></div><span class="pub-distinction">{e(p['distinction'])}</span></article>''' for i,p in enumerate(DATA['publications']))
    awards=''.join(f'''<article class="award"><time>{e(a['date'])}</time><div><h3>{e(a['title'])}</h3><p>{e(a['organization'])}</p></div><span>{e(a['project'])}</span><span class="award-star" aria-hidden="true">✳</span></article>''' for a in DATA['awards'])
    activities=''.join(f'''<article class="activity"><div class="eyebrow">{e(a['period'])}</div><h3>{e(a['title'])}</h3><ul>{''.join(f'<li>{e(b)}</li>' for b in a['bullets'])}</ul></article>''' for a in DATA['activities'])
    return f'''<main id="main">
<section class="hero container"><div class="hero-copy"><p class="eyebrow"><span class="status-dot"></span> PORTFOLIO / 2026</p><h1>문제를 이해하고,<br><span class="underlined">쓰이는 기술</span>로<br>답합니다<span class="hero-period">.</span></h1><p class="hero-description">안녕하세요, 개발자 <strong>박주희</strong>입니다.<br>현장의 요구를 구체화하고 AI를 활용해 구현하며,<br class="desktop-break"> 실제 사용과 검증을 통해 더 나은 결과를 만듭니다.</p><div class="hero-actions"><a class="button primary" href="#projects">프로젝트 살펴보기 <span>↘</span></a><a class="button secondary" href="https://github.com/juhee0223" target="_blank" rel="noopener noreferrer">GitHub ↗</a></div></div>
<div class="hero-board"><div class="board-top"><span>FROM IDEA TO REAL WORLD</span><span class="board-spark" aria-hidden="true">✳</span></div><div class="board-card board-build"><small>01 / BUILD</small><strong>서비스를 만들고</strong><span>단짠 · 실제 축제 서비스 운영</span><div class="board-path"><i>사용자</i><span>↔</span><i>서비스</i><span>↔</span><i>현장</i></div></div><div class="board-card board-explore"><small>02 / EXPLORE</small><strong>가능성을 탐구하고</strong><span>AI 응용 · 에이전트 · 시스템 연구</span></div><div class="board-card board-verify"><small>03 / VERIFY</small><strong>결과로 확인합니다</strong><span>평가 · 관측 · 실험 · 운영 피드백</span><span class="verify-check" aria-hidden="true">↗</span></div><div class="board-bottom"><span>BUILD WITH PURPOSE.</span><span>VERIFY WITH EVIDENCE.</span></div></div></section>
<div class="container"><div class="index-strip"><p>서비스에서 연구까지,<br><strong>경험의 폭과 깊이를 함께.</strong></p><a href="#projects"><b>09</b><span>PROJECTS</span></a><a href="#research"><b>03</b><span>PUBLICATIONS</span></a><a href="#awards"><b>04</b><span>AWARDS</span></a></div></div>
<section id="projects" class="section container"><div class="section-heading"><div><p class="eyebrow">01 / PROJECTS</p><h2>만들고, 연결하고,<br>직접 확인한 것들.</h2></div><p>축제 서비스부터 AI 에이전트, 스토리지 연구까지.<br>각 프로젝트의 문제와 선택, 구현 과정을 담았습니다.</p></div><div class="filter-row"><div class="filters" role="group" aria-label="프로젝트 분야 필터"><button type="button" data-filter="all" class="active" aria-pressed="true">전체 <span>9</span></button><button type="button" data-filter="service" aria-pressed="false">서비스</button><button type="button" data-filter="ai" aria-pressed="false">AI 응용</button><button type="button" data-filter="systems" aria-pressed="false">시스템 연구</button></div><p class="project-count" role="status" aria-live="polite">9개의 프로젝트</p></div><div class="project-grid">{project_html}</div></section>
<section id="research" class="section research-section"><div class="container"><div class="section-heading"><div><p class="eyebrow">02 / RESEARCH & PUBLICATIONS</p><h2>실험을 기록하고,<br>지식으로 나눕니다.</h2></div><p>스토리지 성능 분석과 텍스트 임베딩 연구,<br>그리고 운영체제 교재 기반 RAG 저서.</p></div><div class="publication-list">{pubs}</div></div></section>
<section id="awards" class="section container"><div class="section-heading"><div><p class="eyebrow">03 / AWARDS</p><h2>함께 도전해 얻은 결과.</h2></div><p>해커톤에서의 실행과 연구의 성과.</p></div><div class="award-list">{awards}</div></section>
<section id="activities" class="section activities-section"><div class="container"><div class="section-heading"><div><p class="eyebrow">04 / ACTIVITIES</p><h2>기술 밖에서도,<br>사람과 현장을 잇습니다.</h2></div><p>행사 운영, 콘텐츠 기획, 실습·연구 지원 경험.</p></div><div class="activity-grid">{activities}</div><div class="skills-panel"><div><p class="eyebrow">TOOLS I HAVE WORKED WITH</p><h3>프로젝트 속에서 사용한 기술</h3></div><div class="skill-groups"><p><strong>Development</strong><span>Java · Spring Boot · React · TypeScript · Python · C / C++</span></p><p><strong>AI & Data</strong><span>LLM / RAG · LangGraph · PyTorch · OpenCV · scikit-learn</span></p><p><strong>Systems & Operations</strong><span>Redis · Kafka · MySQL · Docker · Kubernetes · AWS · Linux · Git</span></p></div></div></div></section>
<section id="contact" class="section container contact-section"><div><p class="eyebrow">LET’S CONNECT</p><h2>다음 문제를,<br>함께 풀어가고 싶습니다.</h2><p>단국대학교 소프트웨어학과 4학년<br>정보처리기사 · 2026.09</p></div><div class="contact-links"><a class="contact-email" href="mailto:pjuhee23@dankook.ac.kr">pjuhee23@dankook.ac.kr <span>↗</span></a><div><a class="text-link" href="https://github.com/juhee0223" target="_blank" rel="noopener noreferrer">GitHub ↗</a><a class="text-link" href="https://github.com/juhee0223/juhee0223/blob/main/Resume_JuheePark.md" target="_blank" rel="noopener noreferrer">이력서 보기 ↗</a></div></div></section></main>'''

def detail(p,i):
    body_sections=''
    for j,s in enumerate(p['sections']):
        paragraphs=''.join(f'<p>{e(t)}</p>' for t in s.get('paragraphs',[]))
        bullets='<ul>'+''.join(f'<li>{e(t)}</li>' for t in s.get('bullets',[]))+'</ul>' if s.get('bullets') else ''
        body_sections+=f'<section class="case-section" id="section-{j}"><span class="case-index">0{j+1}</span><div><h2>{e(s["title"])}</h2>{paragraphs}{bullets}</div></section>'
    gallery=''
    if p['slug']=='danzzan':
        gallery='''<section class="case-gallery"><div class="eyebrow">PROJECT SCREENS</div><h2>서비스 화면</h2><div class="phone-gallery"><figure><a href="../assets/danzzan-ticketing.png" target="_blank" rel="noopener"><img src="../assets/danzzan-ticketing.png" alt="단짠 날짜별 예매 상태와 예매 버튼 화면" loading="lazy" width="941" height="1672"></a><figcaption>날짜별 예매 상태와 예매 흐름 · 팀 공동 산출물</figcaption></figure><figure><a href="../assets/danzzan-consent.png" target="_blank" rel="noopener"><img src="../assets/danzzan-consent.png" alt="단짠 예매 안내와 필수 동의 확인 화면" loading="lazy" width="941" height="1672"></a><figcaption>예매 안내와 필수 동의 확인 · 팀 공동 산출물</figcaption></figure></div></section>'''
    elif p['slug']=='olly':
        gallery='''<section class="case-gallery"><div class="eyebrow">DEMO / LOCAL MVP</div><h2>오류 요청도 추적할 수 있도록</h2><figure><a href="../assets/olly-error.png" target="_blank" rel="noopener"><img class="wide-image" src="../assets/olly-error.png" alt="의도적으로 오류를 발생시킨 OLLY 데모에서 요청 ID, trace ID, 오류 상태가 함께 표시된 화면" width="1336" height="676" loading="lazy"></a><figcaption>실패 요청의 ID와 오류 상태를 유지하는 데모 화면 · 팀 공동 산출물</figcaption></figure></section>'''
    nav=''.join(f'<a href="#section-{j}">{e(s["title"])}</a>' for j,s in enumerate(p['sections']))
    nxt=DATA['projects'][(i+1)%len(DATA['projects'])]
    return f'''<main id="main"><div class="container"><a class="back-link" href="../index.html#projects">← 전체 프로젝트</a><section class="case-hero"><div><p class="eyebrow">PROJECT {i+1:02d} / {e(CATS[p['category']])}</p><h1>{e(p['title'])}</h1><p class="case-subtitle">{e(p['subtitle'])}</p><div class="case-meta"><span>{e(p['period'])}</span><span>{e(p['kind'])}</span></div><p class="case-summary">{e(p['summary'])}</p><div class="pub-links">{links(p['links'])}</div></div>{art(p,True)}</section><div class="case-overview"><div><span class="eyebrow">CONTRIBUTION / CONTEXT</span><p>{e(p['role'])}</p></div><div><span class="eyebrow">RESULT</span><p>{e(p['outcome'])}</p></div><div><span class="eyebrow">TECHNOLOGY</span><div class="tech-tags">{tags(p['tech'])}</div></div></div><div class="case-layout"><aside class="case-toc"><span class="eyebrow">ON THIS PAGE</span>{nav}<a href="#evidence">관련 자료</a></aside><div class="case-body">{body_sections}{gallery}<section id="evidence" class="case-evidence"><p class="eyebrow">EVIDENCE & LINKS</p><h2>구현과 기록 살펴보기</h2><div class="evidence-links">{links(p['links'])}</div></section></div></div><nav class="project-pagination" aria-label="프로젝트 이동"><a href="../index.html#projects">← 프로젝트 목록</a><a href="{e(nxt['slug'])}.html"><small>NEXT PROJECT</small><strong>{e(nxt['title'])} →</strong></a></nav></div></main>'''

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
