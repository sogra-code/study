/**
 * Настраивает виртуальное окружение Python и устанавливает зависимости.
 *
 * @param config.python  интерпретатор (по умолчанию "python3")
 */
def call(Map config = [:]) {
    def python = config.python ?: 'python3'
    echo "Setup: creating virtualenv with ${python}"
    sh """
        ${python} -m venv venv
        . venv/bin/activate
        pip install --upgrade pip
        pip install -r requirements.txt -r requirements-dev.txt
        pip install -e .
    """
}
