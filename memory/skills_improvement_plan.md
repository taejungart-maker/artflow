---
name: ""
description: Anthropic 4규칙 기준으로 현재 배우님 모루 시스템 진단 + 개선 우선순위.
metadata: 
  node_type: memory
  type: project
  originSessionId: cff6eec6-5fef-4765-a898-1b7c3dc79ff0
---

배우님 모루 시스템은 이미 Anthropic 엔지니어급 (20+ 스킬 운영 중). 부족한 부분은 **"도구 레이어(검증 스크립트)"**와 **"지속 개선 루틴"** 두 가지.

**Why:** 2026-05-17 Anthropic 스킬 전략 보고서 학습 후 진단. 배우님 현재 사업 규모(토큰 절약 중시)에서 가장 효과 큰 개선 포인트.

**How to apply:**

## 📊 현재 상태 진단

| 규칙 | 배우님 상태 | 개선 필요? |
|---|---|---|
| 1. 스킬 중심 | 🟢 20+ 스킬 운영 | X |
| 2. 3 레이어 (Description·Instructions·Tools) | 🟡 도구 레이어 약함 | ✅ |
| 3. 조립 가능성 | 🟢 카테고리별 분리됨 | X |
| 4. 매 세션 진화 | 🔴 거의 안 함 | ✅ |

## 🎯 개선 우선순위

### 우선순위 1: 토큰 절감용 스크립트 저장 (모루별)
| 모루 | 저장할 스크립트 |
|---|---|
| **1688-sourcing-analyzer** | 마진 계산 Python (CNY→KRW, 관세·물류·쿠팡수수료 자동) |
| **coupang-price-optimizer** | 가격 시뮬레이션 함수 (ROAS, 손익분기) |
| **coupang-reorder-planner** | 안전재고·리드타임 계산 |
| **coupang-dashboard** | 매출 집계·차트 생성 (matplotlib/plotly) |

→ AI 추론 대신 코드 실행 = 토큰 거의 0 + 결과 100% 정확

### 우선순위 2: 위험 작업에 disable-model-invocation
| 작업 | 적용 이유 |
|---|---|
| 쿠팡 상품 자동 등록 | 잘못 등록 시 큰 손실 |
| 1688 자동 발주 | 발주 실수는 돈 직결 |
| Git push (배우님 레포) | 사고 방지 |

### 우선순위 3: 주간 스킬 강화 루틴
- 매주 금요일 or 일요일에 "이번 주 대화 검토해서 자주 반복된 코칭·실수 패턴 정리해줘"
- 정리 결과 → 해당 모루 SKILL.md 업데이트
- 매일 X (토큰 소모), **주 1회**가 적정

### 우선순위 4: examples/ 폴더 누적
- 각 모루 폴더에 `examples/` 디렉토리
- 잘 나온 결과물 = 모범 케이스로 저장
- 모루가 다음에 참조 → 일관성·품질 향상

## ⚠️ 하지 말 것
- 스킬 수 더 늘리지 X — 이미 충분
- 매번 강화 X — 토큰 부담
- artflow(AI 아트)에 무리한 스킬화 X — 창의 영역은 자유 보존

## 🔗 관련

- [[anthropic_skills_strategy]] — 이론적 근거
- [[ceo_agent_decision]] — 스킬 조립 vs CEO 보류 결정 (스킬 조립이 더 가벼움)
- [[mcp_apify_workflow]] — 도구 레이어 확장 사례
