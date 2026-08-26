/**
 * Уведомление о статусе сборки.
 *
 * Заглушка: пишет в лог. Сюда можно добавить отправку в Telegram,
 * Slack, e-mail или другой мессенджер.
 *
 * @param status  "SUCCESS", "FAILURE", "UNSTABLE" и т.п.
 */
def call(String status) {
    def buildNumber = env.BUILD_NUMBER ?: '?'
    echo "Notification: build #${buildNumber} finished with status: ${status}"
}
