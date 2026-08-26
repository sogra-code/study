# Jenkins Shared Library для сборки Python-приложений

Эта библиотека содержит шаги (global variables) и утилиты, которые
используются из `Jenkinsfile`. В реальном проекте библиотека живёт в
**отдельном git-репозитории**, а здесь для учебного проекта лежит рядом
с приложением.

## Структура

```
shared-library/
├── src/org/devops/
│   └── PipelineUtils.groovy   # класс-утилита (gitShortCommit, packageVersion)
└── vars/
    ├── setupPythonEnv.groovy  # создание venv + установка зависимостей
    ├── lintPython.groovy      # flake8
    ├── runPythonTests.groovy  # pytest + покрытие + JUnit-отчёт
    ├── buildPythonApp.groovy  # python -m build (wheel + sdist)
    ├── publishReport.groovy   # архив артефактов + HTML-отчёт о покрытии
    └── notifyBuildStatus.groovy  # уведомление о статусе (заглушка)
```

## Как подключить в Jenkins

1. `Manage Jenkins` → `System` → раздел `Global Pipeline Libraries`.
2. Нажать `Add`:
   - **Name**: `devops-shared-library` (имя должно совпадать с `@Library` в Jenkinsfile);
   - **Default version**: `main`;
   - **Retrieval method**: `Modern SCM` → `Git`;
   - **Project repository**: URL репозитория с этой библиотекой.
3. Сохранить.

## Требуемые плагины Jenkins

- Pipeline
- Git
- JUnit (шаг `junit`)
- HTML Publisher (шаг `publishHTML`)
- Workspace Cleanup (шаг `cleanWs`)
- Timestamper (опция `timestamps`)
