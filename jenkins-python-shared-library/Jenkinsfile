/*
 * Учебный Jenkinsfile: сборка Python-приложения с помощью Jenkins Shared Library.
 *
 * Библиотека 'devops-shared-library' подключается в Jenkins:
 *   Manage Jenkins -> System -> Global Pipeline Libraries
 *   (см. README.md, раздел «Настройка Jenkins»).
 *
 * Каждый шаг (setupPythonEnv, lintPython, runPythonTests, ...) определён
 * в каталоге shared-library/vars и подтягивается из библиотеки.
 */

@Library('devops-shared-library') _

pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup environment') {
            steps {
                setupPythonEnv(python: 'python3')
            }
        }

        stage('Lint') {
            steps {
                lintPython()
            }
        }

        stage('Test') {
            steps {
                runPythonTests()
            }
        }

        stage('Build') {
            steps {
                buildPythonApp()
            }
        }

        stage('Archive') {
            steps {
                publishReport()
            }
        }
    }

    post {
        success {
            notifyBuildStatus('SUCCESS')
        }
        failure {
            notifyBuildStatus('FAILURE')
        }
        always {
            cleanWs()
        }
    }
}
