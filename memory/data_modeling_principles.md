---
name: artflow-memory
description: SQLD 정규화 원칙과 NULL 철학을 artflow 메모리·inspirations 폴더 운영에 적용. 데이터 중복/누락 처리 원칙.
metadata: 
  node_type: memory
  type: reference
  originSessionId: cff6eec6-5fef-4765-a898-1b7c3dc79ff0
---

SQLD 기출 학습에서 artflow 운영에 직접 적용 가능한 2가지 원칙. 나머지 SQL 실무 지식은 mbc_final/쿠팡 모루 영역.

---

## 🎯 원칙 1: 정규화 사고법 → memory/ 폴더 운영

| 정규화 | SQL 의미 | artflow 적용 |
|---|---|---|
| **1NF (1차 정규형)** | 한 속성은 한 개의 값 | 한 메모리 파일 = 한 주제만 (혼합 금지) |
| **2NF (2차 정규형)** | 부분 함수 종속 제거 | 메모리를 카테고리별로 분리 (관계철학·CEO결정·영감 등 별도 파일) |
| **3NF (3차 정규형)** | 이행 함수 종속 제거 (A→B→C) | 메모리 간 직접 [[link]]만 사용, 간접 참조 체인 회피 |
| **반정규화** | 성능 위해 의도적 중복 | 자주 참조되는 핵심 원칙은 여러 메모리에 반복 명시 가능 (의도적) |

**핵심 메시지**: 메모리도 데이터다. 중복·이상현상 방지를 위해 분리·연결 설계 필요.

---

## 🎯 원칙 2: NULL = "아직 알려지지 않은 미지의 값"

| 상황 | NULL 적용 |
|---|---|
| **artist_info.md 작가 미확인** | 0이나 공백이 아닌 **"미확인"** 명시 |
| **작품 제작연도 모름** | NULL 처리 + placeholder 명시 |
| **배우님이 후속 확인 약속** | NULL 상태 → 추후 업데이트 예정 표기 |

**핵심 메시지**: 데이터가 비어있는 것과 "아직 모르는 것"은 다름. 미확인 정보는 명시적으로 표시.

---

## ⚠️ artflow가 학습하지 않은 영역 (다른 모루 영역)

| 영역 | 담당 모루 |
|---|---|
| SQL 함수 (COALESCE, ROUND 등) | mbc_final |
| 조인 (INNER/OUTER/HASH) | mbc_final |
| 윈도우 함수 (RANK, NTILE) | mbc_final, 쿠팡 dashboard |
| 트랜잭션 제어 | mbc_final |
| DDL/DCL (GRANT, REVOKE) | DB 관리 |
| 계층형 쿼리 (CONNECT BY) | mbc_final |

→ **SQLD 기출 PDF 전체는 mbc_final 모루 창에서 본격 학습 권장**

---

## 🔗 관련 메모리

- [[moru_philosophy]] — 모루 가족 역할 분담 철학
- [[skills_improvement_plan]] — 스킬별 영역 분리 원칙
