/**
 * Запускает тесты pytest с покрытием и публикует JUnit-отчёт.
 *
 * @param config.testResults  путь к JUnit-отчёту (по умолчанию "reports/junit.xml")
 */
def call(Map config = [:]) {
    def testResults = config.testResults ?: 'reports/junit.xml'
    echo 'Test: running pytest with coverage'
    sh '''
        . venv/bin/activate
        mkdir -p reports
        pytest -v \
               --junitxml=reports/junit.xml \
               --cov=src \
               --cov-report=term-missing \
               --cov-report=html:reports/coverage
    '''
    junit testResults: testResults
}
