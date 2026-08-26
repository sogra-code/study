/**
 * Собирает Python-пакет (wheel + sdist) и подписывает сборку версией.
 */
def call() {
    echo 'Build: creating wheel and sdist'
    sh '''
        . venv/bin/activate
        python -m build
    '''
    env.APP_VERSION = org.devops.PipelineUtils.packageVersion(this)
    env.GIT_SHA = org.devops.PipelineUtils.gitShortCommit(this)
    echo "Built hello-app version ${env.APP_VERSION} (commit ${env.GIT_SHA})"
}
