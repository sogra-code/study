/**
 * Архивует артефакты сборки и публикует HTML-отчёт о покрытии.
 *
 * @param config.artifacts  маска артефактов (по умолчанию "dist/*")
 */
def call(Map config = [:]) {
    def artifacts = config.artifacts ?: 'dist/*'
    echo 'Archive: saving build artifacts'
    archiveArtifacts artifacts: artifacts, fingerprint: true, allowEmptyArchive: true

    publishHTML(target: [
        reportDir: 'reports/coverage',
        reportFiles: 'index.html',
        reportName: 'Coverage Report'
    ])
}
