package org.devops

/**
 * Вспомогательные утилиты пайплайна.
 * Доступны из vars-шагов и из Jenkinsfile как org.devops.PipelineUtils.
 */
class PipelineUtils implements Serializable {

    static final String DEFAULT_VERSION_FILE = 'pyproject.toml'

    /** Возвращает короткий SHA текущего коммита (8 символов). */
    static String gitShortCommit(script) {
        return script.sh(
            script: 'git rev-parse --short=8 HEAD',
            returnStdout: true
        ).trim()
    }

    /** Читает version = "x.y.z" из pyproject.toml (без внешних библиотек). */
    static String packageVersion(script, String versionFile = DEFAULT_VERSION_FILE) {
        String content = script.readFile(versionFile)
        for (String line : content.readLines()) {
            String trimmed = line.trim()
            if (trimmed.startsWith('version')) {
                return trimmed.split('=')[1].trim().replaceAll(/["']/, '')
            }
        }
        return '0.0.0'
    }
}
