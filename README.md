# Park Juhee · Portfolio

[포트폴리오 보기](https://juhee0223.github.io)

서비스 개발·운영, AI 응용, 시스템 연구 프로젝트를 담은 개인 포트폴리오입니다.

## 수정 및 빌드

외부 패키지 설치 없이 Python 3으로 생성합니다.

```sh
python3 build.py
python3 -m http.server 8765
```

- `content.json`: 프로젝트, 출판, 수상, 활동 내용
- `build.py`: 공통 레이아웃과 정적 HTML 생성
- `styles.css`, `site.js`: 반응형 스타일과 필터·메뉴
- `assets/`: 서비스 화면과 아이콘
- `projects/`: 프로젝트별 상세 페이지

내용을 수정한 뒤 생성된 HTML도 함께 커밋합니다. GitHub Pages는 `main` 브랜치의 루트 디렉터리를 게시합니다.

서비스 화면은 프로젝트 팀의 공동 산출물이며, 상세 페이지에서 개인 기여와 팀 결과를 구분했습니다.
