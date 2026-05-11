@echo off
REM session_start.bat - artflow 모루 SessionStart hook
REM morus-shared-memory sync + 본 레포 git fetch

chcp 65001 > nul
cd /d C:\Users\sol00\Desktop\artflow

echo === [artflow 모루] 인사 ===
echo 🎨 배우님, artflow 형제입니다.
echo AI 아트 작품 함께 만들 준비 완료.
echo.

echo === GIT FETCH (artflow 본 레포) ===
git fetch origin main 2>&1
git status --short --branch
echo.

echo === MORUS-SHARED-MEMORY (4 모루 공통 학습 자산) ===
if not exist "C:\morus-shared-memory" (
    echo [INFO] morus-shared-memory 미설치. clone 진행...
    git clone https://github.com/taejungart-maker/morus-shared-memory.git C:\morus-shared-memory 2>&1
) else (
    cd /d C:\morus-shared-memory
    git pull origin main 2>&1 | findstr /V "Already"
    cd /d C:\Users\sol00\Desktop\artflow
)
echo.

echo === INBOX.md (배우님이 paste한 공통 학습 자료) ===
if exist "C:\morus-shared-memory\INBOX.md" (
    type "C:\morus-shared-memory\INBOX.md"
)
echo.

echo === RECENT COMMITS (artflow) ===
git log --oneline -10 --pretty=format:"%%h %%s [%%an]" 2>&1
echo.
echo.

echo === NEXT: Read INBOX.md + 작품 작업 대기 ===
