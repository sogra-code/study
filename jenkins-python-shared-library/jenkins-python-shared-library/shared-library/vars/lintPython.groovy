/**
 * Проверяет код линтером flake8.
 */
def call() {
    echo 'Lint: running flake8'
    sh '''
        . venv/bin/activate
        flake8 src tests
    '''
}
