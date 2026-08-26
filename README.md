# jenkins-python-shared-library

Учебный проект: **сборка Python-приложения в Jenkins** с помощью
`Jenkinsfile` и **Jenkins Shared Library**.

Идея проекта: весь набор действий по сборке (установка зависимостей,
линт, тесты, сборка пакета, публикация артефактов) вынесен в общую
библиотеку `shared-library/`, а `Jenkinsfile` остаётся коротким и
переиспользует её шаги.

## Структура репозитория

```
jenkins-python-shared-library/
├── Jenkinsfile                 # пайплайн: использует @Library и шаги из vars/
├── src/hello_app/              # Python-пакет приложения
│   ├── __init__.py
│   ├── greeter.py              # функция greet(), word_count()
│   ├── stats.py                # функция summarize() — статистика чисел
│   └── cli.py                  # CLI: hello-app --name Jenkins
├── tests/                      # тесты (unittest, запускаются и через pytest)
├── pyproject.toml              # метаданные пакета, точка входа hello-app
├── requirements.txt            # боевые зависимости (только stdlib)
├── requirements-dev.txt        # pytest, pytest-cov, flake8, build
├── Dockerfile                  # опционально: образ приложения
├── .flake8                     # конфигурация flake8
└── shared-library/             # Jenkins Shared Library
    ├── src/org/devops/PipelineUtils.groovy
    └── vars/                   # setupPythonEnv, lintPython, runPythonTests,
                                # buildPythonApp, publishReport, notifyBuildStatus
```

## Приложение

```
PYTHONPATH=src python3 -m hello_app.cli --name Jenkins
# Hello, Jenkins!

PYTHONPATH=src python3 -m unittest discover -s tests -v   # локальный запуск тестов
```

Пакет собирается в wheel и sdist: `python -m build` (результат — в `dist/`).

## Jenkinsfile и Shared Library

Каждая стадия пайплайна вызывает шаг из библиотеки:

| Стадия | Шаг библиотеки | Что делает |
| --- | --- | --- |
| Checkout | `checkout scm` | клонирует репозиторий |
| Setup environment | `setupPythonEnv` | создаёт venv, ставит зависимости |
| Lint | `lintPython` | flake8 по `src` и `tests` |
| Test | `runPythonTests` | pytest + покрытие, публикует JUnit-отчёт |
| Build | `buildPythonApp` | `python -m build`, подписывает версией из pyproject.toml |
| Archive | `publishReport` | архивирует `dist/*`, публикует HTML-отчёт о покрытии |
| post | `notifyBuildStatus` | логирует статус (заглушка под Telegram/Slack) |

## Настройка Jenkins

### 1. Установите плагины

Pipeline, Git, JUnit, HTML Publisher, Workspace Cleanup, Timestamper.

### 2. Подключите Shared Library

`Manage Jenkins` → `System` → **Global Pipeline Libraries** → `Add`:

- **Name**: `devops-shared-library`
- **Default version**: `main`
- **Retrieval method**: `Modern SCM` → `Git`
- **Project repository**: URL git-репозитория этой библиотеки
  (в учебном проекте — тот же репозиторий, каталог `shared-library`)

Имя библиотеки должно совпадать с `@Library('devops-shared-library')` в Jenkinsfile.

### 3. Создайте Pipeline-джобу

1. `New Item` → имя (например, `hello-app-build`) → тип **Pipeline**.
2. Раздел **Pipeline**:
   - **Definition**: `Pipeline script from SCM`;
   - **SCM**: `Git` → укажите URL репозитория приложения;
   - **Script Path**: `Jenkinsfile`.
3. Нажмите **Build Now**.

### 4. Что увидите в сборке

- Стадии `Checkout → Setup → Lint → Test → Build → Archive`;
- JUnit-отчёт о тестах и тренд на странице сборки;
- HTML-отчёт `Coverage Report` о покрытии кода;
- артефакт `hello-app-1.0.0-py3-none-any.whl` и sdist в разделе Artifacts.

## Как расширить проект

- **Docker-образ**: добавьте стадию с `docker build` (в `Dockerfile` уже
  есть всё необходимое);
- **Уведомления**: замените заглушку в `notifyBuildStatus` на вызов
  Telegram/Slack API;
- **Версии**: в реальном проекте версию можно брать из тега git или
  генерировать в `PipelineUtils`;
- **Параллелизм**: запустите тесты в несколько потоков через
  `pytest -n auto` (потребуется `pytest-xdist`).

## Требования

- Jenkins 2.x с плагинами из раздела «Настройка Jenkins»;
- агент с Python 3.9+ (на этапе `Setup environment` создаётся venv);
- доступ агента в интернет для `pip install`.
